CREATE USER 'ventaCamiones'@'localhost' IDENTIFIED VIA mysql_native_password USING '***';
GRANT USAGE ON *.* TO 'ventaCamiones'@'localhost' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;
CREATE DATABASE IF NOT EXISTS `ventaCamiones`;
GRANT ALL PRIVILEGES ON `ventaCamiones`.* TO 'ventaCamiones'@'localhost';

CREATE TABLE camiones (
	id int NOT NULL AUTO_INCREMENT,
    marca varchar(255),
    modelo varchar(255),
    descripcion varchar(255),
    precio float(10),
    imagen varchar(255),
    fechaCreacion DATETIME,
    PRIMARY KEY (id)                 
)

INSERT INTO `camiones`(`marca`, `modelo`, `descripcion`, `precio`, `imagen`, `fechaCreacion`) VALUES ('Volvo','FH 500','Seminuevo','58500','volvoFH500.PNG',now());

INSERT INTO `camiones`(`marca`, `modelo`, `descripcion`, `precio`, `imagen`, `fechaCreacion`) VALUES ('Scania','R450 NTG','Siempre en garaje','78500','scaniaR450NTG.PNG',now());

INSERT INTO `camiones`(`marca`, `modelo`, `descripcion`, `precio`, `imagen`, `fechaCreacion`) VALUES ('Renault','T 520 ADR','Nuevo','44500','renaultT520ADR.PNG',now());