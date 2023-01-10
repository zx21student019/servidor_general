CREATE TABLE comprador(
	id INT(6) AUTO_INCREMENT NOT NULL,
	dni VARCHAR(20) NOT NULL UNIQUE,
	CONSTRAINT pk_comprador PRIMARY KEY(id)
	)ENGINE=InnoDb
	CHARACTER SET latin1
	COLLATE latin1_spanish_ci;

CREATE TABLE entradas(
	id INT(6) AUTO_INCREMENT NOT NULL,
	numAdultos INT(3) NOT NULL,
numMenores INT(3) NOT NULL,
	total  FLOAT(2) NOT NULL,
	id_comprador INT(6) NOT NULL,
	CONSTRAINT pk_entradas PRIMARY KEY(id),
	CONSTRAINT fk_entradas_comprador FOREIGN KEY(id_comprador) REFERENCES comprador(id)
	)ENGINE=InnoDb
	CHARACTER SET latin1
	COLLATE latin1_spanish_ci;

INSERT INTO comprador(dni) VALUES ("12345678D");
INSERT INTO comprador(dni) VALUES ("87654321F");