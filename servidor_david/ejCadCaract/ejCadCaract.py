#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python


print("Content-Type: text/text\n")

import cgi

args = cgi.parse()

texto = args['cadena'][0]
palabra = args['palabra'][0]
letra = args['letra'][0]

textoMin = texto.lower()
letraMin = letra.lower()

print("Ejercicios de cadenas")
print("=====================")
print("Texto recibido", texto)

print("=====================")
print("Ejercicio 1 - Contar las letras de una frase.")
contador = 0
for x in texto:
    if x != " " :
        contador += 1
print ("La frase tiene",contador,"letras")

print("=====================")
print("Ejercicio 2 - Buscar una palabra dentro de una frase.")
if texto.find(palabra) != -1:
    print ('El texto "'+texto+ '" si contiene la palabra '+palabra)
else :
    print ('El texto "'+texto+ '" no contiene la palabra '+palabra)

print("=====================")
print("Ejercicio 3 - Contar las veces que aparece una letra dentro de una frase.")


contador = 0
if textoMin.find(letraMin) != -1:  
    for x in textoMin :
        if x == letraMin :
            contador += 1
    print ('El texto "'+texto+ '" si contiene la letra '+letra,contador,"veces")
else :
    print ('El texto "'+texto+ '" no contiene la palabra '+palabra)

print("=====================")
print("Ejercicio 4 - Contar las veces que aparece una letra dentro de una frase.")
contadorA=0
contadorE=0
contadorI=0
contadorO=0
contadorU=0

for x in textoMin : 
    match x :
        case 'a':
            contadorA += 1
        case 'e':
            contadorE += 1
        case 'i':
            contadorI += 1
        case 'o':
            contadorO += 1
        case 'u':
            contadorU += 1

print ('El texto "'+texto+ '" contiene',contadorA,"a,",contadorE,"e,",contadorI,"i,",contadorO,"o y",contadorU,"u.")

print("=====================")
print("Ejercicio 5 - Dividir una frase en palabras.")

palabras = texto.split()

for x in palabras:
    print(x)

print("=====================")
print("Ejercicio 6 - Dar la vuelta a las palabras de una frase.")
salida=""
contPalabras=""

for x in palabras :
    for letra in x :
        contPalabras = letra + contPalabras
    salida = salida+" "+contPalabras
    contPalabras=""


print(salida)
