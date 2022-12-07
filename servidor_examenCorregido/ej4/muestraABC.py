#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

from http import cookies 
import os

todasCokis={}
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE']
    listaCoki = listaCoki.split('; ')
    
    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCokis[nombre]=valor

print("Content-Type: text/plain\n")

print('Palabras que empiezan por ABC: '+todasCokis['empiezaABC'])
print('Palabras que empiezan por ABC: '+todasCokis['otras'])