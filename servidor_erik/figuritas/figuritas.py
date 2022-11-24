#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

print("Conten-Type: text/plain\n")

from ast import match_case
import cgi

args = cgi.parse()

nfilas=int(args["nfilas"][0])

figura=int(args["figura"][0])

#### funcion cuadrado
def cuadrado(nf) :
    print("Vamos a dibujar un cuadrado de ",args["nfilas"][0], " asteriscos")
    print("")

    linea=""

    for i in range (nf):
        for j in range (nf):
            linea += "*"
        print(linea)
        linea=""
#### fin funcion cuadrado

### funcion trianguloN
def trianguloN(nf):
    print("")
    print("Vamos a dibujar un triángulo normal de ",args["nfilas"][0], " asteriscos")
    print("")

    linea=""

    for i in range (nf):
        for j in range (i+1):
            linea += "*"
        print(linea)
        linea=""
#### fin funcion tringuloN

### funcion trianguloNV
def trianguloNV(nf):
    print("")
    print("Vamos a dibujar un triángulo normal con vuelta de ",args["nfilas"][0], " asteriscos")
    print("")

    linea=""

    for i in range (nfilas,0,-1):
        for j in range (i):
            linea += "*"
        print(linea)
        linea=""
#### fin funcion trianguloNV

### funcion trianguloNR
def trianguloNR(nf):
    print("")
    print("Vamos a dibujar un triángulo normal al revés de ",args["nfilas"][0], " asteriscos")
    print("")

    linea=""

    for i in range (nf):
        for k in range(nf-i-1):
            linea += " "
        for j in range (i+1):
            linea += "*"
        print(linea)
        linea=""
#### fin funcion trianguloNR

### funcion trianguloNVR
def trianguloNVR(nf):
    print("")
    print("Vamos a dibujar un triángulo normal con vuelta al revés de ",args["nfilas"][0], " asteriscos")
    print("")

    linea=""

    for i in range (nfilas,0,-1):
        for k in range(nfilas-i):
            linea += " "
        for j in range (i):
            linea += "*"
        print(linea)
        linea=""
#### fin funcion trianguloNVR

### funcion elegir figura
def elegirFig(figura):
    match figura:
        case 1 :
            cuadrado(nfilas)
        case 2:
            trianguloN(nfilas)
        case 3:
            trianguloNV(nfilas)
        case 4:
            trianguloNR(nfilas)
        case 5:
            trianguloNVR(nfilas)
        case _:
            print("opción no contemplada")
#### fin funcion elegir figura

elegirFig(figura)
