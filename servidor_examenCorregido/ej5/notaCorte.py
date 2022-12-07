#!C:\Users\zx19student136\AppData\Local\Microsoft\WindowsApps\python

import cgi

fNombres = open('nombres.dat','rt')
fNotas = open('notas.dat','rt')

nombres = fNombres.read()
notas = fNotas.read()

fNombres.close()
fNotas.close()

nombres = nombres.split(' ')
notas = notas.split(' ')


form = cgi.FieldStorage()
corte = form['corte'].value

fSalida = open('salida.dat','wt')

for x in range(len(nombres)):
    if notas[x] >= corte:
        fSalida.write(nombres[x]+' '+notas[x]+'\n')

fSalida.close()

print("Content-Type: text/plain\n")
print('Filtro realizado')