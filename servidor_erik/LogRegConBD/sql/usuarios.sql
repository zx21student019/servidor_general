CREATE TABLE datosUsuarios ( 
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    nombre varchar(255) NOT NULL UNIQUE, 
    contraseña varchar(512) NOT NULL, 
    email varchar(255) NOT NULL UNIQUE, 
    rol int NOT NULL 
);