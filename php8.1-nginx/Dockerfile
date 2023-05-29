FROM php:8.1.18-fpm

# 安装 Redis 扩展
RUN pecl install redis && docker-php-ext-enable redis \
    && docker-php-ext-install mysqli pdo_mysql

# 设置工作目录
WORKDIR /var/www/html

# 暴露端口
EXPOSE 9000

# 启动 PHP-FPM
CMD ["php-fpm"]
