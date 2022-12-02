#!C:\Users\zx21student030\AppData\Local\Programs\Python\Python310\python.exe

from registrarTimestamp import registrarTiempo
import cgi, os, cgitb
from baseDeDatos import cursor, baseDeDatos
import codigoHTML

cgitb.enable()
formulario = cgi.FieldStorage()

insertado = False

def comprobarFormularioRellenado():
     correctos = True
     for x in formulario.keys():
          if formulario.getvalue(x) == '' and x != 'fichero':
               correctos = False
     return correctos

datos = []

todasCokis={}
if'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE']
    listaCoki = listaCoki.split(';')

    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCokis[nombre]=valor
usuario = todasCokis['SID']

if comprobarFormularioRellenado():

     datos.append(formulario.getvalue('titulo'))
     datos.append(formulario.getvalue('autor'))
     datos.append(formulario.getvalue('comentario'))
     portada = None

     fichero = formulario['fichero']
     if fichero.filename:
          nombreFichero = os.path.basename(fichero.filename)
          open('img/'+nombreFichero, 'wb').write(fichero.file.read())
          portada = nombreFichero

     valores = 'Titulo, Autor, Comentario'
     sentencia = 'INSERT INTO comentarios (titulo, autor, comentario, usuarioId, imagen) VALUES (%s, %s, %s, %s, %s)'
     valores = (datos[0], datos[1], datos[2], usuario, portada)
     cursor.execute(sentencia, valores)
     baseDeDatos.commit()
     insertado = True

if insertado:
     registrarTiempo(usuario, os.path.basename(__file__), 'Comentario Insertado')
     print('Content-Type: text/html\n')
     print(codigoHTML.cabeceraHTML.format("Comentario",'<meta http-equiv="Refresh" content="2; URL=paginaLibros.py"/>', '', "Comentario Insertado!","Redirigiendo"))
     print(codigoHTML.finalHTML)
else:
     print('Content-Type: text/html\n')
     print(codigoHTML.cabeceraHTML.format("Comentario",'<meta http-equiv="Refresh" content="2; URL=paginaLibros.py"/>', '', "Erorr al insertar el comentario","Redirigiendo"))
     print(codigoHTML.finalHTML)
