#!/bin/bash
#备份保存路径  
backup_dir=/root/mysqlbackup  
#日期  
dd=`date +%Y%m%d`  
#备份工具  
tool=/usr/local/mysql/bin/mysqldump
#ip地址
host=rm-bp106650287ubona63o.mysql.rds.aliyuncs.com  
#用户名  
username=rilianapp  
#密码  
password=RilianApp1154
#将要备份的数据库  
database_name=db_yuelian 
  
#简单写法  mysqldump -u root -p123456 users > /root/mysqlbackup/users-$filename.dump  
$tool -h $host -u $username -p$password $database_name > $backup_dir/$database_name-$dd.sql
