#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/html\n")

import cgi

args = cgi.parse()

x = int(args['num1'][0])

y = int(args['num2'][0])

oper = int(args['oper'][0])

if oper == 1 :
    texto = (x,"+",y,"=",x+y)
elif oper == 2 :
    texto = (x,"-",y,"=",x-y)
elif oper == 3 :
    texto = (x,"*",y,"=",x*y)
else :
    texto = (x,"/",y,"=",x/y)

print("""

<!DOCTYPE html>
<html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Latest compiled and minified CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Latest compiled JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js"></script>
    <title>Document</title>
</head>

<body>
    <div class="container">
        <div class="row">
            <div class="col-3"></div>
            <div class="col-6">
                <h4 class="text-center display-4">Operaciones</h4>
                <hr>
                <h4 class="text-center display-5">""",texto,"""</h4>    
            </div>
            <div class="col-3"></div>
          </div>
    </div>
</body>
</html>
    """)


