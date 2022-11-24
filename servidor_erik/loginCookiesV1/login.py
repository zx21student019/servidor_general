#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

import datetime
from http import cookies
import os
import cgi
import codigoHTML as HTML

args = cgi.parse()

usuarios = {"pepe":["1234","aaaa"],"maria":["0000","bbbb"]}

user = args["nombre"][0]
pwd = args["pwd"][0]
estilos = args["estilos"][0]
dentro = False

if user in usuarios:
    if usuarios[user][0] == pwd:
        dentro = True
    


if dentro :
    cuki = cookies.SimpleCookie()
    cuki["SID"]=usuarios[user][1]
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=30) #expira en 30 dias
    cuki['SID']['expires'] = expires.strftime("%a, %d %b %Y %H:%m:%S GMT")
    print(cuki)



print("Conten-Type: text/html\n")

if dentro:
    print(HTML.cabeceraHtml.format("FBI",estilos,"Entrada al FBI"))
    print('<h6 class="Display-6">Estas dentro</h6>')
    print('<a href="obama.py">Secretos de Obama</a><br>')
    print('<a href="area51.py">Area 51</a><br>')
    print(HTML.finalHtml)
else:
    print(HTML.redireccionError())
    