import mysql.connector # type: ignore

baseDeDatos = mysql.connector.connect(
    host = 'localhost',
    user = 'comentaLibros',
    password = '1234',
    database = 'comentaLibros'
)
cursor = baseDeDatos.cursor()