#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python
print("Content-Type: text/plain\n")

print('Escribe en la URL "?nfilas=X" donde X es el número que quieras.\n\n')

import cgi

args = cgi.parse()

nfilas = int(args["nfilas"][0])

def cuadrado(nf):
     linea = ""
     for i in range(nf):
          for j in range(nf):
               linea += "* "
          print(linea)
          linea = ""

def trianguloNormal(nf):
     linea = ""
     for i in range(nf):
          for j in range(i+1):
               linea += '* '
          print(linea)
          linea = ''
     
def trianguloNormalReves(nf):
     linea = ""
     for i in range(nf):
          for j in range(nfilas-i-1):
               linea += '  '
          for j in range(i+1):
               linea += '* '
          print(linea)
          linea = ''
     
def trianguloNormalVuelta(nf):
     linea = ""
     for i in range(nf):
          for j in range(nf-i):
               linea += '* '
          print(linea)
          linea = ''
     
def trianguloNormalRevesVuelta(nf):
     linea = ""
     for i in range(nf):
          for j in range(nfilas-i):
               linea += '  '
          for j in range(i):
               linea += '* '
          print(linea)
          linea = ''
     
def cuadradoDividido(nf):
     linea = ""
     for i in range(nfilas):
          for j in range(nfilas-i-1):
               linea += '+ '
          for j in range(i+1):
               linea += '* '
          print(linea)
          linea = ''

print('Vamos a dibujar un cuadrado: ')
cuadrado(nfilas)
     
print('Vamos a dibujar un triángulo normal: ')
trianguloNormal(nfilas)
     
print('Vamos a dibujar un triángulo del revés: ')
trianguloNormalReves(nfilas)

print('Vamos a dibujar un triángulo dado la vuelta: ')
trianguloNormalVuelta(nfilas)

print('Vamos a dibujar un triángulo del revés dado la vuelta: ')
trianguloNormalRevesVuelta(nfilas)
     
print('Vamos a dibujar un cuadrado dividido: ')
cuadradoDividido(nfilas)