@echo off

docker build -t php-7.4-fpm ./

SET dirPath=%~dp0

docker run --name nginx-php -d -p 80:80 -v %dirPath%nginx:/etc/nginx/conf.d -v %dirPath%:/var/local -d nginx

docker run --name php7.4 -p 9000:9000 -v %dirPath%:/var/local php-7.4-fpm
