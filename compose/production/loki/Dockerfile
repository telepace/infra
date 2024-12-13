FROM grafana/loki:2.9.0

COPY ./compose/production/loki/loki-config.yml /etc/loki/

USER root

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD wget --quiet --tries=1 --spider http://localhost:3100/ready || exit 1 