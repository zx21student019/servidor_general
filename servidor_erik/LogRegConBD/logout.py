#!C:\Users\zx21student301\AppData\Local\Microsoft\WindowsApps\python

from http import cookies
import os
import datetime
import codigoHTML as HTML

todasCookies = {}
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE']
    listaCoki = listaCoki.split('; ')

    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCookies[nombre] = valor

if 'SID' in todasCookies:
    cuki = cookies.SimpleCookie()
    cuki["SID"]=todasCookies["SID"]
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=-1) #envia cookie caducada
    cuki['SID']['expires'] = expires.strftime("%a, %d %b %Y %H:%m:%S GMT")
    print(cuki)

print("Conten-Type: text/html\n")

HTML.redireccionLogout()