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
        print(f"Created {directory} directory.")
    else:
        print(f"{directory} directory already exists.")


def check_network_exists(network_name):
    """
    检查指定名称的网络是否存在
    """
    try:
        result = subprocess.run(["docker", "network", "inspect", network_name], capture_output=True, text=True)
        if result.returncode == 0:
            return True
    except Exception as e:
        pass
    return False


# 定义 lnmp-net 网络名称
network_name = "lnmp-net"

# 检查网络是否存在，不存在则创建
if not check_network_exists(network_name):
    subprocess.run(["docker", "network", "create", "lnmp-net"], check=True)
    print("Created lnmp-net network.")
else:
    print("lnmp-net network already exists.")

# 构建镜像
subprocess.run(["docker", "build", "-t", "nginx/rtmp:v1", "."], check=True)

# 获取当前脚本所在的目录路径
dir_path = os.path.dirname(os.path.abspath(__file__))

# 创建日志目录
log_dir = os.path.join(dir_path, "log")
create_directory(log_dir)

# 定义容器运行参数
docker_args = [
    "docker", "run", "-itd", "-p", "9999:80", "-p", "9998:1935",
    "--network", "lnmp-net", "--network-alias", "lnmp-net",
    "--name", "nginx-rtmp-1", "--restart", "always",
    "-v", f"{dir_path}/conf/nginx.conf:/usr/local/nginx/conf/nginx.conf",
    "-v", f"{log_dir}:/usr/local/nginx/logs",
    "-v", f"{dir_path}:/var/www/html",
    "nginx/rtmp:v1"
]

# 运行容器
subprocess.run(docker_args, check=True)
