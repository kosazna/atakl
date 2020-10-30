@echo off

echo Updating AKL Library...
echo.
echo Enter password when prompted and press enter
echo Don't worry if nothing appears on the screen while typing. That's the way it works ;)
echo.

cd %USERPROFILE%\AKL\Lib\site-packages\aztool-akl
git pull git@github.com:kosazna/aztool-akl.git
pip install -r %USERPROFILE%\AKL\Lib\site-packages\aztool-akl\requirements.txt
cd %USERPROFILE%\AKL\Lib\site-packages\aztool-akl\bat
copy *.bat %USERPROFILE%\Desktop\AKL_Auto\.utilities
cd %USERPROFILE%\AKL\Lib\site-packages\aztool-akl\templates
copy *.xlsx %USERPROFILE%\Desktop\AKL_Auto\.templates
copy %USERPROFILE%\AKL\Lib\site-packages\aztool-akl\bat\AKL.bat %USERPROFILE%\Desktop\AKL_Auto\

echo.
echo.
pause