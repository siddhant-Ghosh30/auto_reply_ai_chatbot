# this is to find cursor location of stuff on my system

import pyautogui

while True:
    a = pyautogui.position()
    print(a)
    # 581, 1161 (app location)
    # 836, 221 to 1791, 991 (copy drag)
    # random click to un-copy 858, 716
    # text box = 1212, 1084