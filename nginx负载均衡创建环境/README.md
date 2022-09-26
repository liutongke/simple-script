直接运行`nginx-load-balancing.bat`脚本创建nginx负载均衡器，`nginx`目录为配置文件。
**注：nginx配置文件需要配置应用服务器地址**
```shell
 upstream backend-server {
        server 192.168.0.105:9500;
        server 192.168.0.105:9600;
    }
```