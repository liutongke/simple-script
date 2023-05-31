FROM php:8.1.18-fpm
#FROM php:7.4-fpm-bullseye
WORKDIR /var/www/html

RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y zip unzip
# 安装 Redis 扩展
RUN pecl install redis && docker-php-ext-enable redis \
    && docker-php-ext-install mysqli pdo_mysql

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# 可选：设置 Composer 的全局配置
# 阿里镜像安装composer缺少依赖
#RUN composer config --global repo.packagist composer https://mirrors.aliyun.com/composer/
RUN composer config -g repos.packagist composer https://mirrors.tencent.com/composer/
# 设置工作目录
WORKDIR /var/www/html

# 暴露端口
EXPOSE 9000

# 启动 PHP-FPM
CMD ["php-fpm"]
