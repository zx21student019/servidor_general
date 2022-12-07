#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python
import cgi
from http import cookies 
import os

'''

Hay 2 cookies, empiezaABC y otras. Si la palabra está vacía hay que borrar todas las cookies

empiezaABC -> se concatenan todas las palabras que empiezan por ABC,
            separadas por espacios en blanco.

otras -> se concatenan todas las palabras que NO empiezan por ABC ,
       separadas por espacios en blanco.

'''



#Coger los datos que llegan desde el formulario
form = cgi.FieldStorage()
if "texto" in form:
    palabra = form['texto'].value
else:
    palabra=""

if palabra == "":
    coki = cookies.SimpleCookie()

    coki["empiezaABC"]=""
    coki["otras"]=""
else:
    todasCokis={}
    if'HTTP_COOKIE' in os.environ:
        listaCoki = os.environ['HTTP_COOKIE']
        listaCoki = listaCoki.split('; ') #para que sea correcto puntoycoma con espacio
                                   
        for elemCoki in listaCoki:
            (nombre, valor) = elemCoki.split('=')
            todasCokis[nombre]=valor

    coki = cookies.SimpleCookie()

    abc=" "
    noAbc=" "
    if(palabra[0]=="A" and palabra[1]=="B" and palabra[2]=="C"):
        abc=palabra
    else:
        noAbc=palabra

    if 'empiezaABC' in todasCokis:
        coki['empiezaABC']=todasCokis['empiezaABC'],abc
    else:
        coki['empiezaABC']=abc

    if 'otras' in todasCokis:
        coki['otras']=todasCokis['otras'], noAbc
    else:
        coki['otras']=noAbc

print(coki)

print("Content-Type: text/html\n")

print(todasCokis)

print("correcto")

