#!C:\Users\aceru\AppData\Local\Programs\Python\Python310\python.exe

import cgi

args = cgi.parse()

notaCorte = args["corte"][0]

texto=""

f = open("nombres.dat", "rt")
nombres = f.read()
listaNombres = nombres.split(" ")
f.close()

f = open("notas.dat", "rt")
notas = f.read()
listaNotas = notas.split(" ")
f.close()

contNota=0

print("Content-Type: text/html\n")


for nota in listaNotas:
    
    if int(nota)>=int(notaCorte):
        texto += listaNombres[contNota]
        texto += " "+nota+"\n"
    contNota +=1  

#con la siguiente linea añadiriamos lo que queremos escribir al documento (si tenemos puesta esa a)
#  f = open("salida.dat", "a")

#con la siguiente linea reescribimos el documento (si tenemos puesta esa w)
f = open("salida.dat", "w")
f.write(texto)
f.close()

print("""<!DOCTYPE html>
<html>
<head>
</head>
<body>""")
print("<p>Filtro realizado</p><p>",texto,"</p>")
print("""
</body>

</html>""")
