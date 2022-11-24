#!C:\Users\Javier\AppData\Local\Programs\Python\Python310\python.exe
import sys
sys.path.append('../')

import os
import cgi
import json
from modules.redireccion import redireccion
from http import cookies
import datetime

args = cgi.parse()
datos = []

def loginExitoso():
     if os.path.isfile('./../data/usuarios.json'):
          file = open('./../data/usuarios.json', 'rt')
          usuariosComprobar = json.loads(file.read())
          file.close()
                    
          for usuario in usuariosComprobar: 
               if (usuario[0] == datos[0]) and (usuario[2] == datos[1]):
                         return True
          return False
     else:
          return False

def crearCookie():
     coki = cookies.SimpleCookie()
     coki["SID"]=datos[0]
     expires = datetime.datetime.utcnow() + datetime.timedelta(days=30)
     coki['SID']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
     print(coki)

if len(args)== 2 and ("nombre" in args and "contrasena" in args):
     datos.append(args["nombre"][0])
     datos.append(args["contrasena"][0])

if loginExitoso():
     crearCookie()
     print("Content-Type: text/html\n")
     print(redireccion.format(0, './../app/pagina1.py', '', ''))
else:
     print("Content-Type: text/html\n")
     print(redireccion.format(0, './../modules/error.html', '', ''))
