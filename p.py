import requests
import socket
import os
import whois
import urllib.request
from ipdata import ipdata
from pprint import pprint
import sys
import time
import colorama
from colorama import Fore, Back, Style, init
import sys
os.system("clear")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
print(Fore.RED + """
---------------------------------------------

coder by HAWK 
    SİTE VE SUNUCU BİLGİ TOPLAMA ARACI 
    
---------------------------------------------

coder by HAWK 
        1.PORT TARAMA
        
---------------------------------------------

coder by HAWK 
      2.SAYFA KAYNAK KODU ÇEKME

---------------------------------------------

coder by HAWK 
      3.İP TRACER

---------------------------------------------

coder by HAWK 
      4.WHOİS SORGULAMA 

---------------------------------------------


coder by HAWK 
      4.WHOİS SORGULAMA 

---------------------------------------------


coder by HAWK 
      5.SİTE İP ADRESİ GÖRÜNTÜLE 

---------------------------------------------


coder by HAWK 
      6.HEPSİ  

---------------------------------------------

      """)
veri = input(Fore.GREEN + "Islem Numarasini Girin: ")
if (veri == "1" ) :
    host = input( "LÜTFEN İP ADRESİNİ GİRİNİZ : ")
    port = int(input("TARATILACAK PORT ADRESİNİ GİRİNİZ : "))

def portScanner(port):
    if s.connect_ex((host, port)):
        print(Fore.RED + "BU PORT KAPALI")
    else:
        print(Fore.RED + "BU PORT AÇIK")
    portScanner(port)

if (veri == "2" ) :
    
    url = input(Fore.RED + "(example:https://www.google.com)URL : ")
    r = requests.get(url)
    txt = r.text
    print(txt)

if (veri == "3" ) :

    hawk = input("-->>")
    ipdata = ipdata.IPData('test')
    response = ipdata.lookup(hawk)
    pprint(response)

if (veri == "4" ) :
    domain = input("İP VEYA URL : ")
    ss = whois.whois(domain)
    print (ss)
    print("işin bitti sie")

if (veri == "5" ) :
    dom = input("İP VEYA URL  : ")
    print(socket.gethostbyname(dom))

if (veri == "6" ) :
    d3 = input('Enter IP Or Domain +hawk bilgi toplama aracı+: ')
    os.system(" clear ")
    os.system("curl http://api.hackertarget.com/whois/?q=" + veri)
    time.sleep( 5 )
    os.system(" && ")
    os.system("curl http://api.hackertarget.com/dnslookup/?q=" + veri )
    time.sleep( 5 )
    os.system(" && ")
    os.system("curl https://api.hackertarget.com/reversedns/?q=" + veri )
    time.sleep( 5 )
    os.system(" && ")
    os.system("curl http://api.hackertarget.com/geoip/?q=" + veri )
    time.sleep( 5 )
    os.system(" && ")
    os.system("curl http://api.hackertarget.com/nmap/?q=" + veri )
    time.sleep( 5 )
    os.system(" && ")
    p = """----------------------------------------------------

               HAWK BİLGİ TOPLAMA ARACI
        ----------------------------------------------------
                      ^ hawk v3 ^
"""
    print(p)

