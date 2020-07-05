import requests
import Proxy_INFO_module as ProxyIN

UrlList = {
    'VK': 'https://vk.com',
    'GOOGLE': 'https://google.com',
    'YANDEX': 'https://yandex.ru',
    'STEAM': 'https://store.steampowered.com',
    'AVITO': 'https://avito.ru',
    'OLX': 'https://olx.ua',
    'GMAIL': 'https://gmail.com/',
    'MAIL.RU': 'https://mail.ru',
    'YOUTUBE': 'https://youtube.com',
    'SPEEDTEST': 'https://speedtest.net',
    'INSTAGRAM': 'https://instagram.com',
    'QIWI': 'https://qiwi.com',
    'USER': ''
}

proxies = {
    'http': '193.113.207.105:5836',
    'https': '93.113.207.105:5836'
}

UrlSelectList = ['VK', 'GOOGLE', 'YANDEX', 'STEAM', 'AVITO', 'OLX', 'GMAIL', 'MAIL.RU', 'YOUTUBE', 'SPEEDTEST', 'INSTAGRAM', 'QIWI']

def ClearScreen():
    print('\n'*300)


def PrintLogo():
	print('''

 (                                                
 )\ )                          (           *   )  
(()/((          ) (            )\ )   (  ` )  /(  
 /(_))(   (  ( /( )\ )   ___  (()/(   )\  ( )(_)) 
(_))(()\  )\ )\()(()/(  |___|  /(_))_((_)(_(_())  
| _ \((_)((_((_)\ )(_))       (_)) __| __|_   _|  
|  _| '_/ _ \ \ /| || |         | (_ | _|  | |    
|_| |_| \___/_\_\ \_, |          \___|___| |_|    
                  |__/                          
						

			(c) by dendi developer

''')

def FunctionCheckProxy(UrlAgr):
	
	if WebService == 14:
		ProxyFileGood = open('ProxyGood/' + 'Your URL.txt', 'tw')
	else:
		ProxyFileGood = open('ProxyGood/' + UrlAgr + '.txt', 'tw')
	
	print('[*]', UrlAgr)
	for Proxy in ProxyList:
		try:
			Response = requests.get(UrlList[UrlAgr], proxies=proxies)
			if Response.status_code == requests.codes['ok']:
				print('[Good!] ',proxies['https'])
				ProxyFileGood.write(Proxy + '\n')
		except:
			print('[Bad!] ', proxies['https'])

		proxies['https'] = Proxy
	ProxyFileGood.close()	

def MainMenu():
	print('[1] Check Proxy')
	print('[2] Info Proxy')
	print('[3] Speed Test\n')
	print('[0] Exit')
	Answer = input('$>> ')
	if Answer == '1':
		ProxyCheck()
	elif Answer == '2':
		ProxyIN.InfoProxy()
	elif Answer == '3':
		pass
	elif Answer == '0':
		exit()
 
def ProxyCheck():
	global ProxyList
	global WebService

	ClearScreen()
	PrintLogo()
	ProxyFileInput = input('Proxy File Name (.txt): ')
	ProxyFile = open(ProxyFileInput, 'r')
	ProxyFile = ProxyFile.read()
	ProxyList = ProxyFile.split('\n')
	ClearScreen()
	PrintLogo()
	print('''
[1] VK
[2] GOOGLE
[3] YANDEX
[4] STEAM
[5] AVITO
[6] OLX
[7] GMAIL
[8] MAIL.RU
[9] YOUTUBE
[10] SPEEDTEST
[11] INSTAGRAM
[12] QIWI

[13] ALL SERVICE
[14] YOUR URL
	''')
	WebService = int(input('Please, select web-site: '))
	if WebService < 13:
		FunctionCheckProxy(UrlSelectList[WebService - 1])
	elif WebService == 13:
		for Url in UrlList.keys():
			FunctionCheckProxy(Url)
	elif WebService == 14:
		InputWebService = input('Your url (https://google.com): ')
		UrlList['USER'] = InputWebService
		FunctionCheckProxy('USER')

while True:
	ClearScreen()
	PrintLogo()
	MainMenu()

