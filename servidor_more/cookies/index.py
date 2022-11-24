#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

import os
import codigoHTML
from http import cookies

todasCokis={}
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE']
    listaCoki = listaCoki.split('; ')

    for elemCoki in listaCoki:
        (nombre, valor ) = elemCoki.split('=')
        todasCokis[nombre]=valor

coki = cookies.SimpleCookie()
coki["contador"]=0
coki["nombre"]="yomismoconmimecanismo"
print(coki)

print("Content-type: text/html\n")

print(todasCokis)

print(codigoHTML.finalHtml)