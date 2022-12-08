#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

import json

print("Content-Type: text/plain\n")

f = open("datos\listado.json", "rt")

datosEnJson = json.loads(f.read())
print(datosEnJson)
print(type(datosEnJson[2][1]))

f.close()

tam = len(datosEnJson)

for i in range(tam):
    print(i,":",datosEnJson[i])

for elemento in datosEnJson:
    print(elemento[0],"---",elemento[1])