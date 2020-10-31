@echo off

echo Deleting AKL Project from C:\Users\%username%\...
echo.
echo Enter 'Y' when prompted and press enter
echo.

rmdir %USERPROFILE%\AKL /s

echo.
pause