@echo off

docker network create lnmp-net

SET dirPath=%~dp0

if not exist "%dirPath%\log\" (
    mkdir "%directory%\log"
    echo "log folder created."
) else (
    echo "log folder already exists."
)

rem docker run --name nginx-php -d -p 80:80 -v %dirPath%nginx:/etc/nginx/conf.d -v %dirPath%log:/var/log/nginx -v %dirPath%:/var/www/html -d nginx

rem docker run --name php8.1 -p 9000:9000 -v %dirPath%:/var/www/html php:8.1.18-fpm

docker run -itd -p 9600:80  --network lnmp-net --network-alias lnmp-net --name nginx-01 --restart always -v %dirPath%nginx:/etc/nginx/conf.d -v %dirPath%log:/var/log/nginx -v %dirPath%:/var/www/html nginx


docker run --name php1 --network lnmp-net --network-alias lnmp-net --restart always -p 9000:9000 -v %dirPath%:/var/www/html -d php:8.1.18-fpm
