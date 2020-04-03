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

-- retrieving 2008 songs:
-- "select title and year from table-'cancion',
-- that will be joined with table-'album',
-- by matching titles on each table,
-- where the year is 2008"
SELECT cancion.titulo_cancion, album.anio
FROM cancion JOIN album 
    ON cancion.titulo_album = album.titulo_album
WHERE album.anio = '2018';

-- albums with their artist nationality:
-- "select title and nationality from table-'album',
-- that will be joined with table-'artista',
-- by matching 'nombre_artista' on each table"
SELECT album.titulo_album, artista.nacionalidad
FROM album JOIN artista
    ON album.nombre_artista = artista.nombre_artista;

-- retrieve:
--   'numero_del_track',
--   'titulo_cancion',
--   'titulo_album',
--   'anio', and
--   'nombre_artista'
-- where the titles should appear sorted by
-- 'anio', 'titulo_album' and 'nombre_artista'
SELECT
    cancion.numero_del_track,
    cancion.titulo_cancion,
    cancion.titulo_album,
    album.anio,
    cancion.nombre_artista
FROM cancion JOIN album
    ON cancion.titulo_album = album.titulo_album
ORDER BY album.anio, cancion.titulo_album, cancion.nombre_artista;
