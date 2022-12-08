#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

from http import cookies
import os
import mysql.connector
from configuracion import configBD

mydb = mysql.connector.connect(
    host=configBD["host"],
    user=configBD["user"],
    password=configBD["passwd"],
    database=configBD["database"]
)

redirigir=""
estasDentro=False
textoLib=""

operacion="insertarLibro.py"
parametros=""

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM usuarios")

lista = mycursor.fetchall()

texto="Insertar Libro"

print("Content-Type: text/html\n")

todasCokis={} #diccionario vacio
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE'] #"SID=ASDFasdf344"
    listaCoki = listaCoki.split('; ') #["SID=ASDFasdf344"]

    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCokis[nombre]=valor

if 'User' in todasCokis:
    for x in lista:
        nomDat=x[1]
        correoDat='"'+x[3]+'"'
        if todasCokis["User"]==correoDat:
            estasDentro=True
            usuario=nomDat
            texto2="Rellena el formulario"
            id_usuario=x[0]


if estasDentro==False :
    redirigir='<meta http-equiv="Refresh" content="5; URL=aplicacion.html" />'
    texto="Error"
    texto2="No has iniciado sesion correctamente"

if estasDentro:
    print(id_usuario, operacion, parametros)
    sql = "INSERT INTO regoperaciones(id_usuario, operacion, parametros,hora) VALUES (%s, %s, %s, now())"
    valores = (id_usuario, operacion, parametros)
    mycursor.execute(sql, valores)
    mydb.commit()


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
        <title>Insertar Libro</title>
        """,redirigir,"""
        
    <style type="text/css">@font-face { font-family: Roboto; src: url("chrome-extension://mcgbeeipkmelnpldkobichboakdfaeon/css/Roboto-Regular.ttf"); }</style>
    <link rel="stylesheet" type="text/css" href="aplicacion.css" title="style">
        <style type="text/css">
            #logOut {
                position: absolute;
                top: 28px;
                right: 150px;
            }

            #insertar {
                background-color: lightgray;
                color: black;
                padding: 5px 30px;
                margin-top: 20px;
                margin-bottom: -10px;
                border: black solid 1px;
                font-size: 24px;
            }

            .libro {
                display: flex;
                justify-content: left;
                background-color: lightgray;
                padding: 20px;
                font-size: 24px;
                margin: 30px 0px;
            }

            p {
                max-width: 300px;
                text-align: left;
                word-wrap: break-word;

            }

            label{
                font-size: 24px;
                font-weight: 400;
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
                    <form action="formulario.py" method="get">
                        <div class="mb-3">
                            <label for="titulo" class="form-label">Titulo</label>
                            <input type="text" class="form-control" name="titulo">
                        </div>
                        <div class="mb-3">
                            <label for="autor" class="form-label">Autor</label>
                            <input type="text" class="form-control" name="autor">
                        </div>
                        <div class="mb-3" id="formulario">
                            <label for="comentario" class="form-label">Comentario</label> <br>
                            <textarea name="message" rows="3" cols="70"></textarea>
                        </div>
                        <div class="mb-3" id="formulario">
                            <label for="imagen" class="form-label">Imagen</label>
                            <input type="text" class="form-control" name="url">
                        </div>
                        <button type="submit" class="btn btn-primary" onClick="subirLibro()">Submit</button>
                    </form>
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
