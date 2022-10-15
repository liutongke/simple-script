#!/bin/bash
count=`ps -fe |grep "Swoole.php" | grep -v "grep" | wc -l`

if [ $count -lt 1 ]; then
        nohup /usr/local/php/bin/php /usr/local/nginx/html/Swoole.php &
fi

