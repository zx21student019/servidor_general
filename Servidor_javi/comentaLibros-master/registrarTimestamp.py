from baseDeDatos import baseDeDatos, cursor

def registrarTiempo(idUsuario, operacion, parametros):
     sentencia = 'INSERT INTO regOperaciones (usuarioId, operacion, parametros, timestamp) VALUES (%s, %s, %s, now())'
     valores = (idUsuario, operacion, parametros)
     cursor.execute(sentencia, valores)
     baseDeDatos.commit()