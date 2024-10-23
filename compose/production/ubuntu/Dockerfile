# Production Stage
FROM ubuntu:22.04

LABEL maintainer="3293172751ns@gmail.com" \
      org.opencontainers.image.source=https://github.com/telepace/infra \
      org.opencontainers.image.description="Telepace Base Images" \
      org.opencontainers.image.licenses="MIT"

ARG GO111MODULE=on
ARG GOPROXY=https://goproxy.cn,direct

# Set environment variables
ENV GO111MODULE=$GO111MODULE \
    GOPROXY=$GOPROXY \
    TELEPACE_WORKDIR=/telepace \
    TELEPACE_APP=/telepace/app

# Telepace Config Should pass the path
ENV TELEPACE_APP_CONFIG_NAME=$TELEPACE_APP/config \
    TELEPACE_APP_CMDDIR=$TELEPACE_APP/scripts \
    TELEPACE_APP_LOGDIR=$TELEPACE_APP/logs \
    TELEPACE_APP_BINDIR=$TELEPACE_APP/_output/bin

WORKDIR /telepace

# Install required packages
RUN apt-get update && \
    apt-get install -y tzdata ca-certificates iproute2 lsof psmisc dnsutils && \
    ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    dpkg-reconfigure --frontend noninteractive tzdata && \
    echo "telepace" > /etc/hostname && \
    for dir in "$TELEPACE_APP"; do \
      for subdir in logs _output/bin scripts deployments config; do \
        mkdir -p "$dir/$subdir"; \
      done; \
    done && \
    mkdir -p /telepace/tools

COPY ./README.md ./LICENSE ./
COPY get_os.sh get_arch.sh source.sh /telepace/tools/

RUN /telepace/tools/get_os.sh > ~/os && \
    /telepace/tools/get_arch.sh > ~/arch && \
    echo "export OS=$(cat ~/os)" >> /etc/profile && \
    echo "export ARCH=$(cat ~/arch)" >> /etc/profile && \
    chmod +x /telepace/tools/*.sh && \
    cp /telepace/tools/get_os.sh /usr/local/bin/get_os && \
    cp /telepace/tools/get_arch.sh /usr/local/bin/get_arch

# Set directory to map logs, config files, scripts, and SDK
VOLUME ["/telepace", \
        "/telepace/app/logs", "/telepace/app/config", "/telepace/app/scripts", "/telepace/app/_output/bin"]

WORKDIR /telepace

ONBUILD RUN OS=$(get_os) && \
            ARCH=$(get_arch)
