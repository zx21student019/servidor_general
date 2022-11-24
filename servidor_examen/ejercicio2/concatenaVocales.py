#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

print("Conten-Type: text/html\n")

from ast import For

letras=(['A','E','I','E','A',])

print(letras)

cadena=""
todobien=True

if len(letras) <6:

    for letra in letras:
        if letra =='A'or letra =='E'or letra =='I'or letra =='O'or letra =='U':
            cadena = cadena +letras(letra)
            
        else:
            todobien=False

if todobien:
    print(cadena)
else:
    print("error")