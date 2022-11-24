#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

import cgi
import codigoHTML
import os
import datetime
from http import cookies

usuarios = {"pepe":["1234","asdf1234"],"maria":["1111","oinionh32145"]}

args = cgi.parse()
user = args['usuario'][0]
password = args ['pass'][0]
estaDentro = False

if user in usuarios:
    if usuarios [user][0] == password:
        estaDentro=True

if estaDentro:
    cookies = cookies.SimpleCookie()
    cookies["SID"]=usuarios[user][1]
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=30)
    cookies['SID']['expires'] = expires.strftime("%a, %d %b %Y: %H:%M:%S GMT")
    print(cookies)

print("content-Type: text/html\n")

print(codigoHTML.cabeceraHTML.format("Riot","Entrada a Rito"))

if estaDentro:
    print("<h6 class=''Display-6>Estas dentro</h6>")
    print("<a href='secretosRito.py'>Secretos de Rito</a></br>")
    print("<a href='sectaDeYummi.py'>Secta de yummi</a>")

else:
    print(codigoHTML.redireccion.format("loginCookies.html"))

print(codigoHTML.finalHTML)