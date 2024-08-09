# create_shortcut.py
"""
August 8, 2024
@Author: Shivam Shukla
@Description: The package includes classes dedicated to log generation 

This code is provided solely for educational purposes.
As the developer, I explicitly disclaim any responsibility for any unexpected or adverse effects on your system resulting from its use.
While I encourage learning and experimentation, I recommend exercising caution and using this code wisely.
Ultimately, you, the user, are entirely responsible for how you utilize this code in any scenario or context.

The code is unencumbered by copyright regarding the imported entities, they might have their own individual copyright regulations;
feel free to share, modify, or adapt it as you see fit.
"""

#import pip
#pip.main(["install", "winshell"])
#pip.main(["install", "pywin32"])
#import winshell
from win32com.client import Dispatch

class _CreateShortcut:
    def __init__(self, target_path, shortcut_path, start_in_path, icon_path, description="") -> None:
        """"create shortcut and place it to the prefered location"""
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.TargetPath = target_path
        shortcut.WorkingDirectory = start_in_path
        shortcut.Description = description
        shortcut.IconLocation = icon_path
        shortcut.save()
