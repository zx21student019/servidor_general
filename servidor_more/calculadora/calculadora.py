#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

print("Content-Type: text/plain\n")

import cgi

args = cgi.parse()

num1 = int(args['num1'][0])
num2 = int(args['num2'][0])
oper = int(args['oper'][0])

if(oper == 1):
    print(num1+num2)

elif(oper == 2):
    print(num1-num2)

elif(oper == 3):
    print(num1*num2)

elif(oper == 4):  
    print(num1/num2)

else: print("error")
