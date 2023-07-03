#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess

# 创建网络
subprocess.run(["docker", "network", "create", "lnmp-net"], check=True)

# 构建镜像
subprocess.run(["docker", "build", "-t", "nginx/rtmp:v1", "."], check=True)

# 获取当前脚本所在的目录路径
dir_path = os.path.dirname(os.path.abspath(__file__))

# 创建日志目录
log_dir = os.path.join(dir_path, "log")
if not os.path.exists(log_dir):
    os.mkdir(log_dir)
    print("log folder created.")
else:
    print("log folder already exists.")

# 定义容器运行参数
docker_args = [
    "docker", "run", "-itd", "-p", "9999:80", "-p", "9998:1935",
    "--network", "lnmp-net", "--network-alias", "lnmp-net",
    "--name", "nginx-rtmp-1", "--restart", "always",
    "-v", f"{dir_path}/conf/nginx.conf:/usr/local/nginx/conf/nginx.conf",
    "-v", f"{dir_path}/log:/usr/local/nginx/logs",
    "-v", f"{dir_path}:/var/www/html",
    "nginx/rtmp:v1"
]

# 运行容器
subprocess.run(docker_args, check=True)
