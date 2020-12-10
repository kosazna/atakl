@echo off

echo Updating AKL Library...
echo.
echo Enter password when prompted and press enter
echo Don't worry if nothing appears on the screen while typing. That's the way it works ;)
echo.

cd %USERPROFILE%\AKL\repo\atakl
git pull git@github.com:kosazna/atakl.git

call %USERPROFILE%\AKL\Scripts\activate.bat
pip install -r %USERPROFILE%\AKL\repo\atakl\requirements.txt
call %USERPROFILE%\AKL\Scripts\deactivate.bat

ROBOCOPY %USERPROFILE%\AKL\repo\atakl %USERPROFILE%\AKL\Lib\site-packages\atakl /MIR /NJH /NJS /NDL
ROBOCOPY %USERPROFILE%\AKL\repo\atakl\resources\bat %USERPROFILE%\Desktop\AKL_Auto\.utilities /MIR /NJH /NJS /NDL
ROBOCOPY %USERPROFILE%\AKL\repo\atakl\resources\templates %USERPROFILE%\Desktop\AKL_Auto\.templates /MIR /NJH /NJS /NDL
ROBOCOPY %USERPROFILE%\AKL\repo\atakl\resources\bat %USERPROFILE%\Desktop\AKL_Auto "AKL GUI.bat" /E /IS /IT /NJH /NJS /NDL

echo.
echo.
pause