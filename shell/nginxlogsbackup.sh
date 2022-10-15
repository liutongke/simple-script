#!/bin/bash
# nginx日志备份
#设置日志文件存放目录
LOG_HOME="/root/nginxbackup"

#备分文件名称
LOG_PATH_BAK="$(date -d yesterday +%Y%m%d%H%M)".access.log

#重命名日志文件
mv /usr/local/nginx/logs/access.log ${LOG_HOME}/${LOG_PATH_BAK}

#向nginx主进程发信号重新打开日志 
kill -USR1 `cat /usr/local/nginx/logs/nginx.pid`
