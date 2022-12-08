#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python


print("Content-Type: text/html\n")

print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("</head>")
print("<body>")

y = "\t<h1>hola mundo</h1>"
print(y)
print("<h3><a href=""http://www.dominio1.es"">Inicio</a></h3>")
#comentarios
if 5 > 2:
    print("cinco es mayor que dos")
    print ("hola<br>")

numeros = [5,10]
a,b = numeros
num=7

c=a*b

print("<h3>",c,"</h3>")
  
print("<table border=""1"">")
for x in range (1,11):
    print("<tr><td>",num,"</td><td>*</td><td>",x,"</td><td>",num*x,"</td></tr>")

print("</table>")
print("</body>")
print("</html>")


