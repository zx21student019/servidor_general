#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe
import cgi, os
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
print("Content-Type: text/html\n")
fileitem = form['filename']
# check if the file has been uploaded
if fileitem. filename:
     # strip the leading path from the file name
    fn = os. path.basename (fileitem. filename)
     # open read and write the file into the server
    open("img/"+fn, 'wb').write(fileitem.file.read())