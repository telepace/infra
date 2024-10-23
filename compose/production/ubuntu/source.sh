#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

export OS=$(/telepace/tools/get_os.sh)
export ARCH=$(/telepace/tools/get_arch.sh)

exec "$@"
