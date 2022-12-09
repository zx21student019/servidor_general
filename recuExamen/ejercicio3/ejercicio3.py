#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

marcasCorredor = {
    '1001':["KIPRUTO, RHONEX",3469],
    '1002':["KIPLIMO, JACOB",3457],
    '1003':["KANDIE, KIBIWOTT",	3452],
    '1007':["MUTISO, ALEXANDER",3479],
    '1008':["WANDERS, JULIEN",3595],
    '1009':["KIPLIMO, PHILEMON",3491]
}

print("Content-Type: text/html\n")

print('''
<!DOCTYPE html>
<html lang="en">
    <head>
        
    </head>
    <body>
        <table>
            <tr>
                <th>dorsal</th>
                <th>corredor</th>
            </tr>
''')

ganador =""
tiempo=0
for elemento in marcasCorredor:
    print('''
            <tr>
                <td>'''+elemento+'''</td>
                <td>'''+str(marcasCorredor[elemento][0])+'''</td>
            </tr>
         ''')
    if tiempo==0 or marcasCorredor[elemento][1] < tiempo:
        ganador=marcasCorredor[elemento][0]
        tiempo=marcasCorredor[elemento][1]

print('''
        </table>
            <p>El ganador de la carrera fue '''+str(ganador)+'''</p>
        
    </body>
</html>
''')