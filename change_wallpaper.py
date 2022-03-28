# Download and change wallpaper (Windows 10)
import os
import time
import HID
from HID import CODE

if __name__ == '__main__':
    HID.press(bytes([CODE.LEFT_CTRL, 0, CODE.ESC, *[0] * 5]))
    time.sleep(0.1)
    # open web browser with this URL
    cmd = 'chrome http://images.hdqwalls.com/download/hacker-8k-8p-2560x1440.jpg'
    HID.type_string(cmd)
    time.sleep(0.5)
    HID.press(bytes([*[0] * 2, CODE.ENTER, *[0] * 5]))
    time.sleep(2)
    HID.press(bytes([CODE.LEFT_CTRL, 0, CODE.KEY_S, *[0] * 5]))
    time.sleep(1)
    ## save location
    HID.press(bytes([*[0] * 2, CODE.ENTER, *[0] * 5]))
    time.sleep(0.5)

    # TAB to move focus to Show all Downloads (Chrome)
    HID.press(bytes([*[0] * 2, CODE.TAB, *[0] * 5]))
    time.sleep(0.2)
    HID.press(bytes([*[0] * 2, CODE.ENTER, *[0] * 5]))
    time.sleep(1.0)
    # press tab 11 times to move 
    for _ in range(11):
        HID.press(bytes([*[0] * 2, CODE.TAB, *[0] * 5]))
    time.sleep(0.2)
    # open the settings to set to wallpaper
    HID.press(bytes([*[0] * 2, CODE.ENTER, *[0] * 5]))

    ## press down 6 times
    for _ in range(6):
        HID.press(bytes([*[0] * 2, CODE.KEY_DOWN, *[0] * 5]))
        time.sleep(0.1)
    time.sleep(0.5)
    HID.press(bytes([*[0] * 2, CODE.ENTER, *[0] * 5]))
    time.sleep(0.5)
    HID.press(bytes([*[0] * 2, CODE.KEY_DOWN, *[0] * 5]))
    time.sleep(0.5)
    HID.press(bytes([*[0] * 2, CODE.ENTER, *[0] * 5]))
    time.sleep(0.5)
    # close 2 windows
    for _ in range(2):
        HID.press(bytes([CODE.LEFT_ALT, 0, CODE.F4, *[0] * 5]))
        time.sleep(1.0)
