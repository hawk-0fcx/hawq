import os
import tkinter as tk
import sys
import time
import json
import subprocess
from requests import get
import sys
print("[+] ----------------HAWK-UNİTY----------------------[+]")
print("[-] Author : HAWK UNİTY ")
print("[-] GİT HUB : https://github.com/hawk-unity ")
print("[-] İNSTAGRAM : https://instagram.com/4zusagawa ")
print("[-] YOU TUBE : Bir Coder ")
print("[+] ----------------HAWK-UNİTY----------------------[+]")
print("[+] ----------------HAWK-UNİTY----------------------[+]")
target= input("[+]Target -> : ")
result = get('http://api.hackertarget.com/nmap/?q=' + target).text
sys.stdout.write(result)
result2 = get('http://api.hackertarget.com/dnslookup/?q=' + target).text
sys.stdout.write(result2)
result3 = get('http://api.hackertarget.com/geoip/?q=' + target).text
sys.stdout.write(result3)
i=tk.Tk()
i.configure(background='black')
i.title("MULTİ TOOL : H4WK OFCX")
greeta = tk.Label(i,text=(result) ,font='Verdana 10', bg="red" , fg="black")
greeta.grid(column=0, row=1)
greeta2 = tk.Label(i,text=(result2) ,font='Verdana 10', bg="white",fg="red")
greeta2.grid(column=0, row=2)
greeta2 = tk.Label(i,text=(result3) ,font='Verdana 10', bg="white",fg="red")
greeta2.grid(column=0, row=3)
i.mainloop()
