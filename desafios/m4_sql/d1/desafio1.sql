-- creates db, previously dropped in case it already exists
DROP DATABASE IF EXISTS Biblioteca;
CREATE DATABASE Biblioteca;

-- creates table Libro
CREATE TABLE Libro ( 
    id_libro INTEGER NOT NULL,
    nombre_libro VARCHAR,
    autor VARCHAR,
    genero VARCHAR,
    PRIMARY KEY (id_libro)
);

-- inserts values into Libro
INSERT INTO Libro (id_libro, nombre_libro, autor, genero)
VALUES
(1, 'Sapo y Sepo', 'Arnold Lobel', 'dummy_genre_1'),
(2, 'La Metamorfosis', 'Frank Kafka', 'dummy_genre_2');

-- creates table Prestamo
CREATE TABLE Prestamo (
    id_prestamo INTEGER NOT NULL,
    id_libro INTEGER,
    nombre_persona VARCHAR,
    fecha_inicio DATE,
    fecha_termino DATE,
    PRIMARY KEY (id_prestamo),
    FOREIGN KEY (id_libro) REFERENCES Libro (id_libro)
);

-- adds prestado boolean to table Libro
ALTER TABLE Libro ADD prestado BOOLEAN;

-- updates prestado column in one book
UPDATE Libro
    SET prestado = TRUE
    WHERE nombre_libro in ('Sapo y Sepo');

-- updates prestado column in the other book
UPDATE Libro
    SET prestado = FALSE
    WHERE nombre_libro in ('La Metamorfosis');

-- populates prestamo table with required values
INSERT INTO Prestamo (id_prestamo, id_libro, nombre_persona, fecha_inicio,fecha_termino)
VALUES
(1, 1, 'nombre1', '2020-03-01', '2020-03-05'),
(2, 1, 'nombre2', '2020-03-06', '2020-03-08'),
(3, 1, 'nombre3', '2020-03-09', '2020-03-11'),
(4, 1, 'nombre4', '2020-03-12', '2020-03-15'),
(5, 1, 'nombre5', '2020-03-16', '2020-03-19'),
(6, 2, 'nombre6', '2020-03-01','2020-03-05'),
(7, 2, 'nombre7', '2020-03-06', '2020-03-08'),
(8, 2, 'nombre8', '2020-03-09', '2020-03-11'),
(9, 2, 'nombre9', '2020-03-12', '2020-03-15'),
(10, 2, 'nombre10', '2020-03-16', '2020-03-19'),
(11, 2, 'nombre11', '2020-03-16', '2020-03-19');

-- inserts new book
INSERT INTO Libro (id_libro, nombre_libro, autor, genero, prestado)
VALUES
(3, 'Otro Libro', 'Otro autor', 'dummy_genre_3', FALSE);

-- shows books and to whom they are lent
SELECT nombre_libro, nombre_persona FROM Libro
LEFT JOIN Prestamo on Libro.id_libro = Prestamo.id_libro;

-- for the required book, shows lend status sorted by (lend) date
SELECT Prestamo.* FROM Prestamo
LEFT JOIN libro ON libro.id_libro = Prestamo.id_libro
ORDER BY fecha_inicio Desc;
