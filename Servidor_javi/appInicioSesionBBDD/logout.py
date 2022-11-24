#!C:\Users\zx21student030\AppData\Local\Programs\Python\Python310\python.exe

import os, datetime, codigoHTML
from http import cookies

todasCokis={} 
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE'] 
    listaCoki = listaCoki.split('; ') 

    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCokis[nombre]=valor


if 'SID' in todasCokis:
    coki = cookies.SimpleCookie()
    coki["SID"]=todasCokis["SID"]
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=-1) # enviar cookie caducada
    coki['SID']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
    print(coki)
    logOut = True
            
if logOut:
    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Log out con éxito",
          '<meta http-equiv="Refresh" content="2; URL=appInicioSesionBBDD.html"/>', "Log out con exito. Redirigiendo","",""))
    print(codigoHTML.finalHTML)