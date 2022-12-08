#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/html\n")

total = 0
preciosProductosID = {
    "CA132": 99.2,
    "CB231": 55.7,
    "CA332": 101.0,
    "CD563": 65.2,
    "CB838": 48.1
}

print("""<!DOCTYPE html>
<html>
<head>
</head>
<body>
<table>
<tr>
    <th> Identificador </th> <th> Precio </th>
</tr>""")

for producto in preciosProductosID:
    print('<tr><td>', producto, '</td><td>',
          preciosProductosID[producto], '</td></tr>')
    total = total + preciosProductosID[producto]

print('<tr><td>Total:</td><td>',int(total),'</td></th>')
print("""
</table>
</body>

</html>""")
