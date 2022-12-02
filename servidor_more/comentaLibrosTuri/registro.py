#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

import cgi ,cgitb
import codigoHTML
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


if "usuario" in args and "email" in args and "passwd" in args:
    user = args["usuario"][0]
    mail = args["email"][0]
    
    h=hashlib.sha512(str.encode(args["passwd"][0]))
    passwd=h.hexdigest()

    #crear un cursor a la base de datos
    mycursor = mydb.cursor()

    #buscar el usuario en base de datos

    sql = 'SELECT COUNT(*) FROM usuarios where usuario like \"%s\"'

    val=(user,)

    mycursor.execute(sql,val)

    myresult = mycursor.fetchone()

    if myresult[0]==0:
        #inserta en base de datos
        sql = 'INSERT INTO usuarios (usuario, passwd, mail,rolId ) VALUES (%s, %s, %s, 2)'

        val = (user, passwd, mail)
        mycursor.execute(sql, val)

        mydb.commit()

        print("Content-Type: text/html\n")
        print(codigoHTML.cabeceraHTML.format("Registro correcto",'<meta http-equiv="Refresh" content="2; URL=index.html"/>',"Redirigiendo","",""))
        print(codigoHTML.finalHTML)
    else:    
        print("Content-Type: text/html\n")
        print(codigoHTML.cabeceraHTML.format("Fallo en el registro",'<meta http-equiv="Refresh" content="2; URL=index.html"/>',"Ya existe el usuario. Redirigiendo","",""))
        print(codigoHTML.finalHTML)
else:
    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Fallo en el registro",'<meta http-equiv="Refresh" content="2; URL=index.html"/>',"Faltan datos. Redirigiendo","",""))
    print(codigoHTML.finalHTML)