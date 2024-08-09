# uninstall.py
"""
August 8, 2024
@Author: Shivam Shukla
@Description: This package facilitates the execution or invocation of the application

This code is provided solely for educational purposes.
As the developer, I explicitly disclaim any responsibility for any unexpected or adverse effects on your system resulting from its use.
While I encourage learning and experimentation, I recommend exercising caution and using this code wisely.
Ultimately, you, the user, are entirely responsible for how you utilize this code in any scenario or context.

The code is unencumbered by copyright; feel free to share, modify, or adapt it as you see fit.
"""

from os.path import dirname
from os.path import abspath
from os.path import expanduser
from os import remove as rmfile
from os import system as sys
import shutil

class _Uninstall:
    
    __USER_PATH = expanduser('~')
    __RELEATIVE_PATH = r"AppData\Roaming\Microsoft\Windows\Start Menu\Programs"
    __ABSOLUTE_PATH = "\\".join([__USER_PATH, __RELEATIVE_PATH])
    __SHORTCUT_FILE = "\\".join([__ABSOLUTE_PATH, "Hover.lnk"])
    __CURRENT_PATH = dirname(abspath(__file__))
    
    def __init__(self) -> None:
        """Uninstall the program"""
        shutil.rmtree(f"{self.__CURRENT_PATH}\\Log")
        rmfile(self.__SHORTCUT_FILE)

if __name__ == "__main__":
    _Uninstall()