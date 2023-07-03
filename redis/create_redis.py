#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
import sys


# 创建目录
def create_directory(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)
        print(f"Created {directory} directory.")
    else:
        print(f"{directory} directory already exists.")


# 判断和创建目录
create_directory("data")
create_directory("log")

# 获取当前脚本所在的目录路径
dir_path = os.path.dirname(os.path.abspath(__file__))

# 构建镜像
subprocess.run(["docker", "build", "-t", "redis:v1", "./"], check=True)

# 定义数据卷映射
data_volume = f"{dir_path}/data:/data"
log_volume = f"{dir_path}/log:/var/log/redis/"

# 运行容器
subprocess_args = [
    "docker", "run", "-d", "--name", "redis-1", "-p", "6379:6379", "--restart", "always",
    "-v", data_volume,
    "-v", log_volume,
    "redis:v1"
]

if sys.platform.startswith('linux'):
    # 在 Linux 环境下执行 sudo chmod a+rw data/ log/
    subprocess.run(["sudo", "chmod", "a+rw", "data/", "log/"], check=True)

subprocess.run(subprocess_args, check=True)
