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
import hashlib
os.system("clear")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
print(Fore.RED + """
---------------------------------------------
      1.PORT TARAMA
---------------------------------------------
      2.SAYFA KAYNAK KODU ÇEKME
---------------------------------------------
      3.İP TRACER
---------------------------------------------
      4.WHOİS SORGULAMA
---------------------------------------------
      5.SİTE İP ADRESİ GÖRÜNTÜLE
---------------------------------------------
      6.SHA512 ŞİFRELEME
---------------------------------------------
      7.MD5 ŞİFRELEME
---------------------------------------------
      8.SQLMAP VERİTABANI ÇEKME
---------------------------------------------
      9.Bilgi toplama
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
    m=hashlib.sha512()
    sha512 = input("STRİNG : ")
    m.update(sha512.encode('utf-8'))
    print(m.hexdigest())
if (veri== "7" ) :
    sifreleyici = hashlib.md5()
    metin = input("lütfen Hashlenecek metini giriniz: ")
    sifreleyici.update(metin.encode("utf-8"))
    hash = sifreleyici.hexdigest()
    print("Çıktı>>> %s" % hash)
if (veri== "8" ) :
     açık = input("Açığı olan site : ")
     os.system("sqlmap -u"+açık+" --dbs --random-agent")
if (veri== "9") :
    d3 = input('Enter IP Or Domain +hawk bilgi toplama aracı+: ')
    os.system(" clear ")
    os.system("curl http://api.hackertarget.com/whois/?q=" + d3 )
    time.sleep( 5 )
    os.system(" && ")
    os.system("curl http://api.hackertarget.com/dnslookup/?q=" + d3 )
    time.sleep( 5 )
    os.system(" && ")
    os.system("curl https://api.hackertarget.com/reversedns/?q=" + d3 )
    time.sleep( 5 )
    os.system(" && ")
    os.system("curl http://api.hackertarget.com/geoip/?q=" + d3 )
    time.sleep( 5 )
    os.system(" && ")
    os.system("curl http://api.hackertarget.com/nmap/?q=" + d3 )
    time.sleep( 5 )
