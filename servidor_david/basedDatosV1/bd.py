#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="generico",
    password="generico",
    database="generico"
)

cantRegistros=5

mycursor = mydb.cursor()

mycursor.execute("DELETE FROM tabla")

sql = "INSERT INTO tabla(columna1, columna2, columna3 ) VALUES (%s, %s, %s)"

for i in range(cantRegistros):
    val = ("valor 1"+str(i),"valor 2"+str(i),i)
    mycursor.execute(sql, val)


mydb.commit()

print("Content-Type: text/plain\n")

mycursor.execute("SELECT * FROM tabla")

myresult = mycursor.fetchall()

print(type(myresult))

for x in myresult:
    print(x)

myresult = mycursor.fetchone()

print(type(myresult))

print(myresult[0])


print(mycursor.rowcount, "Registro insertado.")