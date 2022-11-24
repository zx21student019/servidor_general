#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python

print("Conten-Type: text/html\n")

import cgi

args = cgi.parse()

num=int(args['num'][0])

if (1 <= num) and (num <= 10):
    for x in range(1,11):
        print("<br>",num , "por ",x," =")
        print(x*num)
else:
    print("Error, el número debe estar entre 1 y 10")