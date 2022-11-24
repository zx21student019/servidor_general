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

coki = cookies.SimpleCookie()

if 'SID' in todasCokis:
    #crear un cursor a la base de datos
    mycursor = mydb.cursor() 

    sql = 'SELECT count(*) FROM usuarios where rolId = 1 and coki like \"'+todasCokis['SID']+'\"'
    mycursor.execute(sql)
    myresult = mycursor.fetchone()

    if(myresult[0]==1):
        estasDentro=True
            
if estasDentro:
    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Administracion de usuarios","","Administracion de usuarios",
                                         '',
                                         '<form action="logout.py" method="get"><button type="submit" class="btn btn-primary">Log out</button></form>',"",""))
    
    mycursor.execute("SELECT id,usuario,mail FROM usuarios where usuario not like 'admin'")
    myresult = mycursor.fetchall()

    print(codigoHTML.inicioTabla)

    for x in myresult:
        print(codigoHTML.tablausuarios.format(x[0],x[1],x[1],x[2]))

    print(codigoHTML.finalTabla)

    print(codigoHTML.finalHTML)
else:
    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Error", '<meta http-equiv="Refresh" content="2; URL=error.html"/>',
              "No hay cookie","",""))
    print(codigoHTML.finalHTML)