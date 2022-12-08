#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/plain\n")

import cgi

args = cgi.parse()
#print(args)

#cgi.parse ( ) args

#print(args)
#print (args['nombre'][0])
print(args['edad'][0])
nombre= args["nombre"][0]
print (type(args))
print (type(args['edad']))
print (type(args['edad'][0]))

edad=int(args['edad'][0])

print(edad)
print(type(edad))


f = open("datos/listado.dat", "a")
f.write()
f.close()
