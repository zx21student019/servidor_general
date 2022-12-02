#!C:\Users\zx21student030\AppData\Local\Programs\Python\Python310\python.exe

import cgi
import codigoHTML
import hashlib
from baseDeDatos import cursor, baseDeDatos
import datetime

args = cgi.parse()

datos = []

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
            print(codigoHTML.cabeceraHTML.format("Fallo en el registro",'<meta http-equiv="Refresh" content="2; URL=comentaLibros.html"/>',"Usuario ya existe","Redirigiendo"))
            print(codigoHTML.finalHTML)
            correcto=False
            break

    if correcto:
        sentencia = 'INSERT INTO usuarios (usuario, passwd, mail, tmpRegistro, rolId) VALUES (%s, %s, %s,  %s, 2)'
        valores = (datos[0], datos[2],datos[1], datetime.datetime.now())
        cursor.execute(sentencia, valores)
        baseDeDatos.commit()

        print("Content-Type: text/html\n")
        print(codigoHTML.cabeceraHTML.format("Registro correcto",'<meta http-equiv="Refresh" content="2; URL=comentaLibros.html"/>', '', "Registro completado", "Redirigiendo"))
        print(codigoHTML.finalHTML)
else:
    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Fallo en el registro",'<meta http-equiv="Refresh" content="2; URL=error.html"/>', '', "Faltan datos","Redirigiendo"))
    print(codigoHTML.finalHTML)