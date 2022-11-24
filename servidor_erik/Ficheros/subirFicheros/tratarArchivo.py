#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

import os,cgi
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

print("Conten-Type: text/html\n")

fileitem = form['filename']

if fileitem.filename:
    
    fn = os.path.basename(fileitem.filename)

    open("img/"+fn, 'wb').write(fileitem.file.read())
    print("""<html>
        <head>
        </head>
        <body>""")

    print('<img src="img/'+fn+'" style="transform:rotate(90deg);>')

    print("""</body>
        </html>""")