<?php
$redisIp = '';
$redisPwd = '';
$redis = new Redis();
$redis->connect($redisIp, 6379); //连接Redis
$redis->auth($redisPwd); //密码验证
$redis->select(0);//选择数据库,int类型，一般是0-16，选一个
$redis->set("testKey", "Hello Redis"); //设置测试key
echo $redis->get("testKey");//输出value

echo "----";
$servername = '';
$username = "root";
$password = "";
$dbname = "sys";

// 创建连接
$conn = new mysqli($servername, $username, $password, $dbname);

// 检查连接是否成功
if ($conn->connect_error) {
    die("Mysql连接失败: " . $conn->connect_error);
}

echo "Mysql连接成功！";
// 关闭连接
$conn->close();