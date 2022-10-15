#!/bin/bash
#备份保存路径  
backup_dir=/root/mysqlbackup  
#日期  
dd=`date +%Y%m%d`  
#备份工具  
tool=/usr/local/mysql/bin/mysqldump
#ip地址
host=rm-uf6ds902a0jw1h755o.mysql.rds.aliyuncs.com  
#用户名  
username=root  
#密码  
password=Jiqifanyu2017
#将要备份的数据库  
database_name=db_dj  
  
#简单写法  mysqldump -u root -p123456 users > /root/mysqlbackup/users-$filename.dump  
$tool -h $host -u $username -p$password $database_name > $backup_dir/$database_name-$dd.sql
