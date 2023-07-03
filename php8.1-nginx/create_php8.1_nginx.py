#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess


def create_directory(directory):
    """
    检查目录是否存在，如果不存在则创建目录
    """
    if not os.path.exists(directory):
        os.mkdir(directory)
        print("Created", directory, "directory in", current_dir)
    else:
        print(directory, "directory already exists in", current_dir)


# 获取当前目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 创建 conf.d 目录
confd_dir = os.path.join(current_dir, "conf.d")
create_directory(confd_dir)

# 创建 log 目录
log_dir = os.path.join(current_dir, "log")
create_directory(log_dir)

# 构建 PHP 镜像
subprocess.run(["docker", "build", "-t", "php:8.1.18-fpm-custom", "."], check=True)

# 创建网络
subprocess.run(["docker", "network", "create", "lnmp-net"], check=True)

# 运行 nginx 容器
subprocess.run(["docker", "run", "--name", "nginx-cow", "-itd", "nginx:1.25.0-bullseye"], check=True)

# 从容器中复制配置文件到本地
subprocess.run(["docker", "cp", "nginx-cow:/etc/nginx/conf.d/default.conf", f"{confd_dir}"], check=True)

# 停止并删除 nginx 容器
subprocess.run(["docker", "stop", "nginx-cow"], check=True)
subprocess.run(["docker", "rm", "nginx-cow"], check=True)

# 运行 laravle-nginx-01 容器
subprocess.run(
    [
        "docker", "run", "-itd", "-p", "9600:80", "--network", "lnmp-net", "--network-alias", "lnmp-net",
        "--name", "laravle-nginx-01", "--restart", "always", "-v", f"{confd_dir}:/etc/nginx/conf.d",
        "-v", f"{log_dir}:/var/log/nginx", "-v", f"{current_dir}:/var/www/html", "nginx:1.25.0-bullseye"
    ],
    check=True
)

# 运行 laravle-php-01 容器
subprocess.run(
    [
        "docker", "run", "--name", "laravle-php-01", "--network", "lnmp-net", "--network-alias", "lnmp-net",
        "--restart", "always", "-p", "9601:9000", "-v", f"{current_dir}:/var/www/html", "-d",
        "php:8.1.18-fpm-custom"
    ],
    check=True
)
