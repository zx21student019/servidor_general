#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

print("Content-Type: text/plain\n")

import cgi
import string

args = cgi.parse()

texto = args["cadena"][0]
palabra =  args["palabra"][0]

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#--------------------------------------EJERCICIO1-------------------------------------
print("-----------------------------------")
print("-----------------------------------")
print("-----------------------------------")
print("EJERCICIO 1: Numero de letras")

contador = 0

for letra in texto:
    if(letra == " "):
        contador -=1
    contador +=1

print(contador)

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#--------------------------------------EJERCICIO2-------------------------------------
print("-----------------------------------")
print("-----------------------------------")
print("-----------------------------------")
print("EJERCICIO 2 :Ver si la la frase contiene la palabra o letra")

boleano = (palabra in texto)

if(boleano == True):
    print("la palabra si esta en la frase")
else:
    print("la palabra no esta en la frase")

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#--------------------------------------EJERCICIO3-------------------------------------
print("-----------------------------------")
print("-----------------------------------")
print("-----------------------------------")
print("EJERCICIO 3: Ver cuantas veces aparece la palabra o letra")

contLetras = 0

for letra in texto:
        if(letra == palabra):
            contLetras +=1
print(contLetras)

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#--------------------------------------EJERCICIO4-------------------------------------
print("-----------------------------------")
print("-----------------------------------")
print("-----------------------------------")
print("EJERCICIO 4: numero de veces que aparece cada vocal")

contA = 0
contE = 0
contI = 0
contO = 0
contU = 0

for letra in texto:
        if(letra == "a"):
            contA +=1
        elif(letra == "e"):
            contE +=1
        elif(letra == "i"):
            contI +=1
        elif(letra == "o"):
            contO +=1
        elif(letra == "u"):
            contU +=1

print("La letra A aparece "+str(contA)+" veces")
print("La letra E aparece "+str(contE)+" veces")
print("La letra I aparece "+str(contI)+" veces")
print("La letra O aparece "+str(contO)+" veces")
print("La letra U aparece "+str(contU)+" veces")


