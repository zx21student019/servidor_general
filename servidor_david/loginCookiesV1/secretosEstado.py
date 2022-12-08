#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

from http import cookies
from operator import truediv
import codigoHtml
import os

print("Content-Type: text/html\n")

todasCokis={} #diccionario vacio
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE'] #"SID=ASDFasdf344"
    listaCoki = listaCoki.split('; ') #["SID=ASDFasdf344"]

    for elemCoki in listaCoki:
        (nombre,valor )=elemCoki.split('=')
        todasCokis[nombre]=valor

        #todasCokis["SID"]="ASDFasdf344"

coki = cookies.SimpleCookie

if 'SID' in todasCokis:
    estaDentro=True

if estaDentro:
   print(codigoHtml.cabeceraHtml.format("CNI","Secretos del emerito"))
   print("<a href='login.py'>Volver</a><br>")
   print(codigoHtml.finalHtml)
else :
    print(codigoHtml.cabeceraHtml.format("CNI","Error en el acceso"))
    print("<a href='login.py'>pagina de acceso</a><br>")
    print(codigoHtml.finalHtml)
