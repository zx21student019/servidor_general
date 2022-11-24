#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

print("Conten-Type: text/html\n")

import codigoHTML as Html
import cgi

args = cgi.parse()

#iniciar el contador a 0 o al valor que viene desde la URL
contadorLista = args.get("contador",[0])
contador=int(contadorLista[0])

#args -> {"contador": [0]}

#incremento del contador
contador=contador+1

##Inicio del codigo HTML
print(Html.cabeceraHtml.format("Contador de visitas","Contador de visitas"))

#print('<a href="contadorVisitas.py?contador='+str(contador)+'">Llevas '+str(contador)+' visita/s</a><br>')
print('Llevas '+str(contador)+' visita/s<br>')


##method="get"-> muestra la URL (concatena los parametros de los inputs)
##method="post"-> no muestra la URL (no concatena nada)
print('<form action="contadorVisitas.py" method="post">')
print('<input type="hidden" name="contador" value="'+str(contador)+'">')
print('<button type="submit">enviar</button>')
print('<form>')

##Fin codigo HTML
print(Html.finalHtml)