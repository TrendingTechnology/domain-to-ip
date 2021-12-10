#python3.10.0
import sys
import time
from colorama import init, Fore
from socket import gethostbyname

init()
red = Fore.RED
green = Fore.GREEN
cyan = Fore.CYAN
orange = Fore.YELLOW
off = Fore.RESET

banner = (f"""{green}  _  _____ _  _____  
 {green}| |/ /_ _| |/ / _ \  {off}Domain To Ip
 {green}| ' < | || ' < (_) | {off}Author : u53rrss
 {green}|_|\_\___|_|\_\___/  {off}List without http/s
""")
print(banner)
try:
  site = input('[?] Domain List > ')
  output = input('[?] Save As e.g ip.txt > ')
  print('') #cumabuatspasi:p
  utama = open(site,'r').read().splitlines()
  for website in utama:
    try:
          ress = gethostbyname(website)
          print(f'{green}[OK]{off} {website} : {ress}')
          save = open(output, 'a').write(ress + "\n")
    except:
         print(f'{red}[ERROR]{off} {website} : Error Domain')
  print(f'\n{red}[!] {off}Finished - File : {output}')
except:
  print(f'{red}[!] {off}WRONG INPUT {red}[!]{off}')
  time.sleep(1)
  sys.exit()