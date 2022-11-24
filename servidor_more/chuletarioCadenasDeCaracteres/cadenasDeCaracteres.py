#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

print("Content-Type: text/plain\n")

import cgi

args = cgi.parse()

texto = args["cadena"][0]

print(texto)

#longitud de la palabra o texto
print(len(texto))

#bucle el cuar recorre la palabra letra a letra
for letra in texto:
    print(letra)

#buscar palabra o letra en un texto
print("h" in texto)

#pilla los caracteres en ese tramo, en este caso de segundo al sexto caracter
print(texto[2,6])

#pilla los caracteres desde el principio hasta el indicado y vicebersa
print(texto[:6])
print(texto[2:])

#recorrerlo al rves
r=texto[::-1]
print(r)

#intento de algo que no funciona
#numero = (len(texto))
#for letra in texto:
#    print(texto[numero-1:numero])
#    numero-1

