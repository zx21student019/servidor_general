#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/plain\n")

import cgi

args = cgi.parse()

x = int(args['num1'][0])

y = int(args['num2'][0])

oper = int(args['oper'][0])

if oper == 1 :
    print(x,"+",y,"=",x+y)
elif oper == 2 :
    print(x,"-",y,"=",x-y)
elif oper == 3 :
    print(x,"*",y,"=",x*y)
else :
    print(x,"/",y,"=",x/y)


