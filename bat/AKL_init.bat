@echo off

echo Creating python environments and downloading necessary packages...
echo.
echo Enter password when prompted and press enter
echo Don't worry if nothing appears on the screen while typing. That's the way it works ;)
echo.

python -m venv %USERPROFILE%\AKL
mkdir %USERPROFILE%\AKL\repo
mkdir %USERPROFILE%\AKL\Lib\site-packages\aztool_akl
cd %USERPROFILE%\AKL\repo
git clone git@github.com:kosazna/aztool-akl.git
ROBOCOPY %USERPROFILE%\AKL\repo\aztool-akl\src\ %USERPROFILE%\AKL\Lib\site-packages\aztool_akl /is /it /NJH /NJS /NDL
call %USERPROFILE%\AKL\Scripts\activate.bat
%USERPROFILE%\AKL\Scripts\python.exe -m pip install --upgrade pip
pip install -r %USERPROFILE%\AKL\repo\aztool-akl\requirements.txt
call %USERPROFILE%\AKL\Scripts\deactivate.bat
mkdir %USERPROFILE%\Desktop\AKL_Auto
cd %USERPROFILE%\Desktop\AKL_Auto
md .utilities .history .templates
cd %USERPROFILE%\AKL\repo\aztool-akl\bat
copy *.bat %USERPROFILE%\Desktop\AKL_Auto\.utilities
cd %USERPROFILE%\AKL\repo\aztool-akl\templates
copy *.xlsx %USERPROFILE%\Desktop\AKL_Auto\.templates
copy %USERPROFILE%\AKL\repo\aztool-akl\bat\AKL.bat %USERPROFILE%\Desktop\AKL_Auto\
copy %USERPROFILE%\AKL\repo\aztool-akl\templates\DB_Data.xlsx %USERPROFILE%\Desktop\AKL_Auto\

echo.
pause