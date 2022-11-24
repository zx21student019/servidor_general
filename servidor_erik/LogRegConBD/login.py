#!C:\Users\zx21student301\AppData\Local\Microsoft\WindowsApps\python

import cgi
import json
import codigoHTML as HTML
import datetime
from http import cookies
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

args = cgi.parse()

nom = args["nombre"][0]
pwd = args["pwd"][0]

pwdCod = hashlib.sha512(str.encode(pwd))

dentro = False

mycursor.execute('SELECT * FROM datosUsuarios')

myresult = mycursor.fetchall()

users = []

for x in myresult:
    valIni = (x[1],x[2],x[3],x[4])
    users.append(valIni)

for usuario in users:
    if(nom == usuario[0]):
        if(pwdCod.hexdigest() == usuario[1]):
            dentro = True

if dentro :
    cuki = cookies.SimpleCookie()
    cuki["SID"] = pwdCod.hexdigest()
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=30) #expira en 30 dias
    cuki['SID']['expires'] = expires.strftime("%a, %d %b %Y %H:%m:%S GMT")
    print(cuki)

print("Conten-Type: text/plain\n")

if dentro :
    HTML.redireccionPag()
else:
    HTML.redireccionError()