# install.py
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

from datetime import datetime
from os.path import abspath
from os.path import dirname
from os.path import expanduser
from os import system as sys
from create_shortcut import _CreateShortcut

class _Install:
    __USER_PATH = expanduser('~')
    __RELEATIVE_PATH = r"AppData\Roaming\Microsoft\Windows\Start Menu\Programs"
    __ABSOLUTE_PATH = "\\".join([__USER_PATH, __RELEATIVE_PATH])
    __CURRENT_PATH = dirname(abspath(__file__))
    __TARGET_FILE = "\\".join([__CURRENT_PATH, "Hover.bat"])
    __SHORTCUT_FILE = "\\".join([__ABSOLUTE_PATH, "Hover.lnk"])
    __ICON_PATH = "\\".join([__CURRENT_PATH, "..\\Resources\\cursor-hover.256x220.ico"])

    def __init__(self) -> None:
        """Install the program"""
        sys(f"mkdir {self.__CURRENT_PATH}\\Log")
        _CreateShortcut(self.__TARGET_FILE, self.__SHORTCUT_FILE, self.__CURRENT_PATH, self.__ICON_PATH, "Automate cursor")
        self.__gen_installation_log(["__CURRENT_PATH", "__TARGET_FILE", "__SHORTCUT_FILE", "__ICON_PATH",],
                                    [self.__CURRENT_PATH, self.__TARGET_FILE, self.__SHORTCUT_FILE, self.__ICON_PATH])

    def __gen_installation_log(self, str, pth) -> None:
        """Generate installation log."""
        sys(f"echo [{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}] Installation > {self.__CURRENT_PATH}\\Log\\install.log")
        for i in range(len(str)):
            sys(f"echo      {str[i]}: {pth[i]} >> {self.__CURRENT_PATH}\\Log\\install.log")

if __name__ == "__main__":
    _Install()
