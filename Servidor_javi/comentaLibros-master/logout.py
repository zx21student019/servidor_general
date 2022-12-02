#!C:\Users\zx21student030\AppData\Local\Programs\Python\Python310\python.exe

import os, datetime, codigoHTML
from http import cookies
from registrarTimestamp import registrarTiempo

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
    # Habria que poner todasCokis['SID'] pero hay que cambiar esto...
    registrarTiempo(todasCokis['SID'], os.path.basename(__file__), 'Cierre de sesión exitoso')
    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Log out con exito", '<meta http-equiv="Refresh" content="2; URL=comentaLibros.html"/>', '', "Log out con exito","Redirigiendo"))
    print(codigoHTML.finalHTML)