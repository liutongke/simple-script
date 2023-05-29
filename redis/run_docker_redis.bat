docker build -t redis-v1 ./

SET dirPath=%~dp0

docker run -d --name redis-1 -p 6379:6379 -v %dirPath%/data:/data redis-v1
::https://segmentfault.com/a/1190000039769819