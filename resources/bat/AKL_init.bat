@echo off

echo Creating python environments and downloading necessary packages...
echo.
echo Enter password when prompted and press enter
echo Don't worry if nothing appears on the screen while typing. That's the way it works ;)
echo.

python -m venv %USERPROFILE%\AKL
mkdir %USERPROFILE%\AKL\repo
cd %USERPROFILE%\AKL\repo
git clone git@github.com:kosazna/aztool-akl.git

call %USERPROFILE%\AKL\Scripts\activate.bat
%USERPROFILE%\AKL\Scripts\python.exe -m pip install --upgrade pip
pip install -r %USERPROFILE%\AKL\repo\aztool-akl\requirements.txt
call %USERPROFILE%\AKL\Scripts\deactivate.bat

mkdir %USERPROFILE%\Desktop\AKL_Auto\.history
ROBOCOPY %USERPROFILE%\AKL\repo\aztool-akl\aztool_akl %USERPROFILE%\AKL\Lib\site-packages\aztool_akl /MIR /NJH /NJS /NDL
ROBOCOPY %USERPROFILE%\AKL\repo\aztool-akl\resources\bat %USERPROFILE%\Desktop\AKL_Auto\.utilities /MIR /NJH /NJS /NDL
ROBOCOPY %USERPROFILE%\AKL\repo\aztool-akl\resources\templates %USERPROFILE%\Desktop\AKL_Auto\.templates /MIR /NJH /NJS /NDL
ROBOCOPY %USERPROFILE%\AKL\repo\aztool-akl\resources\bat %USERPROFILE%\Desktop\AKL_Auto AKL.bat /E /IS /IT /NJH /NJS /NDL

ROBOCOPY %USERPROFILE%\AKL\repo\aztool-akl\resources\templates %USERPROFILE%\Desktop\AKL_Auto\DB_Data "DB_Concepts.xlsx" "DB_PT Beverages-Lavazza.xlsx" "DB_PT Beverages-Spirits.xlsx" /E /IS /IT /NJH /NJS /NDL


echo.
pause