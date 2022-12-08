#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

import cgi
import os
import mysql.connector

args = cgi.parse()

titulo= args["titulo"][0]
autor= args["autor"][0]
mensaje= args["message"][0]
url= args["url"][0]



mydb = mysql.connector.connect(
    host="localhost",
    user="comentalibros",
    password="comentalibros",
    database="comentalibros"
)

redirigir=""
estasDentro=False
textoLib=""

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM usuarios")

lista = mycursor.fetchall()

texto="Comenta Libros"
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
            texto2="Bienveni@ "+usuario 

if estasDentro==False :
    redirigir='<meta http-equiv="Refresh" content="5; URL=aplicacion.html" />'
    texto="Error"
    texto2="No has iniciado sesion correctamente"

if estasDentro:
    mycursor.execute("SELECT * FROM usuarios WHERE mail="+correoDat)
    lista = mycursor.fetchall()
    idUsu=lista[0][0]
    sql = "INSERT INTO comentarios (titulo, autor, comentario, usuarioId, imagen) VALUES (%s, %s, %s, %s, %s)"
    valores=(titulo,autor,mensaje,idUsu,url)
    mycursor.execute(sql, valores)
    mydb.commit()
    texto=("Completado")
    texto2=("Libro insertado con exito")

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
        <meta http-equiv="Refresh" content="5; URL=pagPrincipal.py" />
    <style type="text/css">@font-face { font-family: Roboto; src: url("chrome-extension://mcgbeeipkmelnpldkobichboakdfaeon/css/Roboto-Regular.ttf"); }</style>
    </head>
    <body>
        <div class="container">
            <div class="row">
                <div class="col-3"></div>
                <div class="col-6 text-center">
                    <h3 class="display-3">Insertar</h3>
                    <h3 class="Display-6">""",texto2,"""</h3>
                </div>
                <div class="col-3"></div>
            </div>
        </div>
    </body>
    </html>

""")