FROM prom/node-exporter:latest

# 设置默认参数
ENV PATH_SYSFS=/host/sys \
    PATH_PROCFS=/host/proc \
    PATH_ROOTFS=/rootfs

# 健康检查
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD wget --quiet --tries=1 --spider http://localhost:9100/metrics || exit 1 