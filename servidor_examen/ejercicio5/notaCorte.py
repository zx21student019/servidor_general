#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

import dat

print("Conten-Type: text/plain\n")

f = open("datos/nombres.dat" ,"rt")

datosEnDatNom = dat.loads(f.read())

f.close()

cadena=[]

for elemento in datosEnDatNom:
    cadena.append(["nombre"][0])



f2 = open("datos/notas.dat" ,"rt")

datosEnDatNot = dat.loads(f.read())

f.close()

for elemento in datosEnDatNot:
    cadena.append(["nota"][0])

f3 = open("datos/salida.dat","a")
f.write(dat.dumps(cadena)+"\n")
f.close()
