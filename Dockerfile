FROM debian:buster-slim
RUN set -x && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
  ca-certificates && \
  rm -rf /var/lib/apt/lists/*
# 将构建好的二进制文件拷贝进镜像
COPY /server /app/server
# 启动 Web 服务
CMD ["/app/server"]