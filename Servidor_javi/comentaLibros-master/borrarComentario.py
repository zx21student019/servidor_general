#!C:\Users\zx21student030\AppData\Local\Programs\Python\Python310\python.exe

from registrarTimestamp import registrarTiempo
import cgi, os, cgitb
from baseDeDatos import cursor, baseDeDatos
import codigoHTML

cgitb.enable()
formulario = cgi.FieldStorage()

borrado = False

todasCokis={}
if'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE']
    listaCoki = listaCoki.split(';')

    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCokis[nombre]=valor
    usuario = todasCokis['SID']

if 'SID' in todasCokis:
    cursor.execute('SELECT * FROM usuarios')
    consulta = cursor.fetchall()
    for fila in consulta:
        if(str(fila[0])==todasCokis['SID']):
            if fila[5] == 1:
                admin = True
            estasDentro=True

idLibro = formulario.getvalue('id-libro')

sentencia = "SELECT usuarioId FROM comentarios WHERE id="+str(idLibro)+""
cursor.execute(sentencia)
usuarioLibro = cursor.fetchall()

if str(usuario) == str(usuarioLibro[0][0]) or admin:
    
    sentencia = 'DELETE FROM comentarios WHERE id = '+idLibro
    cursor.execute(sentencia)
    baseDeDatos.commit()
    borrado = True

if borrado:
    registrarTiempo(usuario, os.path.basename(__file__), 'Comentario Borrado')
    print('Content-Type: text/html\n')
    print(codigoHTML.cabeceraHTML.format("Comentario",'<meta http-equiv="Refresh" content="2; URL=paginaLibros.py"/>', '', "Comentario Borrado!","Redirigiendo"))
    print(codigoHTML.finalHTML)
else:
    print('Content-Type: text/html\n')
    print(codigoHTML.cabeceraHTML.format("Comentario",'<meta http-equiv="Refresh" content="2; URL=paginaLibros.py"/>', '', "Erorr al borrar el comentario","Redirigiendo"))
    print(codigoHTML.finalHTML)
