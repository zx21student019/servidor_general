#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

print("Conten-Type: text/text\n")

preciosProductosID = {
    "CA132":99.2,
    "CB231":55.7,
    "CA332":101.0,
    "CD563":65.2,
    "CB838":48.1
}
print("Los identificadores que irian en la cabecera")
identificadores = preciosProductosID.keys();
print(identificadores)

total=0
print("la Columna de los precios contendria lo siguente")
for producto in preciosProductosID:
    print(preciosProductosID[producto])
    total+=preciosProductosID[producto]


print("total")
print(total)