# 使用稳定的 Debian 基础镜像
FROM debian:bullseye-slim

# 暴露端口
EXPOSE 1935
EXPOSE 80

# 设置工作目录
WORKDIR /usr/local/src

# 使用 USTC 的软件源
RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list

# 安装必要的工具和依赖
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        unzip \
        wget \
        build-essential \
        libpcre3 \
        libpcre3-dev \
        libssl-dev

# 复制本地的  rtmp 模块压缩文件到容器中，网络允许情况下可以注释该行，使用下面的&& wget https://github.com/arut/nginx-rtmp-module/archive/master.zip \部分网络安装
COPY master.zip /usr/local/src/

# 下载 Nginx 和 rtmp 模块
RUN wget http://nginx.org/download/nginx-1.24.0.tar.gz \
#    && wget https://github.com/arut/nginx-rtmp-module/archive/master.zip \
    && tar -zxvf nginx-1.24.0.tar.gz \
    && unzip master.zip

# 编译和安装 Nginx，同时启用 SSL 和 rtmp 模块
WORKDIR /usr/local/src/nginx-1.24.0
RUN ./configure \
    --without-http_gzip_module \
    --with-http_ssl_module \
    --add-module=/usr/local/src/nginx-rtmp-module-master \
    && make \
    && make install

# 切换到 Nginx 的 sbin 目录，运行 Nginx
WORKDIR /usr/local/nginx/sbin
CMD ["./nginx", "-g", "daemon off;"]
