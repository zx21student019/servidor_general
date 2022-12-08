#!C:\Users\zx19student398\AppData\Local\Microsoft\WindowsApps\python

import cgi
import datetime
import os
import codigoHtml
from http import cookies

usuarios = {"pepe":["1234","adfhjadg"],"maria":["1111","klsgk"]}

args = cgi.parse()
user = args['usuario'][0]
passwd = args['contra'][0]
estaDentro = False

if user in usuarios:
    if usuarios[user][0]==passwd:
        estaDentro=True

if estaDentro:
    coki = cookies.SimpleCookie()
    coki["SID"]=usuarios[user][1]
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=30) #caduca en 30 dias
    coki['SID']['expires']=expires.strftime("%a,%d %b %Y %H:%M:%S GMT")
    print(coki)

print("Content-type: text/html\n")

print(codigoHtml.cabeceraHTML.format("CNI","Entrada al CNI"))

if estaDentro:
    print("<h6 class='Display-6'>Estas dentro</h6>")
    print("<a href='secretosEstado.py'>Secretos de estado</a><br>")
    print("<a href='secretosEmerito.py'>Secretos del emerito</a>")
    
print(codigoHtml.finalHTML)