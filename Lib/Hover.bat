@echo off
cls
color 6
echo ################### Hover: Automate Cursor ###################
echo  _
echo "Move cursor at every 4 minutes of interval"
echo  _
echo "Instruction:"
echo * Disable the automatic screen turn off,
echo * Hover and click the cursor on the prefered application after minimising this window,
echo  _
..\env\Scripts\python.exe main.py
