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


def check_network_exists(network_name):
    """
    检查网络是否存在
    """
    result = subprocess.run(["docker", "network", "ls", "--format", "{{.Name}}"], capture_output=True, text=True)
    return network_name in result.stdout.splitlines()


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

# 检查 lnmp-net 网络是否存在
network_name = "lnmp-net"
if not check_network_exists(network_name):
    subprocess.run(["docker", "network", "create", network_name], check=True)
else:
    print("Network", network_name, "already exists.")

# 运行 nginx 容器
subprocess.run(["docker", "run", "--name", "nginx-cow", "-itd", "nginx:1.25.0-bullseye"], check=True)

# 从容器中复制配置文件到本地
subprocess.run(["docker", "cp", "nginx-cow:/etc/nginx/conf.d/default.conf", f"{confd_dir}"], check=True)

# 停止并删除 nginx 容器
subprocess.run(["docker", "stop", "nginx-cow"], check=True)
subprocess.run(["docker", "rm", "nginx-cow"], check=True)

# 运行 laravel-nginx-01 容器
subprocess.run(
    [
        "docker", "run", "-itd", "-p", "9600:80", "--network", network_name, "--network-alias", "lnmp-net",
        "--name", "laravel-nginx-01", "--restart", "always", "-v", f"{confd_dir}:/etc/nginx/conf.d",
        "-v", f"{log_dir}:/var/log/nginx", "-v", f"{current_dir}:/var/www/html", "nginx:1.25.0-bullseye"
    ],
    check=True
)

# 运行 laravel-php-01 容器
subprocess.run(
    [
        "docker", "run", "--name", "laravel-php-01", "--network", network_name, "--network-alias", "lnmp-net",
        "--restart", "always", "-p", "9601:9000", "-v", f"{current_dir}:/var/www/html", "-d",
        "php:8.1.18-fpm-custom"
    ],
    check=True
)
