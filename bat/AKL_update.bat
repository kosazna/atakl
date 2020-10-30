@echo off

echo Updating AKL Library...
echo.
echo Enter password when prompted and press enter
echo Don't worry if nothing appears on the screen while typing. That's the way it works ;)
echo.

cd %USERPROFILE%\AKL\repo\aztool-akl
git pull git@github.com:kosazna/aztool-akl.git
pip install -r %USERPROFILE%\AKL\repo\aztool-akl\requirements.txt
xcopy %USERPROFILE%\AKL\repo\aztool-akl\src %USERPROFILE%\AKL\Lib\site-packages\aztool_akl /h /i /c /k /e /r /y
xcopy %USERPROFILE%\AKL\repo\aztool-akl\bat %USERPROFILE%\Desktop\AKL_Auto\.utilities /h /i /c /k /e /r /y
xcopy %USERPROFILE%\AKL\repo\aztool-akl\templates %USERPROFILE%\Desktop\AKL_Auto\.templates /h /i /c /k /e /r /y
copy %USERPROFILE%\AKL\repo\aztool-akl\bat\AKL.bat %USERPROFILE%\Desktop\AKL_Auto\

echo.
echo.
pause