php:8.1.18-fpm-bullseye nginx:1.25.0-bullseye环境，nginx为配置文件，暂时测试phalapi、laravel配置文件，执行`create_docker_container_nginx.bat`
脚本直接创建镜像、创建容器，完成后将nginx目录中配置文件复制进conf.d目录中，修改配置文件的相应的目录，如若想添加PHP拓展修改`Dockerfile`文件即可。

测试访问地址`http://192.168.0.105/App/Site/Index`