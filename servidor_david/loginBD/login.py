#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

import cgi
from http import cookies
import datetime
import hashlib
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="login",
    password="login",
    database="login"
)

args = cgi.parse()

nombreUsu= args["nombre"][0]
contrasenaUsu= ((hashlib.sha512(str.encode(args["contrasena"][0]))).hexdigest())

def ponerCookies():
    coki = cookies.SimpleCookie()
    #esta parte solo se ejecuta la primera vez que accede el usuario
    coki["User"]=correoDat
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=90) # expires in 30 days
    coki['User']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
    print(coki)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM registros")

lista = mycursor.fetchall()

for x in lista:
    nombreDat=x[1]
    contrasenaDat=x[2]
    correoDat=x[3]
    if nombreUsu==nombreDat or nombreUsu==correoDat:
        if contrasenaUsu==contrasenaDat:
            texto=("Login Correcto")
            textoUrl=("pagPrincipal.py")
            ponerCookies()
            break
        else :
            texto=("Contraseña incorrecta")
            textoUrl=("aplicacion.html")
            break
    else :
        texto=("Correo incorrecto")
        textoUrl=("aplicacion.html")

print("Content-Type: text/html\n")


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
        <title>Login</title>
        <meta http-equiv="Refresh" content="3; URL=""",textoUrl,"""" />
    <style type="text/css">@font-face { font-family: Roboto; src: url("chrome-extension://mcgbeeipkmelnpldkobichboakdfaeon/css/Roboto-Regular.ttf"); }</style>
    </head>
    <body>
        <div class="container">
            <div class="row">
                <div class="col-3"></div>
                <div class="col-6 text-center">
                    <h3 class="display-3">Login</h3>
                    <h3 class="Display-6">""" ,texto,"""</h3>
                </div>
                <div class="col-3"></div>
            </div>
        </div>
    </body>
    </html>

""")


