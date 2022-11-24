#!C:\Users\zx21student030\AppData\Local\Programs\Python\Python310\python.exe

import cgi
import json
import os.path
import codigoHTML
import sys
import hashlib
import mysql.connector # type: ignore

args = cgi.parse()

datos = []

baseDeDatos = mysql.connector.connect(
     host = 'localhost',
     user = 'appInicioSesion',
     password = '1234',
     database = 'appInicioSesion'
)
cursor = baseDeDatos.cursor()

if "usuario" in args and "email" in args and "passwd" in args:
    
    datos.append(args["usuario"][0])
    datos.append(args["email"][0])
    h=hashlib.sha512(str.encode(args["passwd"][0]))
    datos.append(h.hexdigest())

    correcto=True

    cursor.execute('SELECT * FROM usuarios')
    consulta = cursor.fetchall()

    for fila in consulta:
        if fila[1]==datos[0] or fila[3]==datos[1]:
            print("Content-Type: text/html\n")
            print(codigoHTML.cabeceraHTML.format("Fallo en el registro",'<meta http-equiv="Refresh" content="2; URL=appInicioSesionBBDD.html"/>',"Usuario ya existe. Redirigiendo","",""))
            print(codigoHTML.finalHTML)
            correcto=False
            break

    if correcto:
        
        sentencia = 'INSERT INTO usuarios (nombre, contrasena, correo, rol) VALUES (%s, %s, %s, 0)'
        valores = (datos[0], datos[2], datos[1])
        cursor.execute(sentencia, valores)
        baseDeDatos.commit()

        print("Content-Type: text/html\n")
        print(codigoHTML.cabeceraHTML.format("Registro correcto",'<meta http-equiv="Refresh" content="2; URL=appInicioSesionBBDD.html"/>',"Redirigiendo","",""))
        print(codigoHTML.finalHTML)
else:
    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Fallo en el registro",'<meta http-equiv="Refresh" content="2; URL=appInicioSesionBBDD.html"/>',"Faltan datos. Redirigiendo","",""))
    print(codigoHTML.finalHTML)