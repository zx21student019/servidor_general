#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

print("Conten-Type: text/html\n")

import cgi
import random

jugadas = ["Piedra","Papel","Tijeras"]

maquina=random.choice(jugadas)

args = cgi.parse()

if(maquina == args['jugada'][0]):
    print("Jugador:"+args['jugada'][0])
    print("máquina:"+maquina)
    print("Empate, vuelva a jugar")

elif((maquina == "Piedra") and (args['jugada'][0]=="Tijeras")):
    print("Jugador:"+args['jugada'][0])
    print("máquina:"+maquina)
    print("Gana la máquina")

elif((maquina=="Papel")and(args['jugada'][0]=="Piedra")):
    print("Jugador:"+args['jugada'][0])
    print("máquina:"+maquina)
    print("Gana la máquina")

elif((maquina=="Tijeras")and(args['jugada'][0]=="Papel")):
    print("Jugador:"+args['jugada'][0])
    print("máquina:"+maquina)
    print("Gana la máquina")

else:
    print("Jugador:"+args['jugada'][0])
    print("máquina:"+maquina)
    print("Gana el Jugador")
