#!C:\Users\zx21student030\AppData\Local\Programs\Python\Python310\python.exe

import codigoHTML,os
from http import cookies
from baseDeDatos import cursor

estasDentro=False

admin = False

comentarios = []

def contarComentarios():
    cursor.execute('SELECT COUNT(*) FROM comentarios')
    consulta = cursor.fetchall()
    return consulta[0][0]

def obtenerComentarios():
    cursor.execute('SELECT * FROM comentarios')
    consulta = cursor.fetchall()
    
    for comentario in consulta:
        botonBorrar = ''
        if str(comentario[4]) == todasCokis['SID'] or admin:
            botonBorrar = codigoHTML.botonBorrarComentario.format(comentario[0])
        imagen = 'libroSinPortada.png'
        if comentario[5] != None:
            imagen = comentario[5]
        comentarios.append(
            codigoHTML.comentario.format(imagen, comentario[1], comentario[2], comentario[3], botonBorrar)
        )     

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
            nombreUsuario = fila[1]
            if fila[5] == 1:
                admin = True
            estasDentro=True
            
if estasDentro:
    print("Content-Type: text/html\n")
    navegacion = '''
        <nav class="navegacion">
            <a class="enlace" href="paginaInsertar.py">Insertar Comentario</a>
            <a class="enlace" href="logout.py">Log Out</a>
        '''
    if admin:
        navegacion += '<a class="enlace" href="administrarUsuarios.py">Administrar Usuarios</a>'
    print(codigoHTML.cabeceraHTML.format('Pagina de Libros', '', navegacion + '</nav>', 'Bienvenido, '+nombreUsuario, 'Numero de comentarios: '+str(contarComentarios()))
    )

    obtenerComentarios()
    
    comentariosHTML = ''
    for comentario in comentarios:
        comentariosHTML += comentario
    
    print(codigoHTML.contenedorComentarios.format(comentariosHTML))

    print(codigoHTML.finalHTML)
else:
    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Error", '<meta http-equiv="Refresh" content="2; URL=error.html"/>', '', "No se ha encontrado la Cookie","Redirigiendo"))
    print(codigoHTML.finalHTML)