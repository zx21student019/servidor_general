redireccionHTML="""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta http-equiv="Refresh" content="{}; URL={}" />
</head>
<body>
    <h3>{}</h3>
    <h5>Redireccionando</h5>
</body>
</html>
"""

redireccion = lambda r,s,t : print(redireccionHTML.format(r,s,t))

def redireccionPrincipal():
    redireccion(2,"aplicacion.html","Completado") 

def redireccionPag():
    redireccion(2,"pag1.py","Login correcto")

def redireccionError():
    redireccion(4,"aplicacion.html","Error, debe registrarse o iniciar sesion")

def redireccionLogout():
    redireccion(2,"aplicacion.html","Sesión cerrada con éxito")