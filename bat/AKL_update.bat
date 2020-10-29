@echo off

echo Updating AKL Library...
echo.
echo Enter password when prompted and press enter
echo Don't worry if nothing appears on the screen while typing. That's the way it works ;)
echo.

cd C:\Users\%username%\AKL\Lib\site-packages\aztool-akl
git pull git@github.com:kosazna/aztool-akl.git

echo.
echo.
pause