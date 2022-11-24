#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

from http.cookiejar import Cookie
import codigoHTML
import os
from http import cookies

print("content-Type: text/html\n")

usuarios = {"pepe":["1234","asdf1234"],"maria":["1111","oinionh32145"]}
estaDentro = False

todasCookies={}
if 'HTTP_COOKIE' in os.environ:
    listaCookies = os.environ['HTTP_COOKIE']
    listaCookies = listaCookies.split('; ')

    for elemCookies in listaCookies:
        (nombre,valor) = elemCookies.split('=')
        todasCookies[nombre]=valor

if 'SID' in todasCookies:
    estasDentro=True

if estaDentro:
    print(codigoHTML.cabeceraHTML.format("Riot","Entrada a Rito"))
    print("<a href='login.py'>regresar</a></br>")
    print(codigoHTML.finalHTML)
