#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

from http import cookies
import os
import json

redirigir=""
estasDentro=False

f = open("datos.json", "rt")
datosEnJson = json.loads(f.read())
f.close()

texto="Pagina principal 2"

print("Content-Type: text/html\n")

todasCokis={} #diccionario vacio
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE'] #"SID=ASDFasdf344"
    listaCoki = listaCoki.split('; ') #["SID=ASDFasdf344"]

    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCokis[nombre]=valor

if 'User' in todasCokis:
    for x in datosEnJson:
        nomDat=x[0]
        correoDat='"'+x[2]+'"'
        if todasCokis["User"]==correoDat:
            estasDentro=True
            usuario=nomDat
            texto2="Bienveni@ "+usuario


if estasDentro==False :
    redirigir='<meta http-equiv="Refresh" content="5; URL=aplicacion.html" />'
    texto="Error"
    texto2="No has iniciado sesion correctamente"

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

        """,redirigir,"""
        
    <style type="text/css">@font-face { font-family: Roboto; src: url("chrome-extension://mcgbeeipkmelnpldkobichboakdfaeon/css/Roboto-Regular.ttf"); }</style>
    <link rel="stylesheet" type="text/css" href="aplicacion.css" title="style">
        <style type="text/css">
            #img2 {
                        height: 420px;
                        margin-top: 20px;
                }

            #divImg {
                display: flex;
                justify-content: center;
            }

            #logOut{
                position: absolute;
                top: 28px;
                right: 150px;
            

            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="row">
                <div class="col-3"></div>
                <div class="col-6 text-center">
                    <h3 class="display-3">""",texto,"""</h3>
                    <h3 class="Display-6">""",texto2,"""</h3>
                    <div id="divImg">
                        <a href='pagPrincipal.py' id="link"><img id="img2" src="nike-dunk-low-syracuse-CU1726-101-2022-release-date-3.jpg" alt=""></a><br>
                    </div>
                     <a href='logOut.py' id="link">
                        <button id="logOut" type="button" class="btn btn-primary">Log Out</button>
                    </a>
                </div>
                <div class="col-3"></div>
            </div>
        </div>
    </body>
    </html>

""")
