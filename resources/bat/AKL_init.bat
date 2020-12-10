@echo off

echo Creating python environments and downloading necessary packages...
echo.
echo Enter password when prompted and press enter
echo Don't worry if nothing appears on the screen while typing. That's the way it works ;)
echo.

python -m venv %USERPROFILE%\AKL
mkdir %USERPROFILE%\AKL\repo
cd %USERPROFILE%\AKL\repo
git clone git@github.com:kosazna/atakl.git

call %USERPROFILE%\AKL\Scripts\activate.bat
%USERPROFILE%\AKL\Scripts\python.exe -m pip install --upgrade pip
pip install -r %USERPROFILE%\AKL\repo\atakl\requirements.txt
call %USERPROFILE%\AKL\Scripts\deactivate.bat

mkdir %USERPROFILE%\Desktop\AKL_Auto\.history
ROBOCOPY %USERPROFILE%\AKL\repo\atakl %USERPROFILE%\AKL\Lib\site-packages\atakl /MIR /NJH /NJS /NDL
ROBOCOPY %USERPROFILE%\AKL\repo\atakl\resources\bat %USERPROFILE%\Desktop\AKL_Auto\.utilities /MIR /NJH /NJS /NDL
ROBOCOPY %USERPROFILE%\AKL\repo\atakl\resources\templates %USERPROFILE%\Desktop\AKL_Auto\.templates /MIR /NJH /NJS /NDL
ROBOCOPY %USERPROFILE%\AKL\repo\atakl\resources\bat %USERPROFILE%\Desktop\AKL_Auto "AKL GUI.bat" /E /IS /IT /NJH /NJS /NDL

ROBOCOPY %USERPROFILE%\AKL\repo\atakl\resources\templates %USERPROFILE%\Desktop\AKL_Auto\DB_Data "Concepts.xlsx" "PT Beverages - Lavazza.xlsx" "PT Beverages - Spirits.xlsx" /E /IS /IT /NJH /NJS /NDL


echo.
pause