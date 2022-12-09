#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

def cuentaNumeros(frase):
    salida=0
    if len(frase) > 100:
        return 'error'

    for i in frase:
        if(i== '1') or (i== '2') or (i== '3') or (i== '4') or (i== '5')or (i== '6')or (i== '7')or (i== '8')or (i== '9')or (i== '0'):
            salida += 1

    return salida
print("Content-Type: text/plain\n")


print(cuentaNumeros("hola muy buenas"))
print(cuentaNumeros("123 123"))
print(cuentaNumeros("1234567890"))
print(cuentaNumeros("hola 2"))