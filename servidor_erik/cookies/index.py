#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

import codigoHTML as Html
from http import cookies
import os

todasCokis={}
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE']
    listaCoki = listaCoki.split('; ')

    for elemCoki in listaCoki:
        (nombre, valor)=elemCoki.split('=')
        todasCokis[nombre]=valor

coki= cookies.SimpleCookie()

coki["contador"] = 0
coki["eric"] = 0
print(coki)

print("Conten-Type: text/html\n")

##Inicio del codigo HTML
print(Html.cabeceraHtml.format("Cookies","Cookies"))

print(todasCokis)

##Fin codigo HTML
print(Html.finalHtml)