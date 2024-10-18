FROM redis:8.0-M01

# 设置时区
ENV TZ=Asia/Shanghai

# 安装必要的包（如需要）
RUN apt-get update && \
    apt-get install -y locales && \
    sed -i 's/# zh_CN.UTF-8 UTF-8/zh_CN.UTF-8 UTF-8/' /etc/locale.gen && \
    sed -i 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# 配置本地化
ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8

# 复制自定义配置文件
COPY ./compose/production/redis/redis.conf /usr/local/etc/redis/redis.conf

# 设置工作目录
WORKDIR /usr/local/etc/redis

# 健康检查
HEALTHCHECK CMD /bin/nc -z 127.0.0.1 6379

# 启动 Redis 时使用自定义配置
CMD ["redis-server", "redis.conf"]
