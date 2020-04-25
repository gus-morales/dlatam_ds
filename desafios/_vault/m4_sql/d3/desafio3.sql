-- cleans and recreates db
DROP DATABASE IF EXISTS desafio3;
CREATE DATABASE desafio3;

\c desafio3

-- creates table artistas
CREATE TABLE artistas
(
    nombre_artista VARCHAR UNIQUE NOT NULL,
    fecha_de_nacimiento DATE,
    nacionalidad VARCHAR,
    PRIMARY KEY (nombre_artista)
);

-- creates table albums
CREATE TABLE albums
(
    titulo_album VARCHAR UNIQUE NOT NULL,
    nombre_artista VARCHAR,
    anio SMALLINT,
    FOREIGN KEY (nombre_artista)
        REFERENCES artistas (nombre_artista),
    PRIMARY KEY (titulo_album)
);

-- creates table canciones
CREATE TABLE canciones
(
    titulo_cancion VARCHAR UNIQUE NOT NULL,
    nombre_artista VARCHAR,
    titulo_album VARCHAR,
    numero_del_track SMALLINT,
    FOREIGN KEY (nombre_artista)
        REFERENCES artistas (nombre_artista),
    FOREIGN KEY (titulo_album)
        REFERENCES albums (titulo_album),
    PRIMARY KEY (titulo_cancion)
);

-- copying data from files to created tables
\copy artistas FROM Artista.csv DELIMITER ',' CSV HEADER;
\copy albums FROM Album.csv DELIMITER ',' CSV HEADER;
\copy canciones FROM Cancion.csv DELIMITER ',' CSV HEADER;

-- query: from subquery, retrieve the 4th track
SELECT titulo_cancion
FROM   canciones
WHERE  numero_del_track = 4
AND    nombre_artista =
-- subquery: 1st USA artist born after 1992
(
    SELECT   nombre_artista
    FROM     artistas
    WHERE    nacionalidad = 'Estadounidense'
    AND      fecha_de_nacimiento > '1992-12-31'
    ORDER BY nombre_artista
    FETCH FIRST ROW ONLY
);

-- FORMA ALTERNATIVA: USANDO JOIN
SELECT c.titulo_cancion FROM canciones AS c
INNER JOIN 
(
    SELECT * FROM artistas
    WHERE nacionalidad = 'Estadounidense'
    AND fecha_de_nacimiento > '1992-12-31'
    LIMIT 1
)
AS a
ON (c.nombre_artista = a.nombre_artista)
WHERE c.numero_del_track = 4;