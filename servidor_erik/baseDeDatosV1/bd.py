#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

from ast import For
import mysql.connector

#conectar a la base de datos
mibd = mysql.connector.connect(
    host='localhost',
    user='generico',
    password='generico',
    database='generico'
)

cantRegistros = 5

mycursor = mibd.cursor()

#Creamos la sentencia para añadir los valores a la columnas y especificamos el tipo de dato que vamos a insertar
#%s -> string
#%d -> int
#%f -> float

sql = 'DELETE FROM tabla'
mycursor.execute(sql)

sql = 'INSERT INTO tabla (columna1, columna2, columna3) VALUES (%s,%s,%s)'

#val = ('valor 1','valor 2',0) #valores que se van a añadir en las posiciones por orden
#mycursor.execute(sql,val) #ejecuta la sentencia de sql

#val = ('valor 1.1','valor 2.1',1) #valores que se van a añadir en las posiciones por orden
#mycursor.execute(sql,val) #ejecuta la sentencia de sql

for i in range(cantRegistros):
    val = ('valor 1.'+str(i),'valor 2.'+str(i),i)
    mycursor.execute(sql,val)

val = ('valor 1.F','valor 2.F',i) #valores que se van a añadir en las posiciones por orden
mycursor.execute(sql,val) #ejecuta la sentencia de sql

mibd.commit() #hacemos un commit en la base de datos

print("Conten-Type: text/html\n")

mycursor.execute('SELECT * FROM tabla')

myresult = mycursor.fetchall() #devuelve una lista

print(type(myresult))

for x in myresult:
    print(x[0],"-",x[1],"-",x[2],"-",x[3])

mycursor.execute('SELECT count(*) FROM tabla')

myresult = mycursor.fetchone() #devuelve una tupla

print(type(myresult))
print(myresult[0])

#print(mycursor.rowcount, 'Registro insertado.')