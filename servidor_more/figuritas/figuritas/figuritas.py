#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python.exe

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
     for i in range(nf,0,-1):
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



def rombo(nf):

    linea = ""

    for i in range(nf):
        for k in range(nf-i):
            linea += " " 
        for j in range(i):
            linea += "* "
        print(linea)
        linea = ""
    for i in range(i+1):
        for k in range(i):
            linea += " " 
        for j in range(nf-i):
            linea += "* "
        print(linea)
        linea = ""


def rombo2(nf):

    linea = ""

    for i in range(nf): # 5,4,3,2,1
        for k in range(nf-i-1):# 0,1,2,3,4,
            linea += " " 
        for j in range(i+1):
            linea += str(i+1)+" "
        print(linea)
        linea = ""
    for i in range(nf):
        for k in range(i+1):
            linea += " " 
        for j in range(nf-i-1):
            linea += str(nf-i-1)+" "
        print(linea)
        linea = ""



print('cuadrado: ')
cuadrado(nfilas)
     
print('triángulo normal: ')
trianguloNormal(nfilas)
     
print('triángulo del revés: ')
trianguloNormalReves(nfilas)

print('triángulo dado la vuelta: ')
trianguloNormalVuelta(nfilas)

print('triángulo del revés dado la vuelta: ')
trianguloNormalRevesVuelta(nfilas)
     
print('cuadrado dividido: ')
cuadradoDividido(nfilas)

print('rombo: ')
rombo(nfilas)

print('rombo2: ')
rombo2(nfilas)