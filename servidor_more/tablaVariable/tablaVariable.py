#!C:\Users\zx21student019\AppData\Local\Microsoft\WindowsApps\python.exe

print("Content-Type: text/plain\n")

import cgi

args = cgi.parse()

n = int(args['numero'][0])



if (n >= 0) and (n <= 10) :

    for i in range(1,11):
        print(n ,"x", i ,"=", (n * i))
else:
    print('error')