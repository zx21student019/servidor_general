#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

print("Content-Type: text/html\n")

import codigoHTML
import cgi
args = cgi.parse()

contadorLista =args.get("contador", [0])
contador=int(contadorLista[0])

contador = contador+1

print(codigoHTML.cabeceraHTML.format("Contador de Visitas","Contador de Visitas"))

print('<a href="contadorVisitas.py?contador='+str(contador)+'">Llevas ' +str(contador) + 'visitas</a>')

print("<h3 class='display-5'>Esto si</h3>")

print(codigoHTML.finalHTML)