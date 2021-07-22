# 使用官方 Golang 镜像作为构建环境
FROM golang:1.15-buster as builder
WORKDIR /home
# 安装依赖
COPY go.* ./
RUN go env -w GO111MODULE=on
RUN go env -w GOPROXY=https://goproxy.cn,direct
# 将代码文件写入镜像
COPY . /home
#更新mod所有依赖包
RUN go mod download
# 构建二进制文件
RUN go build -mod=readonly -v -o server
# 使用裁剪后的官方 Debian 镜像作为基础镜像
# https://hub.docker.com/_/debian
# https://docs.docker.com/develop/develop-images/multistage-build/#use-multi-stage-builds
FROM debian:buster-slim
RUN set -x && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
  ca-certificates && \
  rm -rf /var/lib/apt/lists/*
COPY . /home
#COPY /runtime /app/server
# 将构建好的二进制文件拷贝进镜像
COPY --from=builder /home/server /home/server
# 启动 Web 服务
WORKDIR /home
CMD ["server"]
#docker build -t go-db:v1 .