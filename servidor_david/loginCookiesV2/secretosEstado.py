#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

from http import cookies
import codigoHTML
import os


print("Content-Type: text/html\n")

usuarios = {"pepe":["1234","adfhjadg"],"maria":["1111","klsgk"]}
estasDentro = False


todasCokis={} #diccionario vacio
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE'] #"SID=ASDFasdf344"
    listaCoki = listaCoki.split('; ') #["SID=ASDFasdf344"]

    for elemCoki in listaCoki:
        (nombre,valor )=elemCoki.split('=')
        todasCokis[nombre]=valor

        #todasCokis["SID"]="ASDFasdf344"

agente = ""

if 'SID' in todasCokis:
    for agen,datos in usuarios.items():
        if(datos[1] == todasCokis[nombre]):
            estasDentro = True
            agente=agen

coki = cookies.SimpleCookie

if 'SID' in todasCokis:
    estasDentro=True

if estasDentro:
   print(codigoHTML.cabeceraHTML.format("CNI","Secretos del emerito"))
   print("<h3 class='Display-3'>Bienvenido, agente "+agente+"</h3>")
   print("<a href='logout.py'>Ir al logout</a>")
   print("<a href='login.py'>Volver</a><br>")
   print(codigoHTML.finalHTML)
else:
   print(codigoHTML.redireccionError.format("index.html"))
    

