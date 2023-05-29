8.0连接mysql时报错`Public Key Retrieval is not allowed`
![Img](https://raw.githubusercontent.com/liutongke/Image-Hosting/master/images/yank-note-picgo-img-20230529182500.png)

添加以下语句：
```
mysql?allowPublicKeyRetrieval=true
```

![Img](https://raw.githubusercontent.com/liutongke/Image-Hosting/master/images/yank-note-picgo-img-20230529182150.png)