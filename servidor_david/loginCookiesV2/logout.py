#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

import os, datetime, codigoHTML
from http import cookies

todasCokis={} #diccionario vacio
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE'] #"SID=ASDFasdf344"
    listaCoki = listaCoki.split('; ') #["SID=ASDFasdf344"]

    for elemCoki in listaCoki:
        (nombre,valor )=elemCoki.split('=')
        todasCokis[nombre]=valor

        #todasCokis["SID"]="ASDFasdf344"


if 'SID' in todasCokis:
    coki = cookies.SimpleCookie()
    coki["SID"]=todasCokis["SID"]
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=30) #caduca en 30 dias
    coki['SID']['expires']=expires.strftime("%a,%d %b %Y %H:%M:%S GMT")
    print(coki)

print("Content-Type: text/html\n")

print(codigoHTML.cabeceraHTML.format("CNI","Saliste del sistema"))
print("<a href='index.html'>pagina de acceso</a><br>")
print(codigoHTML.finalHTML)
