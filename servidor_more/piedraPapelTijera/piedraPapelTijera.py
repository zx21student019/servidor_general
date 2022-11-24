#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

print("Content-Type: text/plain\n")

import cgi
from random import randrange

args = cgi.parse()

jugadaHum = int(args['numero'][0])

jugadaMaq = randrange(1,4)

print(jugadaMaq)

if(jugadaHum == jugadaMaq):
    print("empate")
elif((jugadaHum == 1 and jugadaMaq ==2) or (jugadaHum == 2 and jugadaMaq ==3) or (jugadaHum == 3 and jugadaMaq ==1)):
    print("gana la maquina")
else:
    print("ganastee")