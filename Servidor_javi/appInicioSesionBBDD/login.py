#!C:\Users\zx21student030\AppData\Local\Programs\Python\Python310\python.exe

import cgi, os, sys
import json
import codigoHTML
from http import cookies
import datetime
import hashlib
import mysql.connector # type: ignore

args = cgi.parse()

datos = []
existe = False

baseDeDatos = mysql.connector.connect(
     host = 'localhost',
     user = 'appInicioSesion',
     password = '1234',
     database = 'appInicioSesion'
)
cursor = baseDeDatos.cursor()

if "usuario" in args and "passwd" in args:
    datos.append(args["usuario"][0])
    datos.append(args["passwd"][0])

    cursor.execute('SELECT * FROM usuarios')
    consulta = cursor.fetchall()

    for fila in consulta:
        h=hashlib.sha512(str.encode(datos[1]))
        if fila[1] == datos[0] and fila[2] == h.hexdigest():
            existe = True
            break

if existe:
    coki = cookies.SimpleCookie()
    coki["SID"] = datos[0]
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=30)  
    coki['SID']['expires'] = expires.strftime("%a, %d, %b %Y %H :%M :%S GMT")
    print(coki)

    print("Content-Type: text/html\n")

    print(codigoHTML.cabeceraHTML.format("Entraste",'<meta http-equiv="Refresh" content="2; URL=pagina1.py"/>', "Validado con exito. Redirigiendo","",""))
    print(codigoHTML.finalHTML)
        
if not existe:
    print("Content-Type: text/html\n")

    print(codigoHTML.cabeceraHTML.format("Error", '<meta http-equiv="Refresh" content="2; URL=error.html"/>',"Usuario o contrasena no existen. Redirigiendo","",""))
    print(codigoHTML.finalHTML)