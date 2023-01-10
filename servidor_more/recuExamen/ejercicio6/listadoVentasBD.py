#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="museo",
    password="museo",
    database="museo"
)

print("Content-Type: text/html\n")

print("""<!DOCTYPE html>
<html>
<head>
</head>
<body>
<h1>Listado de ventas</h1>""")

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM entradas ORDER BY id")

listaCompradores = mycursor.fetchall()

for comprador in listaCompradores:
    print("<hr><h4>",comprador[1],"ha comprado las siguientes:</h4>")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM entradas WHERE id_comprador="+str(comprador[0]))
    listaVentas = mycursor.fetchall()
    for ventas in listaVentas:
        print("<p>",ventas[1],"de: "+str(ventas[2])+"</p>")

print("""
</body>
</html>""")