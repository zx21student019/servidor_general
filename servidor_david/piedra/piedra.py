#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/plain\n")

import cgi
from random import randint

args = cgi.parse()

jug2 = randint(1,3)

x = (args['texto'][0]).lower()
jug1 = 0

print(jug2)

if (x=='piedra') :
    print('piedra')
    jug1=1
elif (x=='papel') :
    print('papel')
    jug1=2
elif (x=='tijera') :
    print('tijera')
    jug1=3
else :
    print('Opcion no valida')

if jug1>0 :
    if jug1=jug2 :
        if jug1=1 :
            print('Piedra - Piedra')
            print('Empate')
        
