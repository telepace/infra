FROM redis:7.0.0

# 设置时区
ENV TZ=Asia/Shanghai

# 复制自定义配置文件
COPY ./compose/production/redis/redis.conf /usr/local/etc/redis/redis.conf

# 复制业务相关的初始化脚本或模块（如有）
# COPY your_custom_module.so /usr/local/lib/redis/

# 设置工作目录
WORKDIR /usr/local/etc/redis

# 启动 Redis 时使用自定义配置
CMD ["redis-server", "redis.conf"]
