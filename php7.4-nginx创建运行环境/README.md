php7.4-fpm nginx12.1环境，nginx为配置文件，暂时测试phalapi框架正常运行，执行`create_docker_container_nginx.bat`
脚本直接创建镜像、创建容器，完成后可直接访问，如若想添加PHP拓展修改`Dockerfile`文件即可。

测试访问地址`http://192.168.0.105/App/Site/Index`

&emsp;&emsp;**特别注意：PHP和nginx映射的本地和容器文件夹需要一致**或者在增加如下代码

```shell
    location ~ \.php$ {
        root /var/www/html/public/;#增加PHP服务器的目录
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        fastcgi_pass 192.168.0.105:9000;
        fastcgi_index index.php;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    }
```