#!/bin/bash
ID=`ps -ef | grep "Redisswoole.php" | grep -v "grep" | awk '{print $2}'`
echo $ID  
echo "---------------"  
for id in $ID
do
kill -9 $id
echo "killed $id"  
done
echo "---------------"
count=`ps -fe |grep "server.php" | grep -v "grep" | grep "master" | wc -l`
