#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

import codigoHTML
import os
from http import cookies

print("Conten-Type: text/html\n")

usuarios = {"pepe":["1234","aaaa"],"maria":["0000","bbbb"]}
estaDentro = False

todasCookies = {}
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE']
    listaCoki = listaCoki.split('; ')

    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCookies[nombre] = valor

usuario=""
if 'SID' in todasCookies:
    for user,datos in usuarios.items():
        if(datos[1] == todasCookies[nombre]):
            usuario = user
            estaDentro=True

if estaDentro:
    print(codigoHTML.cabeceraHtml.format('FBI',"",'Area 51'))
    print('<h3 class="Display-3">Bienvenido, agente '+usuario+'</h3>')
    print('<a href="login.py">Volver</a><br>')
    print(codigoHTML.finalHtml)
else:
    print(codigoHTML.redireccionIndex())