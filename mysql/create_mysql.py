#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import random
import string
import subprocess
from datetime import date

today = date.today()
date_str = today.strftime("%Y-%m-%d")
dir_path = f"mysql-{date_str}"  # 根据当天日期生成目录路径

os.makedirs(dir_path, exist_ok=True)
print("Create mysql directory successfully")

characters = string.ascii_letters + string.digits
length = 16
password = "".join(random.choice(characters) for _ in range(length))

current_dir = os.path.join(os.getcwd(), dir_path)
print("Current directory path:", current_dir)

port = 3306  # 设置端口变量

docker_name = "mysql-1"  # 设置容器名称

mysql_version = input("Enter MySQL version (5.7 or 8.0): ")
if mysql_version == "5.7":
    image_name = "mysql:5.7"
elif mysql_version == "8.0":
    image_name = "mysql:8.0"
else:
    print("Invalid MySQL version. Using default version (mysql:8.0).")
    image_name = "mysql:8.0"

subprocess.run(
    [
        "docker",
        "run",
        "--name",
        docker_name,
        "-p",
        f"{port}:3306",  # 使用端口变量
        "--restart",
        "always",
        "-v",
        f"{current_dir}:/var/lib/mysql",
        "-e",
        f"MYSQL_ROOT_PASSWORD={password}",
        "-d",
        image_name,
    ],
    check=True,
)

print(current_dir)
print("MySQL password:", password)
input("Press Enter to exit...")
