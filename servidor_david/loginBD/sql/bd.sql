CREATE USER 'login'@'localhost' IDENTIFIED VIA mysql_native_password USING '***';
GRANT USAGE ON *.* TO 'login'@'localhost' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;
CREATE DATABASE IF NOT EXISTS `login`;
GRANT ALL PRIVILEGES ON `login`.* TO 'login'@'localhost';

CREATE TABLE registros (
	id int NOT NULL AUTO_INCREMENT,
	nombre varchar(1000) NOT NULL,
    contraseña varchar(1000) NOT NULL,
    correo varchar(1000) NOT NULL,
    rol int DEFAULT '0',
    PRIMARY KEY (id)
);