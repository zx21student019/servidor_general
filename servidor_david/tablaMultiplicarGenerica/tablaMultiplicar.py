#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/html\n")

import cgi

args = cgi.parse()

x = int(args['numero'][0])

#for i in range(1,11):
    #print(x,'*',i,'=',x*i)

print("<!DOCTYPE html>")
print("<html lang=""en"">")
print("<head>")
print("  <title>Bootstrap Example</title>")
print("  <meta charset=""utf-8"">")
print("  <meta name=""viewport"" content=""width=device-width, initial-scale=1"">")
print("  <link href=""https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css"" rel=""stylesheet"">")
print('  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js"></script>')
print("</head>")
print("<body>")
print('    <div class="container mt-3">')
print('    <h2>Tabla de multiplicar</h2>')
if x < 11 :
    print('    <table class="table table-dark table-striped style="width:auto">')
    print('        <tbody>')
    for  i in range(1,11):
        print("<tr><td>",x,"<td><td>*</td><td>",i,"</td><td>=</td><td>",x*i,"</td>")
    print('        </tbody>')
    print('    </table>')
else :
    print('  <div class="alert alert-danger alert-dismissible fade show">')
    print('    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>')
    print('    <strong>Error!</strong> El numero tiene que estar entre 1 y 10.')
    print('  </div>')

print('    </div>')

print('</body>')
print('</html>')
