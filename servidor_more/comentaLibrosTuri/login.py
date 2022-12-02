#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

import cgi, os ,cgitb
import codigoHTML
from http import cookies
import datetime
import hashlib
import mysql.connector

cgitb.enable()
print("Content-Type: text/html\n")

#conectar a la base de datos
mydb = mysql.connector.connect(
  host='localhost',
  user='comentaLibros',
  password='comentaLibros',
  database='comentaLibros'
)

args = cgi.parse()

existe=False

if "usuario" in args and "passwd" in args:

    usu = args["usuario"][0]
    h=hashlib.sha512(str.encode(args["passwd"][0]))
    passwd=h.hexdigest()
    
    #crear un cursor a la base de datos
    mycursor = mydb.cursor()    

    sql = "SELECT id,passwd,rolId FROM usuarios where usuario = '"+usu+"'"
    mycursor.execute(sql)
    myresult = mycursor.fetchone()

    if myresult != None and myresult[1]==passwd:
        existe = True



if existe:
    #
    coki = cookies.SimpleCookie()
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=30)  
    #se crea la cookie con el id del usuario y la fecha en el momento de hacer la cookie
    coki["SID"] = hashlib.sha512(str.encode(usu+expires.strftime("%a, %d, %b %Y %H :%M :%S GMT"))).hexdigest()
    coki['SID']['expires'] = expires.strftime("%a, %d, %b %Y %H :%M :%S GMT")
    print(coki)

    #se inserta en la base de datos en el campo correspondientes
    sql = "UPDATE usuarios SET coki = '"+coki['SID'].value+"' where usuario like '"+usu+"'"
    mycursor.execute(sql)
    mydb.commit()

    print("Content-Type: text/html\n")
    if(myresult[2]==1):
        print(codigoHTML.cabeceraHTML.format("Entraste",'<meta http-equiv="Refresh" content="2; URL=administrador.py"/>', "Validado con exito. Redirigiendo","",""))
    else:
        print(codigoHTML.cabeceraHTML.format("Entraste",'<meta http-equiv="Refresh" content="2; URL=listaComentarios.py"/>', "Validado con exito. Redirigiendo","",""))
    print(codigoHTML.finalHTML)
        
if not existe:
    print("Content-Type: text/html\n")

    print(codigoHTML.cabeceraHTML.format("Error", '<meta http-equiv="Refresh" content="2; URL=error.html"/>',"Usuario o contraseña no existen. Redirigiendo","",""))
    print(codigoHTML.finalHTML)