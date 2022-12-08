#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

import cgi
import os
import hashlib
import mysql.connector
from configuracion import configBD
import datetime

mydb = mysql.connector.connect(
    host=configBD["host"],
    user=configBD["user"],
    password=configBD["passwd"],
    database=configBD["database"]
)

print("Content-Type: text/html\n")

tiempo = datetime.datetime.now()

Url="error.html"
texto="Incorrecto"
texto2="Tu registro ha fallado"
rol= 2
try: 
    
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM usuarios")

    lista = mycursor.fetchall()

    noRep= True
    
    args = cgi.parse()

    nombre= args["nombre"][0]
    contrasena= ((hashlib.sha512(str.encode(args["contrasena"][0]))).hexdigest())
    correo= args["correo"][0]

    Url="aplicacion.html"

    for x in lista:
        nombreDat=x[1]
        contrasenaDat=x[2]
        correoDat=x[3]
        if nombre==nombreDat or correo==correoDat:
            texto=("Incorrecto")
            texto2=("Tu registro ha fallado")
            noRep=False
            break


    if noRep==True :
        sql = "INSERT INTO usuarios (usuario, passwd, mail, rolId, tmpRegistro) VALUES (%s, %s, %s, %s, %s)"
        valores=(nombre,contrasena,correo,rol,tiempo)
        mycursor.execute(sql, valores)
        mydb.commit()
        texto=("Completado")
        texto2=("Te has registrado con exito")

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