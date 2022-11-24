#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

print("Conten-Type: text/html\n")

from ast import For
import cgi

args=cgi.parse()

texto=args['cadena'][0]

print(texto)

#Cuenta la cantidad de caracteres que forman un texto
print(len(texto))

#Separa el texto en caracteres y los imprime 1 a 1
for letra in texto:
    print(letra)

#Busca la palabra entre comillas en el texto y devuelve true or false
print("que" in texto)

if "que" in texto:
    print("Hola está en '"+texto+"'")

#Solo imprime los caracteres que se encuentren entre los valores introducidos
print(texto[4:8])

#Coloca el texto que escribamos al revés letra por letra
for letra in texto[::-1]:
    print(letra)

#Coloca el texto que escribamos al revés sin separarlo letra por letra
r=""
for pos in range(len(texto)-1,-1,-1):
    r += texto[pos]

print(r)

