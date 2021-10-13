import sys
import ctypes
import requests
import time
from os import system, name
from random import randint
from colorama import Fore
cummands = ['1','2','3','4','clear','cls','logout','exit','quit']

def shitass_clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def shitass_exit():
	sys.exit("   ╠═[X] EXITING > GOODBYE.")

def shitass_main():
	global newprompt
	newprompt = True
	ctypes.windll.kernel32.SetConsoleTitleW(
		f'Shitass Multi Tool | By bong#5107')
	print('')
	print('')
	shitass_clear()
	print(f'''\n



				███████╗██╗  ██╗██╗████████╗ █████╗ ███████╗███████╗
				██╔════╝██║  ██║██║╚══██╔══╝██╔══██╗██╔════╝██╔════╝
				███████╗███████║██║   ██║   ███████║███████╗███████╗
				╚════██║██╔══██║██║   ██║   ██╔══██║╚════██║╚════██║
				███████║██║  ██║██║   ██║   ██║  ██║███████║███████║
				╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝
																													                                               
		═════════════════════════════════════════════════════════════════════════════════════
		 [{Fore.BLUE}1{Fore.RESET}] PORT SCANNER | [{Fore.RED}2{Fore.RESET}] IP/DOMAIN CHECKER | [{Fore.BLUE}3{Fore.RESET}] TOKEN INFO | [{Fore.RED}4{Fore.RESET}] MULTI TOKEN CHECKER
		═════════════════════════════════════════════════════════════════════════════════════''')



def pscan():
	pass

def ip():
	pass

def tokenInfo(token):
	shitass_main()
	headers = {'Authorization': token, 'Content-Type': 'application/json'}
	r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
	if r.status_code == 200:
			userName = r.json()['username'] + '#' + r.json()['discriminator']
			userID = r.json()['id']
			phone = r.json()['phone']
			email = r.json()['email']
			mfa = r.json()['mfa_enabled']
			print(f'''
			[{Fore.BLUE}User Name{Fore.RESET}]       {userName}
			[{Fore.BLUE}User ID{Fore.RESET}]         {userID}
			[{Fore.BLUE}2 Factor{Fore.RESET}]        {mfa}
			[{Fore.BLUE}Email{Fore.RESET}]           {email}
			[{Fore.BLUE}Phone number{Fore.RESET}]    {phone}
			[{Fore.BLUE}Token{Fore.RESET}]           {token}

			''')
	else:
		print(f'{Fore.RED}{token} is invalid{Fore.RESET}')

def tokenCheck():
	shitass_main()
	input(f"[{Fore.GREEN}!{Fore.RESET}] PROGRAM WILL {Fore.RED}BREAK{Fore.RESET} WITHOUT A {Fore.GREEN}TOKENS.TXT{Fore.RESET}")
	checked = []
	with open('tokens.txt', 'r') as f:
		for line in f:
			time.sleep(0)
			token = line.rstrip("\n")
			headers = {
				'Authorization': f'{token}'  
			}
			src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)
			try:
				if src.status_code == 200:
					print(f"[{Fore.GREEN}VALID TOKEN{Fore.RESET}] > " + token)
					checked.append(token)
				else:
					print(f"[{Fore.RED}INVALID TOKEN{Fore.RESET}] > " + token)
			except Exception:
				print (f"TOKEN-CHECKER [{Fore.RED}FAILED{Fore.RESET}] | CHECK INTERNET CONNECTIVITY, OR TRY AGAIN LATER")
	if len(checked) > 0:
		save = input(f'{Fore.GREEN}{len(checked)} VALID TOKENS{Fore.RESET}\nSAVE TOKENS TO FILE? (Y/N)')
		if save == 'y':
			balls = randint(1,999)
			name = f'VALID_TOKENS{balls}'
			with open(f'{name}.txt', 'w') as saveFile:
				saveFile.write('\n'.join(checked))
			print(f'SAVED TOKENS TO {name}')
		


def cmds():
	global newprompt
	if newprompt:
		newprompt = False
		command = input(
			f"   ╔════════════[{Fore.BLUE}<>{Fore.RESET}]\n   ╚═══>{Fore.RED}Shitass{Fore.RESET}@bignuts {Fore.BLUE}-{Fore.RESET} ")
	else:
		command = input(
			f"   ╠════════════[{Fore.BLUE}<>{Fore.RESET}]\n   ╚═══>{Fore.RED}Shitass{Fore.RESET}@bignuts {Fore.BLUE}-{Fore.RESET} ")
	if command not in cummands:
		print(
			f"   ╠═[{Fore.BLUE}X{Fore.RESET}] {Fore.RED}Invalid{Fore.RESET} Option")
		cmds()
	if command == "1":
		pscan()
	elif command == "2":
		ip()
	elif command == "3":
		print(f'[{Fore.BLUE}>{Fore.RESET}] Enter Account token', end=''); token = input('  :  ')
		tokenInfo(token)
	elif command == "4":
		tokenCheck()
	elif command == "clear":
		shitass_main()
	elif command == "cls":
		shitass_main()
	elif command == "exit":
		shitass_exit()
	elif command == "quit":
		shitass_exit()
	elif command == "logout":
		shitass_exit()


shitass_main()
while True:
	try:
		cmds()
	except KeyboardInterrupt:
		pass
		print('')
		
