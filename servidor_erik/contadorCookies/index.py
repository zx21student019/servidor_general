#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

import codigoHTML as HTML
from http import cookies
import os

todasCokis={}
if 'HTTP_COOKIE' in os.environ:
    #Pasa de una lista de valores a un array en el que cada valor anterior ocupa una posición
    listaCoki = os.environ['HTTP_COOKIE'] #"contador=0;SID=aniofknek224"
    listaCoki = listaCoki.split('; ') #["contador=0","SID=afafaer342"]

    #Separa los elementos del array y los convierte en un diccionario
    for elemCoki in listaCoki:
        (nombre, valor)=elemCoki.split('=')
        todasCokis[nombre]=valor

    #todasCokis["contador"] = 0
    #todasCokis["SID"] = "ainkfaoiek349"

cuki = cookies.SimpleCookie()

if "contador" in todasCokis:
    cuki["contador"] = int(todasCokis["contador"])+1
else:
    cuki["contador"] = 1

#Esta parte solo se ejecuta la primera vez que accede el usuario
    #cuki["contador"] = 1
    #cuki["otra"] = "hola"
    #cuki["SID"] = "asfnuneaj979ah3ubujd98350"

print(cuki)

print("Conten-Type: text/html\n")
print(HTML.cabeceraHtml.format("Contador de visitas con cookies","Contador de visitas con cookies"))
print(todasCokis)
print(HTML.finalHtml)