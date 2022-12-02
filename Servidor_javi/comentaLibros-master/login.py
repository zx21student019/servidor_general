#!C:\Users\zx21student030\AppData\Local\Programs\Python\Python310\python.exe

import os
import cgi
import codigoHTML
from http import cookies
import datetime
import hashlib
from baseDeDatos import cursor
from registrarTimestamp import registrarTiempo

args = cgi.parse()

datos = []
existe = False

if "usuario" in args and "passwd" in args:
    datos.append(args["usuario"][0])
    datos.append(args["passwd"][0])

    cursor.execute('SELECT * FROM usuarios')
    consulta = cursor.fetchall()

    for fila in consulta:
        h=hashlib.sha512(str.encode(datos[1]))
        if fila[1] == datos[0] and fila[2] == h.hexdigest():
            existe = True
            id = fila[0]
            sid = fila[0]
            break

if existe:
    coki = cookies.SimpleCookie()
    # CAMBIAR EL VALOR DE LA COOKIE A UNO HASHEADO CON EL ID USUARIO + EL TIEMPO DE REGISTRO
    coki["SID"] = sid
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=30)  
    coki['SID']['expires'] = expires.strftime("%a, %d, %b %Y %H :%M :%S GMT")
    print(coki)

    registrarTiempo(id, os.path.basename(__file__), 'Inicio de sesión existoso')

    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Entraste",'<meta http-equiv="Refresh" content="2; URL=paginaLibros.py"/>', '', "Validado con exito","Redirigiendo"))
    print(codigoHTML.finalHTML)
        
if not existe:
    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Error", '<meta http-equiv="Refresh" content="2; URL=error.html"/>', '', "Usuario o contrasena no invaldio(s)","Redirigiendo"))
    print(codigoHTML.finalHTML)