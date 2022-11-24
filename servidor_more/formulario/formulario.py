#C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

from turtle import ht

print("Content-Type: text/html\n")

import cgi

args = cgi.parse()
print(args),"<br>"
print(args['nombre'][0])
print(args['edad'][0])

print(type(args))
print(type(args['edad']))
print(type(args['edad'][0]))

edad = int(args['edad'][0])

print(edad)
print(type(edad))