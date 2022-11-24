#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

import cgi
form = cgi.FieldStorage()
import mysql.connector

if"socio"in form and "titulo" in form and "autor" in form:
    socio = form["socio"].value
    titulo = form["titulo"].value
    autor = form["autor"].value

    mybd = mysql.connector.connect(
    host='localhost',
    user='biblioteca',
    password='biblioteca',
    database='biblioteca'
    )

    mycursor = mybd.cursor()
    sql = 'SELECT id FROM socios where nombre like \"'+socio+'\"'
    mycursor.execute(sql)
    myresult = mycursor.fetchone()


    if mycursor.rowcount == 1:
        ids=myresult[0]

        sql='INSERT INTO libros(titulo,autor,id_socio) VALUES(%s,%s,%s)'

        val = (titulo,autor,ids)
        mycursor.execute(sql, val)
        mybd.commit()

        salida="Libro prestado"
    else:
        salida='Socio no exixte'

else:
    salida="Error,Falta un parametro."

print("Content-type:text/plain\n")

print(salida)
