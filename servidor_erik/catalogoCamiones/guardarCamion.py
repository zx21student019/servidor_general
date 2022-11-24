#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

import mysql.connector
import json
import cgi
 
#conectar a la base de datos
mydb = mysql.connector.connect(
  host='localhost',
  user='ventaCamiones',
  password='ventaCamiones',
  database='ventaCamiones'
)
 
mycursor = mydb.cursor()

form = cgi.FieldStorage()
marca = form['marca'].value
modelo = form['modelo'].value
precio = form['precio'].value
desc = form['desc'].value

resultado=True

sql="INSERT INTO camiones(marca, modelo, descripcion, precio, fechaCreacion) VALUES (%s,%s,%s,%s,now());"
val=(marca,modelo,desc,precio)
mycursor.execute(sql,val)
mydb.commit()

print("Content-Type: text/plain\n")
print(json.dumps(resultado))