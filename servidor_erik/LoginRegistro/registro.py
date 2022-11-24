#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

print("Conten-Type: text/plain\n")

import cgi
import json
import codigoHTML as HTML
import os
import hashlib
import sys
#sys.stdin (asociado al teclado) - salida teclado
#sys.stdout (asociado a la ventana) -> salida estandard
#sys.stderr (asociado a la ventana) -> salida de error

args =  cgi.parse()

nom = args["nombre"][0]
pwd = args["pwd"][0]
email = args["email"][0]

pwdCod = hashlib.sha512(str.encode(pwd))

usuario = []

usuario.append(nom)
usuario.append(pwdCod.hexdigest())
usuario.append(email)

listaUsuarios = []

if (os.path.exists("usuarios/usuarios.json")):
    f = open("usuarios/usuarios.json" ,"rt")
    usuariosEnJson = json.loads(f.read())
    f.close()

    for valor in usuariosEnJson:
        elemento = []
        elemento.append(valor[0])
        elemento.append(valor[1])
        elemento.append(valor[2])

        listaUsuarios.append(elemento)

        

listaUsuarios.append(usuario)

#para escribir en el registro de errores de apache
for y in listaUsuarios:
    for z in y:
        sys.stderr.write(">"+z+"<")


usuariosJson = json.dumps(listaUsuarios)

f = open("usuarios/usuarios.json" ,"wt")

f.write(usuariosJson)

f.close()

HTML.redireccionPrincipal()
