#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

import codigoHTML
import os
from http import cookies

todasCookies={}
if 'HTTP_COOKIE' in os.environ:
    listaCookies = os.environ['HTTP_COOKIE']
    listaCookies = listaCookies.split(';' )

    for elemCokies in listaCookies:
        (nombre, valor ) = elemCokies.split('=')
        todasCookies[nombre] = valor

#esta solo se ejecuta la primera vez que accede el usuario
coki = cookies.SimpleCookie()

if 'contador' in todasCookies:
    coki["contenedor"]=int(todasCookies["contador"])+1
else:
    coki["contador"]=1

print(coki)

print("content-type: text/html\n")

print(codigoHTML.cabeceraHTML.format("titulo", "esto es un h3"))
print(todasCookies)
print(codigoHTML.finalHTML)