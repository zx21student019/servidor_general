#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

import cgi
import json
import codigoHTML as HTML
import datetime
from http import cookies
import hashlib

args = cgi.parse()

nom = args["nombre"][0]
pwd = args["pwd"][0]

pwdCod = hashlib.sha512(str.encode(pwd))

dentro = False

f = open("usuarios/usuarios.json")

usuariosEnJson = json.loads(f.read())

f.close()

for usuario in usuariosEnJson:
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