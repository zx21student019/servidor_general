#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe
import cgi,codigoHTML,os
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

coki = cookies.SimpleCookie()

if 'SID' in todasCokis:
    #crear un cursor a la base de datos
    mycursor = mydb.cursor() 

    sql = 'SELECT count(*) FROM usuarios where coki like \"'+todasCokis['SID']+'\"'
    mycursor.execute(sql)
    myresult = mycursor.fetchone()

    if(myresult[0]==1):
        estasDentro=True
            
if estasDentro:
    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Crear un comentario","","Crear un comentario",
                                         '<form action="listaComentarios.py" method="get"><button type="submit" class="btn btn-primary">volver a la lista de comentarios</button></form>',
                                         '<form action="logout.py" method="get"><button type="submit" class="btn btn-primary">Log out</button></form>',"",""))
    print(codigoHTML.formulario)
    print(codigoHTML.finalHTML)
else:
    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Error", '<meta http-equiv="Refresh" content="2; URL=error.html"/>',
              "No hay cookie","",""))
    print(codigoHTML.finalHTML)