CREATE USER 'generico'@'localhost' IDENTIFIED VIA mysql_native_password USING '***';
GRANT USAGE ON *.* TO 'generico'@'localhost' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;
CREATE DATABASE IF NOT EXISTS `generico`;
GRANT ALL PRIVILEGES ON `generico`.* TO 'generico'@'localhost';

CREATE TABLE tabla (
    id int NOT NULL AUTO_INCREMENT,
    columna1 varchar(200) NOT NULL,
    columna2 varchar(200) UNIQUE,
    columna3 int,
    PRIMARY KEY(id)
);

CREATE TABLE tabla2 (
    id int NOT NULL AUTO_INCREMENT,
    columna1 int,
    columna2 varchar(255),
    tablaId int NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (tablaId) REFERENCES tabla(id)
);