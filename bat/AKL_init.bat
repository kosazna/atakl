@echo off

echo Creating python environments and downloading necessary packages...
echo.
echo Enter password when prompted and press enter
echo Don't worry if nothing appears on the screen while typing. That's the way it works ;)
echo.

python -m venv C:\Users\%username%\AKL
cd C:\Users\%username%\AKL\Lib\site-packages
git clone git@github.com:kosazna/aztool-akl.git
call C:\Users\%username%\AKL\Scripts\activate.bat
C:\Users\%username%\AKL\Scripts\python.exe -m pip install --upgrade pip
pip install -r C:\Users\aznavouridis.k\AKL\Lib\site-packages\aztool-akl\requirements.txt
call C:\Users\%username%\AKL\Scripts\deactivate.bat

echo.
pause