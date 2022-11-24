#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

import datetime
from http import cookies
import os
import cgi

args = cgi.parse()

texto = args["texto"][0]
print(texto)

cuki = cookies.SimpleCookie()
cuki["empiezaABC"]=texto[0]
expires = datetime.datetime.utcnow() + datetime.timedelta(days=30) #expira en 30 dias
cuki['empiezaABC']['expires'] = expires.strftime("%a, %d %b %Y %H:%m:%S GMT")
print(cuki)

cuki2 = cookies.SimpleCookie()
cuki2["empiezaABC"]=texto[0]
expires = datetime.datetime.utcnow() + datetime.timedelta(days=30) #expira en 30 dias
cuki2['empiezaABC']['expires'] = expires.strftime("%a, %d %b %Y %H:%m:%S GMT")
print(cuki2)