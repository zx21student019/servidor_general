#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

print("Content-Type: text/html\n")

print('''
<!DOCTYPE html>
<html lang="en">
    <head>
    
    </head>
    <body>
    <div>
''')

for x in range(1,11):
    print('''
            <a href="producto'''+str(x)+'''.htnl" title="Ir al producto '''+str(x)+'''">Producto numero '''+str(x)+'''</a>
           
         ''')
         
print('''
        </div>
    </body>
</html>
''')
