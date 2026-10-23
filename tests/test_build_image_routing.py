#!/usr/bin/env python3
"""Run only the actual workflow's routing shell against temporary Git commits.

Requires the already-installed PyYAML. No Docker, registry or remote calls.
Usage: python3 test_build_image_routing.py path/to/build-images.yml
"""
import os
from pathlib import Path
import subprocess
import sys
import tempfile

import yaml


def main():
    workflow = yaml.safe_load(Path(sys.argv[1]).read_text())
    job = workflow['jobs']['build-and-push']
    matrix = job['strategy']['matrix']['include']
    routing = next(step['run'] for step in job['steps'] if step.get('id') == 'changes')
    failures = []
    checks = 0

    with tempfile.TemporaryDirectory(prefix='infra-routing-') as directory:
        root = Path(directory)

        def git(*args):
            return subprocess.check_output(
                ['git', '-c', 'user.name=Offline audit', '-c',
                 'user.email=offline-audit@example.invalid', *args],
                cwd=root, text=True, stderr=subprocess.PIPE).strip()

        def commit(message):
            git('add', '.')
            git('commit', '-m', message)
            return git('rev-parse', 'HEAD')

        git('init', '-q')
        for item in matrix:
            target = root / item['path'] / 'Dockerfile'
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text('# offline fixture\n')
        (root / 'README.md').write_text('baseline\n')
        workflow_path = root / '.github/workflows/build-images.yml'
        workflow_path.parent.mkdir(parents=True)
        workflow_path.write_text('# baseline\n')
        before = commit('baseline')

        def route(item, after, expected, scenario, ref='refs/heads/main'):
            nonlocal checks
            checks += 1
            script = routing
            for expression, value in {
                'github.ref': ref,
                'github.event.before': before,
                'github.sha': after,
                'matrix.path': item['path'],
            }.items():
                script = script.replace('${{ ' + expression + ' }}', value)
            output = root / '.git/routing-output'
            output.unlink(missing_ok=True)
            result = subprocess.run(
                ['bash', '--noprofile', '--norc', '-e', '-o', 'pipefail', '-c', script],
                cwd=root, env={**os.environ, 'GITHUB_OUTPUT': str(output)},
                text=True, capture_output=True)
            actual = output.read_text().strip() if output.exists() else ''
            expected_output = 'changed=' + str(expected).lower()
            if result.returncode or actual != expected_output:
                failures.append(f'{scenario}/{item["project"]}: expected '
                                f'{expected_output}, got {actual!r}, exit={result.returncode}')

        for selected in matrix:
            git('reset', '--hard', before)
            (root / selected['path'] / 'Dockerfile').write_text('# changed\n')
            after = commit('change one project')
            for item in matrix:
                route(item, after, item['project'] == selected['project'],
                      'changed-' + selected['project'])

        for relative, scenario in [
            ('docs/unrelated.md', 'unrelated-doc'),
            ('.github/workflows/build-images.yml', 'workflow-only-push'),
            ('compose/production/postgres2/Dockerfile', 'directory-prefix-lookalike'),
        ]:
            git('reset', '--hard', before)
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text('# changed\n')
            after = commit(scenario)
            for item in matrix:
                route(item, after, False, scenario)

        git('reset', '--hard', before)
        selected = next(item for item in matrix if item['project'] == 'postgres')
        (root / selected['path'] / 'Dockerfile').unlink()
        after = commit('delete project file')
        for item in matrix:
            route(item, after, item['project'] == 'postgres', 'deleted-file')

        for item in matrix:
            route(item, before, True, 'tag-all-projects', 'refs/tags/v1.2.3')

    for failure in failures:
        print('FAIL', failure)
    print(f'{checks - len(failures)}/{checks} routing assertions passed; '
          f'{len(failures)} failed; no Docker or remote commands executed')
    return bool(failures)


if __name__ == '__main__':
    sys.exit(main())
