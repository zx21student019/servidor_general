#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

print("Conten-Type: text/text\n")

thislist = ["apple","banana","cherry","blueberry"]

#Cuenta la longitud de la lista
print(len(thislist))

#Forma corta de escribir un bucle "for" que recorre la lista
[print(x) for x in thislist]

[print(type(x)) for x in thislist]

#Ejemplos:

#Ejemplo 1
#Se usa "def" para crear una función
def sacaPorPantalla(fruta):
    print("Esto es :",fruta)

[sacaPorPantalla(x) for x in thislist]

#Ejemplo 2
listaNumeros = [1,2,3,4,5,6,7,8,9,10]

listaMayores5 = [x for x in listaNumeros if x > 5]

listaMenoresIgual5 = [x for x in listaNumeros if x <= 5 ]

print(listaMayores5, listaMenoresIgual5)

#Ejemplo 3
def valor01(n):
    if(n>=5):
        return 1
    else:
        return 0

lista01 = [valor01(n) for n in listaNumeros]

print(lista01)




