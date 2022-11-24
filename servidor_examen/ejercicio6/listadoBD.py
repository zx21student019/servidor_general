#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

import mysql.connector

mybd = mysql.connector.connect(
    host='localhost',
    user='biblioteca',
    password='biblioteca',
    database='biblioteca'
)

mycursor = mybd.cursor()
sql = 'SELECT * FROM socios'
mycursor.execute(sql)
myresult = mycursor.fetchall()

print("Content-type:text/plain\n")

print('<html><head><meta charset="UTF-8"></head></html>')
print('<h2>Listado de libros prestados</h2>')

for socio in myresult:
    ids=socio[0]
    nombre=socio[]

    print('<hr>')
    print('<h3>'+socio+'ha recibido el prestamo<h3/>')

    sql= 'SELECT titulo FROM libros where id_socio='(ids)
    mycursor.execute(sql)
    myresult