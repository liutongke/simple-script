@echo off
setlocal EnableDelayedExpansion

set "characters=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%%^&*()-_=+"
set "length=16"
set "password="

for /l %%i in (1,1,%length%) do (
    set /a "random_index=!random! %% 80"
    for %%j in (!random_index!) do set "char=!characters:~%%j,1!"
    set "password=!password!!char!"
)

docker run --name mysql-v1 -p 3306:3306 -v C:\Users\keke\dev\docker\MySQL\data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=%password% -d mysql:5.7

echo MySQL password: %password%
pause