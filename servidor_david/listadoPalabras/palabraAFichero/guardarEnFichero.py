#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

import cgi
import json

print("Content-Type: text/plain\n")


args = cgi.parse()

palabra= args["palabra"][0]

palabraLi = list(palabra.splitlines())

f = open("datos\listado.json", "rt")
lista = json.loads(f.read())
f.close()

lista.append(palabraLi)

tam = len(lista)

for i in range(tam):
    print(i,":",type(lista[i]))

print(json.dumps(lista))

f = open("datos\listado.json", "w")
f.write(json.dumps(lista))
f.close()
