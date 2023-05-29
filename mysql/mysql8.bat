@echo off
set "dir_path=mysql"  REM 替换为目标目录的路径

if not exist "%dir_path%" (
    mkdir "%dir_path%"
    echo "Create mysql directory successfully"
)

setlocal EnableDelayedExpansion

set "characters=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
set "length=16"
set "password="

for /l %%i in (1,1,%length%) do (
    set /a "random_index=!random! %% 80"
    for %%j in (!random_index!) do set "char=!characters:~%%j,1!"
    set "password=!password!!char!"
)

set "current_dir=%CD%"
echo current directory path: %current_dir%

docker run --name mysql-v1 -p 3306:3306 --restart always -v %current_dir%/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=%password% -d mysql:8.0
echo %current_dir%mysql
echo MySQL password: %password%
rem 暂时不退出
pause