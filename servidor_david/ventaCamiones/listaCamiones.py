#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

import mysql.connector
import json

mydb = mysql.connector.connect(
    host='localhost',
    user='ventaCamiones',
    password='ventaCamiones',
    database='ventaCamiones'
)

mycursor = mydb.cursor()

sql="SELECT imagen,modelo,marca,precio,descripcion FROM camiones ORDER BY fechaCreacion DESC"
mycursor.execute(sql)
lc = mycursor.fetchall()
print("Content-Type: text/plain\n")
print(json.dumps(lc))