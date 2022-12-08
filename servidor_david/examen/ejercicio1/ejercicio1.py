#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/html\n")

print("""<!DOCTYPE html>
<html>
<head>
</head>
<body>""")

for i in range(20):
    print('<div id="', i+1, '"><img src="imagen/coche'+str(i+1)+'.png" \
    alt="imagen de coche', i+1, '"></div>')

print("""</body>

</html>""")
