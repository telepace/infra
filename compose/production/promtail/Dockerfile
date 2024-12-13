FROM grafana/promtail:latest

COPY ./compose/production/promtail/promtail-config.yml /etc/promtail/

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD wget --quiet --tries=1 --spider http://localhost:9080/ready || exit 1 