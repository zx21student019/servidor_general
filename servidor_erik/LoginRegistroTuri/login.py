#!C:\Users\alberto.turienzo\AppData\Local\Microsoft\WindowsApps\python

import cgi, os, sys
import json
import codigoHTML
from http import cookies
import datetime
import hashlib

args = cgi.parse()

datos = []
existe = False

if "usuario" in args and "passwd" in args and os.path.exists("datos/usuarios.json"):
    datos.append(args["usuario"][0])
    datos.append(args["passwd"][0])

    f = open("datos/usuarios.json", "rt")
    datosJson = json.loads(f.read())
    f.close()

    #para escribir en el log de error de apache
    for y in datosJson:
        for z in y:
            sys.stderr.write(">"+z+"<")


    for x in datosJson:
        datosNombre = x[0]
        datosEmail = x[1]
        datosPasswd = x[2]

        h=hashlib.sha512(str.encode(datos[1]))

        if datosNombre == datos[0] and datosPasswd == h.hexdigest():
            existe = True
            break

if existe:
    coki = cookies.SimpleCookie()
    coki["SID"] = "alskdjfhg"
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=30)  
    coki['SID']['expires'] = expires.strftime("%a, %d, %b %Y %H :%M :%S GMT")
    print(coki)

    print("Content-Type: text/html\n")

    print(codigoHTML.cabeceraHTML.format("Entraste",'<meta http-equiv="Refresh" content="2; URL=pagina1.py"/>', "Validado con exito. Redirigiendo","",""))
    print(codigoHTML.finalHTML)
        
if not existe:
    print("Content-Type: text/html\n")

    print(codigoHTML.cabeceraHTML.format("Error", '<meta http-equiv="Refresh" content="2; URL=error.html"/>',"Usuario o contraseña no existen. Redirigiendo","",""))
    print(codigoHTML.finalHTML)