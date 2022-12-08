CREATE USER 'login'@'localhost' IDENTIFIED VIA mysql_native_password USING '***';
GRANT USAGE ON *.* TO 'login'@'localhost' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;
CREATE DATABASE IF NOT EXISTS `login`;
GRANT ALL PRIVILEGES ON `login`.* TO 'login'@'localhost';

CREATE USER 'comentalibros'@'localhost' IDENTIFIED VIA mysql_native_password USING '***';
GRANT USAGE ON *.* TO 'comentalibros'@'localhost' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;
CREATE DATABASE IF NOT EXISTS `comentalibros`;
GRANT ALL PRIVILEGES ON `comentalibros`.* TO 'comentalibros'@'localhost';

CREATE TABLE registros (
	id int NOT NULL AUTO_INCREMENT,
	nombre varchar(1000) NOT NULL,
    contraseña varchar(1000) NOT NULL,
    correo varchar(1000) NOT NULL,
    rol int DEFAULT '2',
    PRIMARY KEY (id)
);

CREATE TABLE roles (
    id int NOT NULL AUTO_INCREMENT,
    descripcion varchar(255),
    PRIMARY KEY (id)
);
CREATE TABLE usuarios (
    id int NOT NULL AUTO_INCREMENT,
    usuario varchar(255) UNIQUE NOT NULL,
    passwd varchar(600) NOT NULL,
    mail varchar(255),
    rolId int,
    FOREIGN KEY (rolId) REFERENCES roles(id),
    PRIMARY KEY (id)
);

CREATE TABLE comentarios (
    id INT NOT NULL AUTO_INCREMENT,
    titulo varchar(255) NOT NULL,
    autor varchar(255) NOT NULL,
    comentario varchar(3000) NOT NULL,
    usuarioId INT NOT NULL,
    imagen varchar(255),
    PRIMARY KEY (id),
    FOREIGN KEY (usuarioId) REFERENCES usuarios(id)
);

INSERT INTO roles (descripcion) VALUES ('Administrador')
INSERT INTO roles (descripcion) VALUES ('Usuarios')
INSERT INTO usuarios (usuario, passwd, mail, rolId) VALUES ('David','d404559f602eab6fd602ac7680dacbfaadd13630335e951f097af3900e9de176b6db28512f2e000b9d04fba5133e8b1c6e8df59db3a8ab9d60be4b97cc9e81db','david@gmail,com',1)
INSERT INTO comentarios (titulo, autor, comentario, usuarioId, imagen) VALUES ("El Quijote","Cervantes","Buen libro",1,"portada_quijote_s.jpg")