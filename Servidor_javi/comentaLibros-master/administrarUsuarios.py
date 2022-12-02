#!C:\Users\zx21student030\AppData\Local\Programs\Python\Python310\python.exe

import codigoHTML,os
from http import cookies
from baseDeDatos import cursor

estasDentro=False

admin = False

def obtenerUsuarios():
     cursor.execute('SELECT * FROM usuarios')
     consulta = cursor.fetchall()
     usuarios = ''
     for usuario in consulta:
          usuarios += codigoHTML.filaUsuario.format(
               usuario[0],
               usuario[1],
               usuario[3],
               usuario[0]
          )
     return usuarios

todasCokis={} 
if'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE'] 
    listaCoki = listaCoki.split(';')
                                
    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCokis[nombre]=valor

coki = cookies.SimpleCookie()

if 'SID' in todasCokis:
     cursor.execute('SELECT * FROM usuarios')
     consulta = cursor.fetchall()
     for fila in consulta:
          if(str(fila[0])==todasCokis['SID']):
               if fila[5] == 1:
                    admin = True
               estasDentro=True
            
if admin and estasDentro:
     print("Content-Type: text/html\n")
     navegacion = '''
     <nav class="navegacion">
       <a class="enlace" href="paginaInsertar.py">Insertar Comentario</a>
       <a class="enlace" href="logout.py">Log Out</a>
       <a class="enlace" href="administrarUsuarios.py">Administrar Usuarios</a>
     '''
     print(codigoHTML.cabeceraHTML.format('Pagina de Libros', '', navegacion + '</nav>', 'Bienvenido, Admin', 'Administrar Usuarios'))

     usuariosHTML = obtenerUsuarios()
    
     print(codigoHTML.tablaUsuarios.format(usuariosHTML))

     print(codigoHTML.finalHTML)
else:
    print('Content-Type: text/html\n')
    print(codigoHTML.cabeceraHTML.format("Comentario",'<meta http-equiv="Refresh" content="2; URL=paginaLibros.py"/>', '', "Erorr al administrar los usuarios","Redirigiendo"))
    print(codigoHTML.finalHTML)