#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

print("Conten-Type: text/html\n")

import cgi

args = cgi.parse()
print(args)
print(args['nombre'][0])
print(args['edad'][0])

print(type(args))
print(type(args['nombre'][0]))
print(type(args['edad'][0]))

edad = int(args['edad'][0])
print(edad)
print(type(edad))