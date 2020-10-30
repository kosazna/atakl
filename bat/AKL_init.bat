@echo off

echo Creating python environments and downloading necessary packages...
echo.
echo Enter password when prompted and press enter
echo Don't worry if nothing appears on the screen while typing. That's the way it works ;)
echo.

python -m venv %USERPROFILE%\AKL
cd %USERPROFILE%\AKL\Lib\site-packages
git clone git@github.com:kosazna/aztool-akl.git
call %USERPROFILE%\AKL\Scripts\activate.bat
%USERPROFILE%\AKL\Scripts\python.exe -m pip install --upgrade pip
pip install -r %USERPROFILE%\AKL\Lib\site-packages\aztool-akl\requirements.txt
call %USERPROFILE%\AKL\Scripts\deactivate.bat
mkdir %USERPROFILE%\Desktop\AKL_Auto
cd %USERPROFILE%\Desktop\AKL_Auto
md .utilities .history .templates
cd %USERPROFILE%\AKL\Lib\site-packages\aztool-akl\bat
copy *.bat %USERPROFILE%\Desktop\AKL_Auto\.utilities

echo.
pause