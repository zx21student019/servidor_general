#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print('Hola, soy un', self.tipo, 'y mi sonido es el', self.onomatopeya,'y mi nombre es:', self.nombre)

class Gato(Animal):
    tipo = 'gato'    

class Perro(Animal):
    tipo = 'perro'

class Canario(Animal):
    tipo = 'canario'


gato = Gato('Fluffy', 'maullido')
gato.saludo()

perro = Perro('Firulais', 'ladrido')
perro.saludo()

canario = Canario('Piolin', 'silvido')
canario.saludo()