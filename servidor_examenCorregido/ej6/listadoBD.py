#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'biblioteca',
    password = 'biblioteca',
    database = 'biblioteca'
)

mycursor = mydb.cursor()

sql='SELECT id,nombre from socios'
mycursor.execute(sql) 
myResult = mycursor.fetchall()

print('Content-type:text/html\n')

print('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
<h2>Listado de libros prestados</h2>
''')


for socio in myResult:
    id = socio[0]
    nombre = socio[1]
    print('<hr>')
    print('<h2>'+nombre+' ha recibido en prestamo</h2>')

    sql='SELECT titulo from libros where id_socio='+str(id)
    mycursor.execute(sql) 
    myResult2 = mycursor.fetchall()

    for libro in myResult2:
        print('<p>'+libro[0]+'</p>')

print('''
</body>
</html>
''')