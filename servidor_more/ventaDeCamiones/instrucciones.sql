CREATE TABLE camiones (
    id int NOT NULL AUTO_INCREMENT,
    marca varchar(255),
    modelo varchar(255),
    descripcion varchar(255),
    precio float(10),
    imagen varchar(255),
    PRIMARY KEY (id)
)
 
INSERT INTO
`camiones`(`marca`, `modelo`, `descripcion`, `precio`, `imagen`)
VALUES ('Volvo','FH 500','seminuevo',58500,'VolvoFH500.png');
 
INSERT INTO
`camiones`(`marca`, `modelo`, `descripcion`, `precio`, `imagen`)
VALUES ('Scania','R 450 NTG','Siempre en garage',78500,'scaniaSCANIAR450NTG.png');