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
    form = cgi.FieldStorage()
    idComent = form['id'].value

    sql = 'SELECT id FROM usuarios where coki like \"'+todasCokis['SID']+'\"'
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    id=myresult[0]    

    print("Content-Type: text/html\n")

    try:
        sql = 'delete FROM comentarios where id='+str(idComent)+' and '+'usuarioId='+str(id)
        mycursor.execute(sql)
        mydb.commit()
    except mysql.connector.Error as err:
        print(codigoHTML.cabeceraHTML.format("No borrado",'<meta http-equiv="Refresh" content="2; URL=listaComentarios.py"/>', "No se pudo borrar. Redirigiendo",str(err),""))        
    else:
        print(codigoHTML.cabeceraHTML.format("Borrado",'<meta http-equiv="Refresh" content="2; URL=listaComentarios.py"/>', "Borrado con exito. Redirigiendo","",""))        
        
    print(codigoHTML.finalHTML)
else:
    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Error", '<meta http-equiv="Refresh" content="2; URL=error.html"/>',
              "No hay cookie","",""))
    print(codigoHTML.finalHTML)