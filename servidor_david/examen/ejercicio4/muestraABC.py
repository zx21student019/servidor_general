#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

from http import cookies
import os

todasCokis={} #diccionario vacio
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE'] #"SID=ASDFasdf344"
    listaCoki = listaCoki.split('; ') #["SID=ASDFasdf344"]

    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCokis[nombre]=valor

print("Content-Type: text/html\n")
print("""<!DOCTYPE html>
<html>
<head>
</head>
<body>""")
print("<p>Palabras que empiezan por ABC:",todasCokis["empiezaABC"],"</p>")
print("<p>Palabras que no empiezan por ABC:",todasCokis["otras"],"</p>")

print("""
</body>

</html>""")