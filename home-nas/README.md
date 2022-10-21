## （一）PhotoPrism相册共享
[PhotoPrism开发文档](https://docs.photoprism.app/getting-started/docker-compose/#__tabbed_1_4)

```shell
#修改项目文件夹
docker-compose.yml
docker-compose up -d
```
创建成功后需要初始化密码
```shell
PHOTOPRISM_ADMIN_PASSWORDdocker-compose exec photoprism photoprism passwd
```
密码设置成功后重启
```
docker-compose stop
docker-compose up -d
```
**archive 存档：** 存档里面的照片才可以删除，且存档里的文件不显示在其他的地方
**approve 批准：** 照片不在存档中可以在其它显示，想删除照片需先移动到存档中
**注意：** <u>设置中可以设置显示存档照片</u>

## （二）jellyfin媒体系统

[jellyfin客户端](https://jellyfin.org/clients/)
`media`视频内容文件夹

### [影视内容命名规范](https://jellyfin.org/docs/general/server/media/movies/)
```
Film (2010) [imdbid-tt0106145]Film (2018) [tmdbid-65567]

影片名+空格+（年份）+为了更好的识别可以把元数据id加上
```
[tmdb搜刮官网](https://www.themoviedb.org/search/movie?query=%E9%B9%BF%E9%BC%8E%E8%AE%B0)，名称可以去这里直接参考。


### 中文字幕不显示或乱码问题
https://post.smzdm.com/p/a5dro4d3/

**解决方案：**
安装Open Subtitles插件->[外挂字幕网](https://assrt.net/sub/?searchword=%E7%81%B0%E7%8C%8E%E7%8A%AC%E5%8F%B7)下载字幕->上传srt字幕

![Img](https://raw.githubusercontent.com/lixiaoben123/picgo/master/images/yank-note-picgo-img-20221021121725.png)

[字幕网站推荐：](https://www.jihosoft.cn/zimu/subtitles/subtitle-download-sites/)：
1. [字幕库](https://zimuku.org/)
1. [伪射手](http://assrt.net/)
1. [A4k字幕网](https://www.a4k.net/)

### 解决元数据削刮媒体信息失败问题

修改hots，[查询网址ip：](https://ipaddress.com/website/api.tmdb.org)
```
api.themoviedb.org
api.themoviedb.org
```
Dockerfile示例(**--add-host=**)：
```shell
docker run \
    -v /mydata/jellyfin:/config \
    -v /mydata/video:/media \
    -p 8096:8096 -p 8920:8920 \
    --name=jellyfin \
    --add-host=api.themoviedb.org:52.85.151.18 \
    --add-host=api.Tmdb.org:18.160.37.15 \
    --restart always \
    --device=/dev/dri:/dev/dri \
    jellyfin/jellyfin:latest
```

docker-compose示例(**extra_hosts:**)：
```shell
version: '3.1'
services:
  jellyfin:
    image: jellyfin/jellyfin:latest
    container_name: jellyfin
    #类似 Docker 中的 --add-host 参数 ，https://ipaddress.com/website/api.tmdb.org
    extra_hosts:
      - "api.themoviedb.org:52.85.151.18"
      - "api.themoviedb.org:52.85.151.24"
      - "api.themoviedb.org:52.85.151.28"
      - "api.themoviedb.org:52.85.151.48"
      - "api.Tmdb.org:18.160.37.15"
      - "api.Tmdb.org:18.160.37.20"
      - "api.Tmdb.org:18.160.37.47"
      - "api.Tmdb.org:18.160.37.81"
    environment:
      - TZ=Asia/Shanghai
    volumes:
      - ./jellyfin/config:/config
      - ./jellyfin/cache:/cache
      - ./jellyfin/media:/media
    ports:
      - 8096:8096
      - 8920:8920
      - 7359:7359/udp
      - 1900:1900/udp
    restart: always
```

## （三）多设备同步
[syncthing](https://syncthing.net/downloads/)

## （四）Nextcloud网盘

- [Nextcloud私人云盘安装配置](https://www.zywvvd.com/notes/environment/nas/nextcloud/nextcloud/)
- [Nextcloud外挂磁盘](https://www.zywvvd.com/notes/environment/nas/nextcloud/nextcloud-add-disk/)
- [Nextcloud服务端文档](https://docs.nextcloud.com/server/latest/admin_manual/file_workflows/access_control.html)

安装
```shell
docker run -it -d --name nextcloud --privileged=true -p 8080:80 -v C:\Users\keke\dev\docker\nextcloud:/var/www/html/data --restart=always nextcloud
```
选项含义：

<table>
<thead>
<tr>
<th>参数</th>
<th>含义</th>
</tr>
</thead>
<tbody>
<tr>
<td>-it</td>
<td>将容器的 Shell 映射到当前的 Shell，然后你在本机窗口输入的命令，就会传入容器</td>
</tr>
<tr>
<td>-d</td>
<td>后台运行</td>
</tr>
<tr>
<td>–name</td>
<td>容器名称</td>
</tr>
<tr>
<td>-p</td>
<td>端口映射</td>
</tr>
<tr>
<td>-v</td>
<td>宿主机路径映射</td>
</tr>
<tr>
<td>–restart=always</td>
<td>开机自动启动</td>
</tr>
<tr>
<td>–privileged=true</td>
<td>允许docker拥有宿主机root权限，可以执行mount等命令</td>
</tr>
</tbody>
</table>

错误提示：**nextcloud 您的数据目录可被其他用户读取 请更改权限为 0770 以避免其他用户查看目录**

解决方法：
config.php 添加
```php
'check_data_directory_permissions' => false
```

绑定onedrive https://apps.nextcloud.com/apps/files_external_onedrive

## 手动扫描文件夹新增内容：

在`/var/www/html`目录中操作，[参考网址](https://www.coder17.com/posts/nextcloud-auto-scan/)
```shell
su /bin/bash -c "php /var/www/html/occ files:scan --all"
```
![Img](https://raw.githubusercontent.com/lixiaoben123/picgo/master/images/yank-note-picgo-img-20221019022441.png)

**流程图插件名称:Draw.io**