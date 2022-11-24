#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

print("Conten-Type: text/plain\n")

import json
import cgi

args = cgi.parse()

f = open("datos\datos.json","rt")

datosEnJson = json.loads(f.read())

f.close()

datosEnList = []

for elemento in datosEnJson:
    datosEnList.append(elemento)

datosEnList.append(args["color"][0])

print(datosEnList)

f = open("datos\datos.json","wt")

f.write(json.dumps(datosEnList)+"\n")

f.close()

print(json.dumps(datosEnList))



