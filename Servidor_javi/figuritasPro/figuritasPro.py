#!C:\Users\zx21student030\AppData\Local\Programs\Python\Python310\python.exe
print("Content-Type: text/plain\n")

print('Escribe en la URL "?nfilas=X&tipo=Y" donde X es el número que quieras\ne Y el tipo de figura a imprimir (1, 2 o 3)\n\n')

import cgi
from socket import inet_aton

args = cgi.parse()

nfilas = int(args["nfilas"][0])
tipo = int(args["tipo"][0])
caracter = '* '

def llenarAbecedario():
     abecedario = []
     for i in range(65, 91):
          abecedario.append(chr(i))
     return abecedario

abecedario = llenarAbecedario()

def figuraUno(nf, c):
     linea = ""
     for i in range(nf):
          for j in range(nf-i-1):
               linea += ' '
          for j in range(i+1):
               linea += c
          print(linea)
          linea = ''
     
     nf -= 1
     for i in range(nf):
          for j in range(i+1):
               linea += ' '
          for j in range(nf-i):
               linea += c
          print(linea)
          linea = ''

def figuraDos(nf, c):
     contador = 1
     linea = ""
     for i in range(nf):
          for k in range(nf-i-1):
               linea += ' '
          for j in range(i+1):
               linea += str(contador)+' '
          contador += 1
          print(linea)
          linea = ''
     
     nf -= 1
     contador -= 2
     for i in range(nf):
          for k in range(i+1):
               linea += ' '
          for j in range(nf-i):
               linea += str(contador)+' '
          contador -= 1
          print(linea)
          linea = ''
     
def figuraOpcional(nf, c):
     contador = 1
     linea = ""
     for i in range(nf):
          for k in range(nf-i-1):
               linea += ' '
          for j in range(i+1):
               linea += sustituirNumero(contador, abecedario)+' '
          contador += 1
          print(linea)
          linea = ''
     
     nf -= 1
     contador -= 2
     for i in range(nf):
          for k in range(i+1):
               linea += ' '
          for j in range(nf-i):
               linea += sustituirNumero(contador, abecedario)+' '
          contador -= 1
          print(linea)
          linea = ''
                  
def sustituirNumero(num, abecedario):
     if(num <= len(abecedario)):
          return(abecedario[num-1])
     else:
          return('?')
        
match tipo:
     case 1:
          print('Figura Uno: ')
          figuraUno(nfilas, caracter)
     case 2:
          print('Figura Dos: ')
          figuraDos(nfilas, caracter)
     case 3:
          print('Figura Opcional: ')
          figuraOpcional(nfilas, caracter)
     case other:
          print('Introduce un número válido.')