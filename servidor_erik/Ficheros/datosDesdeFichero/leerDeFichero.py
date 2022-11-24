#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

print("Conten-Type: text/plain\n")

import json

##r hace referencia a read y t al tipo texto
f = open("datos/listado.json" ,"rt")

##Imprime linea a linea cada linea del fichero
#for x in f:
    #print(x)

##Convierte los datos del archivo json en un array (separa por los [], no el contenido de dentro de cada item)
datosEnJson = json.loads(f.read())

f.close()

#tam = len(datosEnJson)

##Te da cada elemento del array datosEnJson
#for i in range(tam):
    #print(i ,": ",datosEnJson[i])

##Recorre el array de datosEnJson e imprime los valores que existan dentro del elemento del array
for elemento in datosEnJson:
    print(elemento[0],"----",elemento[1])

##Esto imprime el primer elemento del primer item del array, es decir, del elemento 0 del array datosEnJson imprime el primer valor que tenga
print(datosEnJson[0][0])