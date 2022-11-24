#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

print("Conten-Type: text/text\n")

#Creación del diccionario
persona = {
    "nombre":"Juan",
    "apellidos":"Lopez lopez",
    "edad":32,
    "pareja" : True,
    "deportes" : ["furbo", "balonsesto"]
}

print("=======================")
print(persona)

print("=======================")
print(type(persona))

#Para llamar a datos concretos del diccionario se escribe nombre_diccionario["key"]
print("=======================")
print("La edad de",persona["nombre"],"es",persona["edad"])

print("=======================")
print(persona["deportes"][1])

#Cambiar valores del diccionario
persona["nombre"] = "Alberto"
persona["edad"] = 40

print("=======================")
print("La edad de",persona["nombre"],"es",persona["edad"])

#Ver unicamente las claves o keys del diccionario
claves = persona.keys();

print("=======================")
print(claves)

#Añadir claves al diccionario
persona["altura"] = 180

#No hace falta volver a declarar "claves" para que las claves que se actualicen
print("=======================")
print(claves)

#Ver unicamente los valores que contienen cada una de las llaves
valores = persona.values();

print("=======================")
print(valores)

#Recoge tanto la clave como el valor que lleva asociado
listaDeTuplas = persona.items();

print(listaDeTuplas)

print("=======================")
#Recorre los items y los muestra 1 a 1
for itm in listaDeTuplas:
    print(itm[0],itm[1])

#No hace falta volver a declarar los items cuando añadimos o quitamos claves, se actualiza automaticamente
persona["peso"] = 75

print("=======================")
for itm in listaDeTuplas:
    print(itm[0],itm[1])

print("=======================")
if "fechaNac" in persona:
    print(persona["fechaNac"])
else:
    print("No tiene fecha de nacimiento")

persona["fechaNac"] = "22/07/1990"