#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/plain\n")

import cgi 

args = cgi.parse()

texto = args["cadena"][0]

print(texto)
print(len(texto))

for letra in texto:
    print(letra)

if "hola" in texto:
    print("hola esta en",texto)
else :
    print("hola no esta en",texto)

print (texto[2:10])

print (texto[:10])
print (texto[2:])
print (texto[-3])
print (texto[-8:-3])

cadivn=""

for letra in texto:
    cadivn = letra + cadivn

print (cadivn)


