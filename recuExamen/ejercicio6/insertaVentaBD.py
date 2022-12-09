#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

import cgi
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="museo",
    password="museo",
    database="museo"
)

args = cgi.parse()

dni=""
adultos=0
menores=0
total=0

dni = args["dni"][0]
adultos = int(args["adultos"][0])
menores = int(args["menores"][0])

noVacio=False
usuario=False

print("Content-Type: text/plain\n")

if adultos!=" " and menores!=" "and dni!=" ":
    noVacio=True

if noVacio:
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM comprador")

    lista = mycursor.fetchall()
    for comprador in lista:
        if comprador[1]==comprador:
            usuario=True
            idComprador=comprador[0]

if usuario:
    sql = "INSERT INTO entradas (numAdultos, numMenores, total, id_comprador) VALUES (%s, %s, %s, %s)"
    total=(adultos*20)+(menores*5)
    valores=(adultos,menores,total,idComprador)
    mycursor.execute(sql, valores)
    mydb.commit()
    print("Venta registrada")
else:
    print("error")