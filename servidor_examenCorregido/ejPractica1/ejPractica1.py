#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python


import cgitb
cgitb.enable()
print('Content-Type: text/html')
numeros = {
    'primero':1.0,
    'segundo':3.0,
    'tercero':5.0,
    'cuarto':7.0,
    'quinto':9.0
}



print('''
<!DOCTYPE html>
<html lang="en">
    <head>
    
    </head>
    <body>
    <tr>
''')
contador=0
segundoContador=0
contadorInverso=0
for f in numeros:
    contador += 1

for i in numeros:
    contadorInverso = int(contador) - int(segundoContador)
    segundoContador=+1
    print(contadorInverso)
    print('''
                <td>'''+str(numeros[contadorInverso])+'''</td>
            ''')


print('''
    </tr>
    </body>
</html>
''')
