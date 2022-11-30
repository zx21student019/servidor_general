#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

import cgi,codigoHTML,os
import cgitb
from http import cookies
import mysql.connector



#conectar a la base de datos
mydb = mysql.connector.connect(
  host='localhost',
  user='comentaLibros',
  password='comentaLibros',
  database='comentaLibros'
)

#variable que indica que el usuario entró correctamente
estasDentro=False

#lista de todas las cookies
todasCokis={} 
if'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE'] 
    listaCoki = listaCoki.split(';')
                                
    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCokis[nombre]=valor

#comprobar la cookie sid es correcta
if 'SID' in todasCokis:
    #crear un cursor a la base de datos
    mycursor = mydb.cursor() 

    sql = 'SELECT count(*) FROM usuarios where coki like \"'+todasCokis['SID']+'\"'
    mycursor.execute(sql)
    myresult = mycursor.fetchone()

    if(myresult[0]==1):
        estasDentro=True


if estasDentro:

    #obtengo la imagen, el titulo y el comentario
    form = cgi.FieldStorage()
    fileitem = form['imagen']
    ttl = form['titulo'].value
    cmntr = form['comentario'].value

    #obtengo el autor y su id
    sql = 'SELECT usuario,id FROM usuarios where coki like \"'+todasCokis['SID']+'\"'
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    usr=myresult[0]
    id=myresult[1]

    #la imagen subida por el cliente se guarda en el directorio img
    if fileitem.filename:
        fn = os.path.basename(fileitem.filename)
        open("img/"+fn, 'wb').write(fileitem.file.read())

    #inserta la informacion en la base de datos
    sql = 'INSERT INTO comentarios (titulo, autor, comentario,usuarioId, imagen ) VALUES (%s,%s,%s,%s,%s)'
    val = (ttl, usr, cmntr, id, fileitem.filename)
    mycursor.execute(sql, val)
    mydb.commit()    

    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Comentario creado", '<meta http-equiv="Refresh" content="2; URL=listaComentarios.py"/>',
              "Comentario Creado","",""))
    print(codigoHTML.finalHTML)
else:
    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Error", '<meta http-equiv="Refresh" content="2; URL=error.html"/>',
              "No hay cookie","",""))
    print(codigoHTML.finalHTML)