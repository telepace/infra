# Infra 容器化基础架构镜像支持

本仓库旨在为 **Infra** 项目提供容器化的基础架构镜像支持，包括基础镜像的开源镜像源地址，如阿里云镜像、GitHub 镜像以及 Docker Hub 镜像。

## 镜像源地址

每个应用的镜像均可从以下镜像源获取：

- **Docker Hub**: `docker.io/telepace/ai_feedback_production_${project}`
- **阿里云镜像仓库**: `registry.cn-hangzhou.aliyuncs.com/telepace/ai_feedback_production_${project}`
- **GitHub Container Registry**: `ghcr.io/telepace/ai_feedback_production_${project}`

其中，`${project}` 为以下应用名称之一：

- `aws`
- `nginx`
- `postgres`
- `python-3-12-slim-bookworm`
- `python`
- `redis`
- `traefik`

## 应用列表及说明

### 1. AWS

- **描述**: 包含 Amazon AWS CLI 工具的镜像，便于在容器中执行 AWS 命令行操作。
- **拉取命令**:
  - Docker Hub:
    ```bash
    docker pull docker.io/telepace/ai_feedback_production_aws
    ```
  - 阿里云镜像仓库:
    ```bash
    docker pull registry.cn-hangzhou.aliyuncs.com/telepace/ai_feedback_production_aws
    ```
  - GitHub Container Registry:
    ```bash
    docker pull ghcr.io/telepace/ai_feedback_production_aws
    ```

### 2. Nginx

- **描述**: 基于 Nginx 的高性能 HTTP 和反向代理服务器镜像。
- **拉取命令**:
  ```bash
  # Docker Hub
  docker pull docker.io/telepace/ai_feedback_production_nginx

  # 阿里云镜像仓库
  docker pull registry.cn-hangzhou.aliyuncs.com/telepace/ai_feedback_production_nginx

  # GitHub Container Registry
  docker pull ghcr.io/telepace/ai_feedback_production_nginx
  ```

### 3. Postgres

- **描述**: PostgreSQL 数据库镜像，支持最新版本的关系型数据库服务。
- **拉取命令**:
  ```bash
  docker pull docker.io/telepace/ai_feedback_production_postgres
  docker pull registry.cn-hangzhou.aliyuncs.com/telepace/ai_feedback_production_postgres
  docker pull ghcr.io/telepace/ai_feedback_production_postgres
  ```

### 4. Python-3.12-slim-bookworm

- **描述**: 基于 Debian Bookworm 的 Python 3.12 精简版镜像，适用于轻量级 Python 应用。
- **拉取命令**:
  ```bash
  docker pull docker.io/telepace/ai_feedback_production_python-3-12-slim-bookworm
  docker pull registry.cn-hangzhou.aliyuncs.com/telepace/ai_feedback_production_python-3-12-slim-bookworm
  docker pull ghcr.io/telepace/ai_feedback_production_python-3-12-slim-bookworm
  ```

### 5. Python

- **描述**: 通用的 Python 镜像，适用于各种 Python 应用程序的开发和部署。
- **拉取命令**:
  ```bash
  docker pull docker.io/telepace/ai_feedback_production_python
  docker pull registry.cn-hangzhou.aliyuncs.com/telepace/ai_feedback_production_python
  docker pull ghcr.io/telepace/ai_feedback_production_python
  ```

### 6. Redis

- **描述**: 内存数据结构存储 Redis 的镜像，用于缓存、消息代理和队列。
- **拉取命令**:
  ```bash
  docker pull docker.io/telepace/ai_feedback_production_redis
  docker pull registry.cn-hangzhou.aliyuncs.com/telepace/ai_feedback_production_redis
  docker pull ghcr.io/telepace/ai_feedback_production_redis
  ```

### 7. Traefik

- **描述**: 现代化的反向代理和负载均衡器 Traefik 镜像，支持自动化的服务发现和配置。
- **拉取命令**:
  ```bash
  docker pull docker.io/telepace/ai_feedback_production_traefik
  docker pull registry.cn-hangzhou.aliyuncs.com/telepace/ai_feedback_production_traefik
  docker pull ghcr.io/telepace/ai_feedback_production_traefik
  ```

## 使用指南

1. **选择镜像源**: 根据您的网络环境，选择 Docker Hub、阿里云镜像仓库或 GitHub Container Registry。
2. **拉取镜像**: 使用对应的拉取命令获取所需的应用镜像。
3. **运行容器**: 根据应用需求，使用 `docker run` 或编写 `docker-compose.yml` 文件运行容器。

## 目录结构

本仓库的目录结构如下：

```
infra/
└── compose/
    └── production/
        ├── aws/
        ├── nginx/
        ├── postgres/
        ├── python-3-12-slim-bookworm/
        ├── python/
        ├── redis/
        └── traefik/
```

每个目录包含对应应用的 Dockerfile 和配置文件，您可以根据需要自行构建和定制。


## 许可证

MIT
