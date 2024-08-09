# main.py
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

from time import sleep
import pyautogui as pg
from gen_log import _GenLog

SCREEN_SIZE = pg.size()
SCREEN_HEIGHT = SCREEN_SIZE.height
SCREEN_WIDTH = SCREEN_SIZE.width

# Time in seconds
SLEEP_TIME = 240

if __name__ == "__main__":
    gen_log = _GenLog()

    while True:
        sleep(SLEEP_TIME)
        gen_log._generate_log(1)
        pg.moveTo(SCREEN_HEIGHT/5, SCREEN_WIDTH/5, duration = 1)
        gen_log._generate_log(2)
        gen_log._generate_log(3)
        for _ in range(3):
            pg.moveRel(-50, 50, duration = 0.5)
            pg.moveRel(50, -50, duration = 0.5)
        gen_log._generate_log(4)
        gen_log._generate_log(0)