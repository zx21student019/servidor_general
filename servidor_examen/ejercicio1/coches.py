#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

import codigoHTML as HTML

print("Conten-Type: text/html\n")
        
print(HTML.cabeceraHtml.format("coches"))
x=0
for x in range(1,21):
        x+1
        print("<div id='contendor"+x+"'>")
        print("<img alt='imagen de coche"+x+"' src='imagen\coche"+x+".png'")
        print("</div>")
print(HTML.finalHtml)