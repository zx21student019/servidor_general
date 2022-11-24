#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

import codigoHTML
import os
from http import cookies

print("Conten-Type: text/html\n")

usuarios = {"pepe":["1234","aaaa"],"maria":["0000","bbbb"]}
estaDentro = False

todasCookies = {}
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE'] #"SID=aaaa"
    listaCoki = listaCoki.split('; ') #["SID=aaaa"]

    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCookies[nombre] = valor

        #todasCookies["SID"] = "aaaa"

usuario = "nadie"

if 'SID' in todasCookies:
    for user,datos in usuarios.items(): #en user="pepe" en datos=["1234","aaaa"]
        if(datos[1] == todasCookies[nombre]):
            usuario = user
            estaDentro=True

if estaDentro:
    print(codigoHTML.cabeceraHtml.format('FBI',"",'Secretos de Obama'))
    print('<h3 class="Display-3">Bienvenido, agente '+usuario+'</h3>')
    print('<a href="login.py">Volver</a><br>')
    print('<a href="logout.py">Salir</a><br>')
    print(codigoHTML.finalHtml)
else:
    codigoHTML.redireccionIndex()