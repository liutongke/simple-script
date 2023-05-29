FROM redis:6.2.12-bullseye

WORKDIR /var/tmp

RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
#设置时区
ENV TZ=Asia/Shanghai
RUN apt-get update
RUN apt-get install wget pwgen -y
RUN wget http://download.redis.io/releases/redis-6.2.12.tar.gz

RUN tar -zxvf redis-6.2.12.tar.gz
# 在构建过程中生成随机字符串
RUN random_pass=$(pwgen 16 1) \
    # 替换字段
    && sed -i "s/# requirepass foobared/requirepass $random_pass/" /var/tmp/redis-6.2.12/redis.conf \
    && sed -i 's/^bind 127.0.0.1 -::1/# bind 127.0.0.1 -::1/' /var/tmp/redis-6.2.12/redis.conf \
    && sed -i 's/^protected-mode yes/protected-mode no/' /var/tmp/redis-6.2.12/redis.conf
# 将修改后的配置文件复制到目标位置
RUN mkdir -p /usr/local/etc/redis
RUN cp /var/tmp/redis-6.2.12/redis.conf /usr/local/etc/redis/redis.conf
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]