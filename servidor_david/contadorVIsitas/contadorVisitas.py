#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/html\n")

import codigoHtml
import cgi

args = cgi.parse() #devuelve diccionario

contadorLista = args.get("contador",[0])
contador=int(contadorLista[0])

contador=contador+1

print(codigoHtml.cabeceraHtml.format("Contador de visitas","Contador de visitas"))

print('<h5 class="display-5">Esto funciona</h5>')

print('<a href="contadorVisitas.py?contador='+str(contador)+'">Llevas '+str(contador)+ ' visitas</a><br>')

print(codigoHtml.finalHtml)
