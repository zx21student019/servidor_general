#!C:\Users\zx21student030\AppData\Local\Programs\Python\Python310\python.exe

import codigoHTML,os,sys
from http import cookies
import json
import mysql.connector # type: ignore

estasDentro=False

todasCokis={} 
if'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE'] 
    listaCoki = listaCoki.split(';')
                                
    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCokis[nombre]=valor

coki = cookies.SimpleCookie()

baseDeDatos = mysql.connector.connect(
     host = 'localhost',
     user = 'appInicioSesion',
     password = '1234',
     database = 'appInicioSesion'
)
cursor = baseDeDatos.cursor()

if 'SID' in todasCokis:
    cursor.execute('SELECT * FROM usuarios')
    consulta = cursor.fetchall()
    for fila in consulta:
        if(fila[1]==todasCokis['SID']):
            estasDentro=True
            
if estasDentro:
    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Pagina 1","","Pagina 1",
                                         '<form action="pagina2.py" method="get"><button type="submit" class="btn btn-primary">Pagina 2</button></form>',
                                         '<form action="logout.py" method="get"><button type="submit" class="btn btn-primary">Log out</button></form>',"",""))
    print(codigoHTML.finalHTML)
else:
    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Error", '<meta http-equiv="Refresh" content="2; URL=error.html"/>',
              "No hay cookie","",""))
    print(codigoHTML.finalHTML)