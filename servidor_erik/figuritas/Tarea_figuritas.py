#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

print("Conten-Type: text/plain\n")

import cgi

args = cgi.parse()

#Variable que define el numero de filas que va a haber
nfilas=int(args["nfilas"][0])

#Variable que define el tipo de igura que se va a pintar
figura=int(args["figura"][0])

### funcion match para elegir una opcion de figura
def elegirFigura(figura):
    match figura:
        case 1:
            figura1(nfilas)
        case 2:
            figura2(nfilas)
        case 3:
            figura3(nfilas)
        case _:
            print("Opción no contemplada")
#### fin funcion match

### funcion figura con *
def figura1(nf):
    linea=""

    for i in range (nf):
        for k in range(nf-1-i):
            linea += " "
        for j in range (i+1):
            linea += "* "
        print(linea)
        linea=""

    for i in range (nf,1,-1):
        for k in range(nf+1-i):
            linea += " "
        for j in range (i-1):
            linea += "* "
        print(linea)
        linea=""
#### fin funcion figura con *

### función figura con numeros
def figura2(nf):
    cont = 1
    linea=""

    for i in range (nf):
        for k in range(nf-1-i):
            linea += " "
        for j in range (i+1):
            linea += str(cont)+" "
        cont = cont+1
        print(linea)
        linea=""
    cont = int(nf)
    for i in range (nf,1,-1):
        cont = cont-1
        for k in range(nf+1-i):
            linea += " "
        for j in range (i-1):
            linea += str(cont)+" "
        print(linea)
        linea=""
#### fin funcion figura con numeros

### funcion figura con letras
def figura3(nf):
    cont=65
    linea=""

    for i in range (nf):
        for k in range(nf-1-i):
            linea += " "
        for j in range (i+1):
            linea += str(chr(cont))+" "
        cont = cont+1
        print(linea)
        linea=""
    cont=cont-1
    for i in range (nf,1,-1):
        cont = cont-1
        for k in range(nf+1-i):
            linea += " "
        for j in range (i-1):
            linea += str(chr(cont))+" "
        print(linea)
        linea=""
#### fin funcion figura con letras

elegirFigura(figura)
