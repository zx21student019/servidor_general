#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

import codigoHtml
import os   
from http import cookies


todasCokis = {}
if 'HTTP_COOKIE' in os.environ :
    listaCoki = os.environ ['HTTP_COOKIE']
    listaCoki = listaCoki.split ('; ')
    for elemCoki in listaCoki :
        ( nombre , valor ) = elemCoki.split ('=')
        todasCokis [nombre] = valor


coki = cookies.SimpleCookie()
coki["contador"]=1
coki["nombre"]="david"
print(coki)

print("Content-Type: text/html\n")

print(codigoHtml.cabeceraHtml.format("Cookies","Cookies"))

print(todasCokis)

for x in listaCoki:
    if "contador" in str(x):
        print("si")

for x in valor:
 print(x)

print('<br><a href="index.py">enlace</a>')

print(codigoHtml.finalHtml)
