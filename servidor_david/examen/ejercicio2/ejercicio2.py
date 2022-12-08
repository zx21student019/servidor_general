#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/plain\n")

listaVocales = ['A', 'E', 'A', 'U', 'O']


def concatenaVocales(lista):
    texto = ""
    contador = 0

    for x in lista:
        if x != " ":
            contador += 1

    if contador <= 5:
        for letra in lista:
            match letra:
                case "A":
                    texto = texto +"A"
                case "E":
                    texto = texto +"E"
                case "I":
                    texto = texto +"I"
                case "O":
                    texto = texto +"O"
                case "U":
                    texto = texto +"U"
                case error:
                    texto = "error"
                    break
    else:
        texto = "error"

    return texto


print(concatenaVocales(listaVocales))
