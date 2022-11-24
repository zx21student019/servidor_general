CREATE USER 'comentaLibros'@'localhost' IDENTIFIED VIA mysql_native_password USING '***';
GRANT USAGE ON *.* TO 'comentaLibros'@'localhost' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;
CREATE DATABASE IF NOT EXISTS `comentaLibros`;
GRANT ALL PRIVILEGES ON `comentaLibros`.* TO 'comentaLibros'@'localhost'; 

CREATE TABLE roles (
     id INT NOT NULL AUTO_INCREMENT,
     descripcion VARCHAR(255),
     PRIMARY KEY (id)
);

CREATE TABLE usuarios (
     id INT NOT NULL AUTO_INCREMENT,
     usuario VARCHAR(255) UNIQUE NOT NULL,
     passwd VARCHAR(600) NOT NULL,
     mail VARCHAR(255),
     rolId INT,
     FOREIGN KEY (rolId) REFERENCES roles(id),
     PRIMARY KEY (id)
);

CREATE TABLE comentarios (
     id INT NOT NULL AUTO_INCREMENT,
     titulo VARCHAR(255) NOT NULL,
     autor VARCHAR(255) NOT NULL,
     comentario VARCHAR(3000) NOT NULL,
     usuarioId INT NOT NULL,
     imagen VARCHAR(255),
     PRIMARY KEY (id),
     FOREIGN KEY (usuarioId) REFERENCES usuarios(id)
);