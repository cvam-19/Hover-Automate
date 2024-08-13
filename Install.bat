@echo off
cls
color 5

echo ################### Hover: Automate Cursor ###################
echo  _
echo "Move cursor at every 4 minutes of interval"
echo  _
echo *Disclaimer*
echo This software is provided solely for educational purposes.
echo As the developer, I explicitly disclaim any responsibility for any unexpected or adverse effects on your system resulting from its use.
echo While I encourage learning and experimentation, I recommend exercising caution and using this software wisely.
echo Ultimately, you, the user, are entirely responsible for how you utilize this software in any scenario or context.
echo  _
setlocal

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed.
    echo You can download python from: https://www.python.org/downloads/windows/
    echo Installation Failed!!!
    pause
    exit /b 1
)

:: Install virtual environment package
python -m pip install virtualenv
if %errorlevel% neq 0 (
    echo Error occurred while installing virtualenv.
    echo Installation Failed!!!
    pause
    exit /b 1
)

:: Create virtual environment
python -m venv env
if %errorlevel% neq 0 (
    echo Error occurred while creating virtual environment.
    echo To remove virtualenv package:
    echo Exec: "python -m pip uninstall virtualenv"
    echo Installation Failed!!!
    pause
    exit /b 1
)

.\env\Scripts\pip.exe install pyautogui winshell pywin32
if %errorlevel% neq 0 (
    echo Error occurred while installing packages.
    echo Reverting ---
    rmdir /s /q env
    echo env removed.
    echo To remove virtualenv package:
    echo Exec: "python -m pip uninstall virtualenv"
    echo Installation Failed!!!
    pause
    exit /b 1
)

:: Execute install.py
.\env\Scripts\python.exe .\Lib\install.py
if %errorlevel% neq 0 (
    echo Error occurred while running install.py.
    echo Reverting ---
    rmdir /s /q env
    echo env removed.
    echo To remove virtualenv package:
    echo Exec: "python -m pip uninstall virtualenv"
    echo Installation Failed!!!
    pause
    exit /b 1
)

echo All commands executed successfully.
endlocal

echo Installation complete
echo Search for the "Hover" in start menu

pause