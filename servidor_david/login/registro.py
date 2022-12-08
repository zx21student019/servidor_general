#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

import cgi
import json
import os
import hashlib

print("Content-Type: text/html\n")

Url="error.html"
texto="Incorrecto"
texto2="Tu registro ha fallado"
try: 
    noRep= True

    args = cgi.parse()

    nombre= args["nombre"][0]
    contrasena= ((hashlib.sha512(str.encode(args["contrasena"][0]))).hexdigest())

    correo= args["correo"][0]

    Url="aplicacion.html"

    datos=[]
    datos.append(nombre)
    datos.append(contrasena)
    datos.append(correo)

    if (os.path.exists("datos.json")):
        existe=True
    else:
        f = open("datos.json", "wt")
        f.write("[]")
        f.close()


    f = open("datos.json", "rt")
    lista = json.loads(f.read())
    f.close()

    for x in lista:
        nombreDat=x[0]
        contrasenaDat=x[1]
        correoDat=x[2]
        if nombre==nombreDat or correo==correoDat:
            texto=("Incorrecto")
            texto2=("Tu registro ha fallado")
            noRep=False
            break
            
    if noRep==True :
        texto=("Completado")
        texto2=("Te has registrado con exito")
        lista.append(datos)

    f = open("datos.json", "w")
    f.write(json.dumps(lista))
    f.close()
except:
    noSive=True

print("""
<html>
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width,initial-scale=1.0">
        <!-- Latest compiled and minified CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel=" stylesheet ">
        
        <!-- Latest compiled JavaScript -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js "></script>
        
        <!-- Se ha de poner brackets para cambiarlo en el otro codigo -->
        <title>Registro""",texto,"""</title>
        <meta http-equiv="Refresh" content="5; URL=""",Url,"""" />
    <style type="text/css">@font-face { font-family: Roboto; src: url("chrome-extension://mcgbeeipkmelnpldkobichboakdfaeon/css/Roboto-Regular.ttf"); }</style>
    </head>
    <body>
        <div class="container">
            <div class="row">
                <div class="col-3"></div>
                <div class="col-6 text-center">
                    <h3 class="display-3">Registrarse</h3>
                    <h3 class="Display-6">""",texto2,"""</h3>
                </div>
                <div class="col-3"></div>
            </div>
        </div>
    </body>
    </html>

""")