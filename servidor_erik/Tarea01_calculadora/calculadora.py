#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

print("Conten-Type: text/html\n")

import cgi

args=cgi.parse()

n1 = int(args['num1'][0])
n2 = int(args['num2'][0])

operacion=int(args['oper'][0])

# if( operacion == 1):
#     print("La suma de ",n1," + ",n2," es ",(n1+n2))
# elif( operacion == 2):
#     print("La resta de ",n1," - ",n2," es ",(n1-n2))
# elif( operacion == 3):
#     print("La multiplicación de ",n1," * ",n2," es ",(n1*n2))
# elif( operacion == 4):
#     print("La división de ",n1," / ",n2," es ",(n1/n2))

match operacion:
    case 1:
        print("La suma de ",n1," + ",n2," es ",(n1+n2))
    case 2:
        print("La resta de ",n1," - ",n2," es ",(n1-n2))
    case 3:
        print("La multiplicación de ",n1," * ",n2," es ",(n1*n2))
    case 4:
        print("La división de ",n1," / ",n2," es ",(n1/n2))
    case _:
        print("Opción no contemplada")
