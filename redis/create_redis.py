#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
import sys
import re


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

# 动态输入镜像名称
while True:
    default_image_name = "redis:v1"
    image_name = input(f"Enter image name (default: {default_image_name}): ")
    if not image_name.strip():
        image_name = default_image_name
    if ":" not in image_name:
        image_name += ":latest"
    break

# 构建镜像
subprocess.run(["docker", "build", "-t", image_name, "./"], check=True)

# 动态输入容器名称
while True:
    default_container_name = "redis-1"
    container_name = input(f"Enter container name (default: {default_container_name}): ")
    if not container_name.strip():
        container_name = default_container_name
    break

# 定义数据卷映射
data_volume = os.path.join(dir_path, "data:/data")
log_volume = os.path.join(dir_path, "log:/var/log/redis/")

# 运行容器
subprocess_args = [
    "docker", "run", "-d", "--name", container_name, "-p", "6379:6379", "--restart", "always",
    "-v", data_volume,
    "-v", log_volume,
    image_name
]

if sys.platform.startswith('linux'):
    # 在 Linux 环境下执行 sudo chmod a+rw data/ log/
    subprocess.run(["sudo", "chmod", "a+rw", "data/", "log/"], check=True)

subprocess.run(subprocess_args, check=True)


def run_docker_exec(container_name, command):
    cmd = f"docker exec {container_name} {command}"
    result = subprocess.check_output(cmd, shell=True, text=True)
    return result.strip()


grep_command = 'grep "^requirepass" /usr/local/etc/redis/redis.conf'

output = run_docker_exec(container_name, grep_command)
match = re.search(r"requirepass\s+(.+)", output)
password = match.group(1)
print("Redis登录密码:", password)
