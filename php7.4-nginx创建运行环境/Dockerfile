FROM php:7.4.30-fpm

EXPOSE 9000

RUN apt-get update \
    && apt-get install autoconf \
	&& set -ex \
    && pecl update-channels \
    && pecl install redis-stable \
    && docker-php-ext-enable redis \
    && docker-php-ext-install mysqli pdo_mysql \
    && php -r "copy('https://install.phpcomposer.com/installer', 'composer-setup.php');" \
    && php composer-setup.php \
    && php -r "unlink('composer-setup.php');"

#COPY / /var/www

#WORKDIR /var/www

#CMD ["php","./apiswoole.php"]

#docker build -t apiswoole:v1 ./