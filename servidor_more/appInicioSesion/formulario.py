#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

import cgi
import os
import json

args = cgi.parse()

nombre = args['nombre'][0]
email = args['email'][0]
contrasena = args['contrasena'][0]

usuario = []
usuario.append(nombre)
usuario.append(email)
usuario.append(contrasena)

contenido = []

if (os.path.exists("usuarios.json")):
    f=open("usuarios.json","rt")
    contenido = json.loads(f.read())
    f.close()

contenido.append(usuario)

f=open("usuarios.json","wt")
f.write(json.dumps(contenido))
f.close()
print("Content-type: text/plain\n")
print("acido")