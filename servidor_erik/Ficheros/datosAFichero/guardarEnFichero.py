#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

print("Conten-Type: text/plain\n")

import cgi
import json

args =  cgi.parse()

datos = []

datos.append(args["nombre"][0])
datos.append(args["edad"][0])

##Si el fichero que ponemos en el open no existe, se crea
f = open("datos/listado.json","a")
f.write(json.dumps(datos)+"\n")
f.close()
