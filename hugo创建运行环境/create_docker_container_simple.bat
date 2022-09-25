@echo off
SET dirPath=%~dp0

docker run --name nginx-04 -d -p 80:80 -v %dirPath%:/etc/nginx/conf.d -v %dirPath%public:/var/local -d nginx
