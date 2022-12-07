#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

'''

Crear un html con:
20 * div -> img

div id="contenedor1"
    img src="coche1.png" img="imgaen de coche 1"

'''

print("Content-Type: text/html\n")

print('''
<!DOCTYPE html>
<html lang="en">
    <head>
    
    </head>
    <body>
''')

for x in range(1,21):
    print('''
            <div id="contenedor'''+str(x)+'''">
                <img src="img/coche'''+str(x)+'''.png" alt="imagen de coche''',x,'''">
             </div>
         ''')


print('''
    </body>
</html>
''')

