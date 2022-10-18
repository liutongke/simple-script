## （一）PhotoPrism相册共享
[PhotoPrism开发文档](https://docs.photoprism.app/getting-started/docker-compose/#__tabbed_1_4)

```shell
docker-compose.yml
#修改项目文件夹后执行：
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

## （二）jellyfin家庭影院

[jellyfin](https://jellyfin.org/clients/)

`media`视频内容文件夹
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

错误：
**您的数据目录可被其他用户读取
请更改权限为 0770 以避免其他用户查看目录。**
---

nextcloud 您的数据目录可被其他用户读取 请更改权限为 0770 以避免其他用户查看目录**解决方法**http://xieboke.net/article/374/
---
绑定onedrive https://apps.nextcloud.com/apps/files_external_onedrive

## 扫描文件夹手动新增内容：

在`/var/www/html`目录中操作，[参考网址](https://www.coder17.com/posts/nextcloud-auto-scan/)
```shell
su /bin/bash -c "php /var/www/html/occ files:scan --all"
```
![Img](https://raw.githubusercontent.com/lixiaoben123/picgo/master/images/yank-note-picgo-img-20221019022441.png)
