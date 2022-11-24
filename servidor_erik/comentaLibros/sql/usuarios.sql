CREATE USER 'comentalibros'@'localhost' IDENTIFIED VIA mysql_native_password USING '***';
GRANT USAGE ON *.* TO 'comentalibros'@'localhost' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;
CREATE DATABASE IF NOT EXISTS `comentalibros`;
GRANT ALL PRIVILEGES ON `comentalibros`.* TO 'comentalibros'@'localhost';

CREATE TABLE roles (
    id int NOT NULL AUTO_INCREMENT,
    descripcion varchar(255),
    PRIMARY KEY (id)
);

CREATE TABLE datosUsuarios ( 
    id int NOT NULL AUTO_INCREMENT, 
    nombre varchar(255) NOT NULL UNIQUE, 
    contraseña varchar(512) NOT NULL, 
    email varchar(255), 
    rolId int,
    FOREIGN KEY (rolId) REFERENCES roles(id),
    PRIMARY KEY (id)
);

CREATE TABLE comentarios(
    id int AUTO_INCREMENT,
    titulo varchar(255) NOT NULL,
    autor varchar(255) NOT NULL,
    comentario varchar(3000) NOT NULL,
    usuarioID int NOT NULL,
    imagen varchar(255),
    FOREIGN KEY (usuarioId) REFERENCES datosusuarios(id),
    PRIMARY KEY (id)
);