@echo off

call conda activate atakl_dev
call pyuic5 -x aztool_akl_gui.ui -o ..\designer.py