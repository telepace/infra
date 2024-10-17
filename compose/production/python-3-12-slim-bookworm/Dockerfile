# 使用官方 Python 基础镜像
FROM python:3.12.4-slim-bookworm

# 设置时区
ENV TZ=Asia/Shanghai
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    tzdata \
    && ln -sf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 安装基础依赖库
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    wget \
    git \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /app

# 安装 Python 常用库
RUN pip install --no-cache-dir \
    requests \
    numpy \
    pandas \
    scipy

# 创建非 root 用户，提升安全性
# RUN useradd -m telepace && chown -R telepace /app
# USER telepace

# 设置 Python 环境变量
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# 暴露工作目录
VOLUME /app

# 镜像完成标记
LABEL maintainer="3293172751nss@gmail.com" \
      description="A base Python image with common dependencies"

# 运行测试命令，确保环境正常
CMD ["python", "--version"]
