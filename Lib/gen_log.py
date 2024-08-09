# gen_log.py
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

from os import system as sys
from datetime import datetime

class _GenLog:
    __BLUE = "\033[1;34m"
    __CYAN = "\033[1;36m"
    __GREEN = "\033[1;32m"
    __RESET = "\033[0m"

    __LOG_PATH = "Log/app.log"
    
    __CALL_COUNT = 0

    def __init__(self) -> None:
        """Generate initial log."""
        print(self.__BLUE, "[" + self.__GREEN + "on" + self.__BLUE + "]",
              self.__CYAN, datetime.now().strftime("%d/%m/%Y %H:%M:%S"), self.__RESET,
              "started, main initiated")
        sys(f"echo [on] {datetime.now().strftime("%d/%m/%Y %H:%M:%S")} started, main initiated > {self.__LOG_PATH}")

    def __format_string(self, info, description) -> None:
        """Format message/log"""
        print(self.__BLUE + "["+ self.__GREEN, info, self.__BLUE + "]" +
              self.__CYAN, datetime.now().strftime("%H:%M:%S"), self.__RESET,
              description)

    def _generate_log(self, level) -> None:
        """Generate log, print on console and create log file."""
        match level:
            case 0:
                self.__format_string("RESET", "repeating")
            
            case 1:
                self.__format_string("info", "sleep initiated and completed successfully, sleep(): 3 minutes")
            
            case 2:
                self.__format_string("info", "mouse moved at predefined position")
        
            case 3:
                self.__format_string("info", "motion initiated")

            case 4:
                self.__CALL_COUNT += 1
                self.__format_string("info", f"motion stopped, completed in 3 sec, count: {self.__CALL_COUNT}")
                sys(f"echo [info] {datetime.now().strftime("%H:%M:%S")} call count: {self.__CALL_COUNT} >> {self.__LOG_PATH}")
            
            case _:
                print("Unknown Level:", level)