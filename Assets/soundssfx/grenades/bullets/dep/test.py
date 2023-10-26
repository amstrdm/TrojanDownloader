import subprocess
import os 

username = os.path.expanduser('~')
"""
os.system(r'''
Powershell -Command "& { Start-Process \"notepad.exe\"
 -ArgumentList @(\"C:\\Windows\\System32\\drivers\\etc\\hosts\")
 -Verb RunAs } " ''')
"""
print(r'Powershell -Command "& { Start-Process "'+ username + r'\chrome.exe" -Verb RunAs } " ')