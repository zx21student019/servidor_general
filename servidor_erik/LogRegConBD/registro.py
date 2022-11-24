#!C:\Users\zx21student301\AppData\Local\Microsoft\WindowsApps\python

print("Conten-Type: text/plain\n")

import cgi
import json
import codigoHTML as HTML
import os
import hashlib
import mysql.connector

#conectar a la base de datos
mibd = mysql.connector.connect(
    host='localhost',
    user='Log/Reg',
    password='Log/Reg',
    database='Log/Reg'
)

mycursor = mibd.cursor()

args =  cgi.parse()

nom = args["nombre"][0]
pwd = args["pwd"][0]
email = args["email"][0]

pwdCod = hashlib.sha512(str.encode(pwd))

mycursor.execute('SELECT * FROM datosUsuarios')

myresult = mycursor.fetchall()

users = []

for x in myresult:
    if(x[1] != 'admin'):
        sqlIni = "INSERT INTO datosUsuarios (nombre,contraseña,email,rol) VALUES (%s, %s, %s, %s);"

        valIni = (x[1],x[2],x[3],x[4])
        users.append(valIni)

sqlDel = 'DELETE FROM datosUsuarios'
mycursor.execute(sqlDel)

sql = "INSERT INTO datosUsuarios (nombre,contraseña,rol) VALUES (%s, %s ,%s);"

pwdAd = "admin"
pwdAdCod = hashlib.sha512(str.encode(pwdAd))

val = ('admin',pwdAdCod.hexdigest(),'1')
mycursor.execute(sql,val)

for u in users:
    mycursor.execute(sqlIni,u)

sql = "INSERT INTO datosUsuarios (nombre,contraseña,email,rol) VALUES (%s, %s, %s, %s);"

val = (nom,pwdCod.hexdigest(),email,'0')
mycursor.execute(sql,val)

mibd.commit()

HTML.redireccionPrincipal()
