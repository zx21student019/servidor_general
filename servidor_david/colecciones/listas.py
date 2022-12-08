#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/plain\n")

thislist = ["manzana","platano","fresa"]

def sacaPorPantalla(fruta) :
    print("esto es ",fruta)

print(len(thislist))

[sacaPorPantalla(x) for x in thislist]

listaNumeros = [1,2,3,4,5,6,7,8,9,10]

listaMayores5 =[]

for x in listaNumeros :
    if x>5 :
        listaMayores5.append(x)

listaMenores5 = [n for n in listaNumeros if n < 5 ]



print(listaNumeros,listaMayores5,listaMenores5) 