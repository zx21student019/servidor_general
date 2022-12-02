#!C:\Users\zx21student030\AppData\Local\Programs\Python\Python310\python.exe

import codigoHTML,os
from http import cookies
from baseDeDatos import cursor

estasDentro=False

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
            estasDentro=True
            
if estasDentro:
    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format('Insertar Comentario', '', '''
        <nav class="navegacion">
            <a class="enlace" href="paginaLibros.py">Ver Comentarios</a>
            <a class="enlace" href="logout.py">Log Out</a>
        </nav>
        ''', 'Bienvenido', 'Crear comentario del libro:'))
    print(codigoHTML.formularioComentario)
    print(codigoHTML.finalHTML)
else:
    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Error", '<meta http-equiv="Refresh" content="2; URL=error.html"/>', '', "No se ha encontrado la Cookie","Redirigiendo"))
    print(codigoHTML.finalHTML)