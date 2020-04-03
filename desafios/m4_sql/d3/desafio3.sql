-- cleans and recreates db
DROP DATABASE IF EXISTS Desafio2;
DROP TABLE IF EXISTS artista CASCADE;
DROP TABLE IF EXISTS album CASCADE;
DROP TABLE IF EXISTS cancion CASCADE;
CREATE DATABASE Desafio2;

-- creates table artista
CREATE TABLE artista
(
    nombre_artista VARCHAR UNIQUE NOT NULL,
    fecha_de_nacimiento DATE,
    nacionalidad VARCHAR,
    PRIMARY KEY (nombre_artista)
);

-- creates table album
CREATE TABLE album
(
    titulo_album VARCHAR UNIQUE NOT NULL,
    nombre_artista VARCHAR,
    anio SMALLINT,
    FOREIGN KEY (nombre_artista)
        REFERENCES Artista (nombre_artista),
    PRIMARY KEY (titulo_album)
);

-- creates table cancion
CREATE TABLE cancion
(
    titulo_cancion VARCHAR UNIQUE NOT NULL,
    nombre_artista VARCHAR,
    titulo_album VARCHAR,
    numero_del_track SMALLINT,
    FOREIGN KEY (nombre_artista)
        REFERENCES Artista (nombre_artista),
    FOREIGN KEY (titulo_album)
        REFERENCES Album (titulo_album),
    PRIMARY KEY (titulo_cancion)
);

-- Copying data from files to previous tables
\copy artista FROM Artista.csv DELIMITER ',' CSV HEADER;
\copy album FROM Album.csv DELIMITER ',' CSV HEADER;
\copy cancion FROM Cancion.csv DELIMITER ',' CSV HEADER;
