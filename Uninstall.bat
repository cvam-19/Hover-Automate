@echo off
cls
color 5

echo ################### Hover: Automate Cursor ###################

.\env\Scripts\python.exe .\Lib\uninstall.py
rmdir /s /q env
rmdir /s /q Lib\__pycache__
echo Uninstallation complete

pause