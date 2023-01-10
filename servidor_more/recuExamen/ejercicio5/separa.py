#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

print("Content-Type: text/html\n")
import cgi
args = cgi.parse()

datos=" "
personas=" "
nombres=""
arrayPersonas=" "
arrayNombres=""
notas=""
aprobados=""
suspensos=""
i=0

f = open("datos.dat", "rt")
for linea in f:
    persona=linea.split(" ")
    if int(persona[1])<5:
        suspensos += persona[0]+" "+persona[1]
        i+1
    else:
        aprobados += persona[0]+" "+persona[1]
        i+1     
f.close()

f = open("aprobados.dat", "w")
f.write(aprobados)
f.close()

f = open("suspensos.dat", "w")
f.write(suspensos)
f.close()

print("""<!DOCTYPE html>
<html>
<head>
</head>
<body>""")
print("<p>Separacion Finalizada</p>")
print("""
</body>

</html>""")