#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/text\n")

import cgi

args = cgi.parse()

num = args['numero'][0]
figura = args['figura'][0]

num = int(num)

print("Figuritas")

def numLet(num):
    match num:
        case 1:
            return "A"
        case 2:
            return "B"
        case 3:
            return "C"
        case 4:
            return "D"
        case 5:
            return "E"
        case 6:
            return "F"
        case 7:
            return "G"
        case 8:
            return "H"
        case 9:
            return "I"

def figura1():
    print("=====================")
    print("Figura 1:")


    imprimir=""

    for x in range(num):
        imprimir=""
        for y in range (num-x-1):
            imprimir += " "
        for z in range (x+1):
            imprimir +=("* ")
        print(imprimir)

    for x in range(num-1):
        imprimir=""
        for y in range (x+1):
            imprimir += " "
        for z in range (num-x-1):
            imprimir +=("* ")
        print(imprimir)

def figura2() :

    print("=====================")
    print("Figura 2:")
    numero=0

    for x in range(num):
        
        imprimir=""
        numero +=1
        for y in range (num-x-1):
            imprimir += " "
        for z in range (x+1):
            imprimir +=(str(numero)+" ")
        print(imprimir)

    for x in range(num-1):
        imprimir=""
        numero -=1
        for y in range (x+1):
            imprimir += " "
        for z in range (num-x-1):
            imprimir +=(str(numero)+" ")
        print(imprimir)

def figura3 ():
    
    print("=====================")
    print("Figura 3:")
    numero=0

    for x in range(num):
        
        imprimir=""
        numero +=1
        letra = numLet(numero)

        for y in range (num-x-1):
            imprimir += " "
        for z in range (x+1):
            imprimir +=(letra+" ")
        print(imprimir)

    for x in range(num-1):
        imprimir=""
        numero -=1
        letra = numLet(numero)

        for y in range (x+1):
            imprimir += " "
        for z in range (num-x-1):
            imprimir +=(letra+" ")
        print(imprimir)

if int(figura)==1 :
    figura1()
elif int(figura)==2 :
    figura2()
else :
    figura3()
