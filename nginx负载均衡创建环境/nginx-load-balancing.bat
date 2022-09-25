@echo off

SET dirPath=%~dp0

docker run --name nginx-load-balancing -d -p 80:80 -v %dirPath%nginx:/etc/nginx -d nginx
