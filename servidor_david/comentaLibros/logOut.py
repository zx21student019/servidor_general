#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

import os, datetime
from http import cookies

todasCokis={} #diccionario vacio
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE'] #"SID=ASDFasdf344"
    listaCoki = listaCoki.split('; ') #["SID=ASDFasdf344"]

    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCokis[nombre]=valor

if 'User' in todasCokis:
    coki = cookies.SimpleCookie()
    #esta parte solo se ejecuta la primera vez que accede el usuario
    coki["User"]=todasCokis["User"]
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=-1) # enviar cookie caducada
    coki['User']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
    print(coki)

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
        <meta http-equiv="Refresh" content="3; URL=aplicacion.html" />
    <style type="text/css">@font-face { font-family: Roboto; src: url("chrome-extension://mcgbeeipkmelnpldkobichboakdfaeon/css/Roboto-Regular.ttf"); }</style>
    </head>
    <body>
        <div class="container">
            <div class="row">
                <div class="col-3"></div>
                <div class="col-6 text-center">
                    <h3 class="display-3">Log out</h3>
                    <h3 class="Display-6">Volviendo a la pagina principal</h3>
                </div>
                <div class="col-3"></div>
            </div>
        </div>
    </body>
    </html>

""")