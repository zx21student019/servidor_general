#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

import cgi
import mysql.connector

args = cgi.parse()

nombre = args['nombre'][0]
email = args['email'][0]
contrasena = args['contrasena'][0]

print("Content-Type: text/plain\n")

mydb = mysql.connector.connect(
        host="localhost",
        user="login",
        password="1234",
        database="login"
)

mycursor = mydb.cursor()

sql = "INSERT INTO usuarios (nombre, email, contrasena, roll) VALUES (%s, %s, %s, %s)"
val = (nombre, email, contrasena,0)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")