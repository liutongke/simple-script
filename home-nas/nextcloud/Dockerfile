FROM nextcloud:latest

RUN apt-get update \
    && apt-get install -y cron \
    && apt-get install -y vim \
    && service cron start

#COPY / /var/www

#WORKDIR /var/www

#CMD ["php","./apiswoole.php"]

#docker build -t apiswoole:v1 ./