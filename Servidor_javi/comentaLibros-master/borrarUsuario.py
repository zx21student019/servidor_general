#!C:\Users\zx21student030\AppData\Local\Programs\Python\Python310\python.exe

from registrarTimestamp import registrarTiempo
import cgi, os, cgitb
from baseDeDatos import cursor, baseDeDatos
import codigoHTML

print('Content-Type: text/html\n')
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

idUsuario = formulario.getvalue('id-usuario')

sentencia = "SELECT usuarioId FROM comentarios WHERE id="+str(idUsuario)+""
cursor.execute(sentencia)
usuarioLibro = cursor.fetchall()

if admin:
     sentencia = 'DELETE FROM comentarios WHERE usuarioId = '+idUsuario
     cursor.execute(sentencia)
     sentencia = 'DELETE FROM usuarios WHERE id = '+idUsuario
     cursor.execute(sentencia)
     baseDeDatos.commit()
     borrado = True

if borrado:
     registrarTiempo(usuario, os.path.basename(__file__), 'Usuario Borrado')
     print('Content-Type: text/html\n')
     print(codigoHTML.cabeceraHTML.format("Usuario",'<meta http-equiv="Refresh" content="2; URL=administrarUsuarios.py"/>', '', "Usuario Eliminado!","Redirigiendo"))
     print(codigoHTML.finalHTML)
else:
     print('Content-Type: text/html\n')
     print(codigoHTML.cabeceraHTML.format("Usuario",'<meta http-equiv="Refresh" content="2; URL=paginaLibros.py"/>', '', "Error al eliminar el Usuario","Redirigiendo"))
     print(codigoHTML.finalHTML)
