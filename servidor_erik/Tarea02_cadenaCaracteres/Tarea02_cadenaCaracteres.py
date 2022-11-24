#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

print("Conten-Type: text/text\n")

import cgi

args = cgi.parse()

texto=args['cadena'][0]

print("Ejercicios de cadenas")
print("=======================")
print("Texto recibido: ",texto)
print()

print("-----------------------------------")
print("Ejercicio 1: Buscar una palabra dentro de una frase.")


palabra=args['palabra'][0]

print(palabra.upper() in texto.upper())

print()
print("-----------------------------------")
print("Ejercicio 2: Contar las veces que aparece una letra dentro de una frase.")


letra=args['letra'][0]

contador=0

for l in texto:
    if (l == letra):
        contador = contador+1

print(contador)

print()
print("-----------------------------------")
print("Ejercicio 3: Contar todas las veces que aparecen las vocales en una frase por separado.")


contadorA=0
contadorE=0
contadorI=0
contadorO=0
contadorU=0

for l in texto:
    if ((l == 'a') or (l == 'A')):
        contadorA = contadorA+1
    elif((l=='e')  or (l == 'E')):
        contadorE = contadorE+1
    elif((l=='i')  or (l == 'I')):
        contadorI=contadorI+1
    elif((l=='o')  or (l == 'O')):
        contadorO =contadorO+1
    elif((l=='u')  or (l == 'U')):
        contadorU=contadorU+1

print("A: ",contadorA," E: ",contadorE," I: ",contadorI," O: ",contadorO," U: ",contadorU)

print()
print("-----------------------------------")
print("Ejercicio 4: Dividir una frase en palabras.")

p=""

for l in texto:
    if(l != " "):
        p = p+l
    else:
        p = p + "\n"

print(p)

print()
print("-----------------------------------")
print("Ejercicio 5: Dar la vuelta a las palabras de una frase.")

pR=""

salida=""

for l in texto:
    if(l != " "):
        pR = l+pR
    else:
        salida = salida + " " + pR
        pR=""

salida = salida + " " + pR

print(salida)

print()
print("-----------------------------------")
print("Ejercicio 6: Contar las letras de una frase.")

contLetras = 0

for l in texto:
    if(l != " "):
        contLetras = contLetras + 1

print(contLetras)
