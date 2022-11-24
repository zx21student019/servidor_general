#!C:\Users\alberto.turienzo\AppData\Local\Microsoft\WindowsApps\python

import cgi
import json
import os.path
import codigoHTML
import sys
import hashlib

args = cgi.parse()

datos = []

if "usuario" in args and "email" in args and "passwd" in args:
    datos.append(args["usuario"][0])
    datos.append(args["email"][0])
    
    h=hashlib.sha512(str.encode(args["passwd"][0]))
    datos.append(h.hexdigest())
    
    datosJson=[];
    correcto=True

    if(os.path.exists("datos/usuarios.json")): 
        f = open("datos/usuarios.json","rt")
        datosJson=json.loads(f.read())
        f.close()
    else :
        f = open("datos/usuarios.json","w")
        f.write(json.dumps(datosJson))
        f.close

    #para escribir en el log de error de apache
    for y in datosJson:
        for z in y:
            sys.stderr.write(">"+z+"<")    

    for x in datosJson:
        datosNombre = x[0]
        datosEmail = x[1]
        if datosNombre==datos[0] or datosEmail==datos[1]:
            print("Content-Type: text/html\n")
            print(codigoHTML.cabeceraHTML.format("Fallo en el registro",'<meta http-equiv="Refresh" content="2; URL=index.html"/>',"Usuario ya existe. Redirigiendo","",""))
            print(codigoHTML.finalHTML)
            correcto=False
            break

    if correcto:
        datosJson.append(datos)
    
        f = open("datos/usuarios.json","w")
        f.write(json.dumps(datosJson))
        f.close()

        print("Content-Type: text/html\n")

        print(codigoHTML.cabeceraHTML.format("Registro correcto",'<meta http-equiv="Refresh" content="2; URL=index.html"/>',"Redirigiendo","",""))
        print(codigoHTML.finalHTML)
else:
    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Fallo en el registro",'<meta http-equiv="Refresh" content="2; URL=index.html"/>',"Faltan datos. Redirigiendo","",""))
    print(codigoHTML.finalHTML)