#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

import cgi
import mysql.connector

form = cgi.FieldStorage()

if 'socio' in form and 'titulo' in form and 'autor' in form:
    socio = form['socio'].value
    titulo = form['titulo'].value
    autor = form['autor'].value

    mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'biblioteca',
            password = 'biblioteca',
            database = 'biblioteca'
    )

    mycursor = mydb.cursor()

    sql='SELECT id from socios where nombre like\"'+socio+'\"'
    mycursor.execute(sql) 
    myResult = mycursor.fetchone()


    if mycursor.rowcount == 1:
        
        id = myResult[0]

        sql = 'INSERT INTO libros (titulo, autor, id_socio) VALUES(%s,%s,%s)'
        val = (titulo,autor,id)
        mycursor.execute(sql,val)
        mydb.commit()

        salida = 'Libro prestado.'
    else:
        salida = 'El socio no existe'

    
else:
    salida = 'Error. Falta un parametro.'


print('Content-Type:text/plain\n')
print(salida)