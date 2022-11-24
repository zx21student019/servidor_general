#!C:\Users\zx21student301\AppData\Local\Microsoft\WindowsApps\python

import codigoHTML as HTML
import os
from http import cookies
import json
import mysql.connector

#conectar a la base de datos
mibd = mysql.connector.connect(
    host='localhost',
    user='Log/Reg',
    password='Log/Reg',
    database='Log/Reg'
)

mycursor = mibd.cursor()

mycursor.execute('SELECT * FROM datosUsuarios')

myresult = mycursor.fetchall()

users = []

for x in myresult:
    valIni = (x[1],x[2],x[3],x[4])
    users.append(valIni)

print("Conten-Type: text/plain\n")

estaDentro = False

todasCookies = {}
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE'] 
    listaCoki = listaCoki.split('; ') 

    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCookies[nombre] = valor

usuario = ""

if 'SID' in todasCookies:
    for datos in users:
        if(datos[1] == todasCookies["SID"]):
            usuario = datos[0]
            estaDentro=True


if estaDentro:
    print("""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Latest compiled and minified CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Latest compiled JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js"></script>

    <title>Aplicacion</title>

    <style>
        .imagen{
            width: 100%;
            height: 100%;
        }
    </style>
</head>

<body>
    <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
        <div class="container-fluid">
            <svg width="50" height="40" viewBox="0 0 256 255" xmlns="http://www.w3.org/2000/svg" 
                preserveAspectRatio="xMinYMin meet">
            <defs>
                <linearGradient x1="12.959%" y1="12.039%" x2="79.639%" y2="78.201%" id="a">
                    <stop stop-color="#387EB8" offset="0%"/>
                    <stop stop-color="#366994" offset="100%"/>
                </linearGradient>
                <linearGradient x1="19.128%" y1="20.579%" x2="90.742%" y2="88.429%" id="b">
                    <stop stop-color="#FFE052" offset="0%"/>
                    <stop stop-color="#FFC331" offset="100%"/>
                </linearGradient>
            </defs>
            <path d="M126.916.072c-64.832 0-60.784 28.115-60.784 28.115l.072 29.128h61.868v8.745H41.631S.145 61.355.145 126.77c0 65.417 36.21 63.097 36.21 63.097h21.61v-30.356s-1.165-36.21 35.632-36.21h61.362s34.475.557 34.475-33.319V33.97S194.67.072 126.916.072zM92.802 19.66a11.12 11.12 0 0 1 11.13 11.13 11.12 11.12 0 0 1-11.13 11.13 11.12 11.12 0 0 1-11.13-11.13 11.12 11.12 0 0 1 11.13-11.13z" fill="url(#a)"/><path d="M128.757 254.126c64.832 0 60.784-28.115 60.784-28.115l-.072-29.127H127.6v-8.745h86.441s41.486 4.705 41.486-60.712c0-65.416-36.21-63.096-36.21-63.096h-21.61v30.355s1.165 36.21-35.632 36.21h-61.362s-34.475-.557-34.475 33.32v56.013s-5.235 33.897 62.518 33.897zm34.114-19.586a11.12 11.12 0 0 1-11.13-11.13 11.12 11.12 0 0 1 11.13-11.131 11.12 11.12 0 0 1 11.13 11.13 11.12 11.12 0 0 1-11.13 11.13z" 
                fill="url(#b)"/>
            </svg>
        </div>
        <div class="container-fluid">
            <!-- Links -->
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="pag1.py">Pagina 1</a>
                </li>
            </ul>
        </div>
            <!-- Links -->
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="logout.py">LogOut</a>
                </li>
            </ul>
    </nav>
    <div class="imagen">
        <img src="https://clickwallpapers.net/wp-content/uploads/2022/08/clickwallpapers-Python-img1.jpg" width="100%">
    </div>
</body>

</html>""")

else:
    HTML.redireccionError()