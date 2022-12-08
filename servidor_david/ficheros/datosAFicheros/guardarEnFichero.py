#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

import cgi
import json

args = cgi.parse()

nombre= args["nombre"][0]
edad = args["edad"][0]


print("Content-Type: text/plain\n")

datos=[]

datos.append(args["nombre"][0])
datos.append(args["edad"][0])

print(json.dumps(datos))

f = open("datos\listado.json", "a")
f.write(json.dumps(datos))
f.close()