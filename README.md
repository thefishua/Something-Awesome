# Something-Awesome
## The Project
This project represents 30+ hours of work in creating a rubber ducky that performs both a changing of a person's wallpaper and a reverse shell that occurs at 1pm daily for a windows device. During this project I learned a lot about microcontrollers, using raspberrypi's as tools for both malicious and ethical activity and some reflection on how I could've made the project even better. Below I talk about how to install the raspberry pi OS and an overview of a HID device, The changing of a wallpaper script, reverse shells and a final reflection on the project. 

## Installing Raspberry Pi Zero OS and What is a HID Device [12 hours]
Blog:https://www.openlearning.com/u/joshuafish-r7ahqh/blog/AchievingAndBricking0/
Blog:https://www.openlearning.com/u/joshuafish-r7ahqh/blog/HidPacketTranslation/
Summary:
- Download raspberry pi imager from the raspberry pi website 
- Write to an SD card the specific OS for the machine recommend Raspbian 
- Update modules and drivers in config.txt and etc/modules on the raspberrypi
- Use a configuration file to enable the raspberry pi to be ion gadget mode
- During this process you may come across a coloured screen when starting up the raspberry pi. If this occurs like it did for me you have bricked the system and must restart the process of installing the OS.
- In the blog there is a simple script called example.py and to run:
```
? sudo python3 example.py
```
- HID packets are the size of a byte and must be created in a certain syntax for the computer to understand the key injection
## Changing a Wallpaper [4 hours]
Blog:https://www.openlearning.com/u/joshuafish-r7ahqh/blog/KeyLoggingInAction/
Summary:
- In the project there is a script called change_wallpaper.py
- Have the raspberrypi plugged into the target computer
- To run the script on the attacker screen
```
$ ssh pi@raspberry
$ cd SomethingAwesome
$ sudo python3 change_wallpaper
```
- This will change the wallpaper to a certain hacker
- During this process there was trouble with the key injection tool failing to pick up commands as the script was going too fast. To solve this using the python time library to slow down the script
- Also to fix buggyness had to make sure that all keys registered especially when messing with windows GUI
- Lastly the script is just a show-case of the raspberrypi rubber ducky working and that I had successful figured out the process
## Reverse Shells [16 hours]
Blog:https://www.openlearning.com/u/joshuafish-r7ahqh/blog/ReverseShell/
Summary:
- Reverse Shells is where the user initiates a remote shell connection and the target system listens for such connection
- For this part the goal was to not use administrative access and also to bypass the windows defender and any antivirus software that was on the target computer
- For this too work I had problems with one liner reverse shells that I had created as they would be picked up by the windows defender and be denied
- To solve this issue I then created a powershell script that allocated memory to a byte array that would be used to create commands in the reverse shell
- Then I created a while loop that would then send the commands through the IEX function to the target computer
- To get around antivirus software I put the script on my github page under reverse.ps1 and then in the reverse_shell.py attack it would download the file and run it
- Also the file is run every day at 1pm enabling a attacker the option of stacking out there target at certain times without the need for the target to physically plug the usb in every time
- However, there is still current issues such as a forensics team could easily see that there is a random script downloaded on the target computer and if they stop the script at the right time they can track it back to my github
## Reflection 
Future Projects that were Missed
- Near the end of the project I had planned to make a 3D model for the rubber ducky, but ran out of time. This would make the rubber ducky look less suspicious and also more incognito. To do this I would've used fusion360 and a 3D printer to create the design. 
- Other tools that I wanted to create was a keylogger that would make a file in the rubber ducky that would then get sent to a google drive. For this I would just need the rubber ducky to check what keys had been pressed and output that to a file. This file would then be uploaded. 
- The other tool that could be create is a screen recorder that could record the screen of the target

Stuff that went Wrong
- During the project alot of stuff went wrong that enabled myself to learn. This included bricking the system, debugging the rubber ducky and loss of connection. For next time I would've just changed my goal of bypassing antivirus software to just launching the powershell in admin mode. This would've then allowed for more time for the other tools/projects I had for the something awesome. 


