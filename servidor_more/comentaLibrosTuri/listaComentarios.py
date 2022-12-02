#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

import codigoHTML,os
from http import cookies
import mysql.connector

#conectar a la base de datos
mydb = mysql.connector.connect(
  host='localhost',
  user='comentaLibros',
  password='comentaLibros',
  database='comentaLibros'
)

estasDentro=False

todasCokis={} 
if'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE'] 
    listaCoki = listaCoki.split(';')
                                
    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCokis[nombre]=valor

if 'SID' in todasCokis:
    #crear un cursor a la base de datos
    mycursor = mydb.cursor() 

    sql = 'SELECT count(*) FROM usuarios where coki like \"'+todasCokis['SID']+'\"'
    mycursor.execute(sql)
    myresult = mycursor.fetchone()

    if(myresult[0]==1):
        estasDentro=True
            
if estasDentro:

    sql = 'SELECT id FROM usuarios where coki like \"'+todasCokis['SID']+'\"'
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    id=myresult[0]

    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Comentarios de fotos","","Comentarios de fotos",
                                         '<form action="creaComentario.py" method="get"><button type="submit" class="btn btn-primary">Crea un comentario nuevo</button></form>',
                                         '<form action="logout.py" method="get"><button type="submit" class="btn btn-primary">Log out</button></form>',"",""))
    
    mycursor.execute("SELECT imagen,titulo,comentario,autor,usuarioId,id FROM comentarios")
    myresult = mycursor.fetchall()

    for x in myresult:
        if(x[4]==id):
            print(codigoHTML.tarjetaComentarioBotonBorrar.format("img/"+x[0],x[0],x[1],x[2],x[3],x[5]))
        else:
            print(codigoHTML.tarjetaComentario.format("img/"+x[0],x[0],x[1],x[2],x[3]))
            

    print(codigoHTML.finalHTML)
else:
    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Error", '<meta http-equiv="Refresh" content="2; URL=error.html"/>',
              "No hay cookie","",""))
    print(codigoHTML.finalHTML)