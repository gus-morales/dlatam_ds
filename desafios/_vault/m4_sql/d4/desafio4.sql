-- cleans and recreates db
DROP DATABASE IF EXISTS d4;
CREATE DATABASE d4;

\c d4

-- creates table Inventario
CREATE TABLE inventario
(
    codigo_producto SMALLINT,
    producto VARCHAR,
    locacion VARCHAR,
    precio FLOAT,
    existencia BOOLEAN,
    stock SMALLINT,
    ubicacion VARCHAR,
    numero_bodega SMALLINT,
    vendedor VARCHAR,
    rut_vendedor INTEGER,
    numero_boleta INTEGER,
    cantidad_vendida INTEGER,
    rut_cliente INTEGER,
    nombre_cliente VARCHAR,
    PRIMARY KEY (codigo_producto)
);

-- THIS DOESN'T WORK: BOOLEAN FIELD NOT HOMOGENOUS
-- \copy inventario FROM d4.csv DELIMITER ',' CSV HEADER;

/*
(1NF) Atomicidad: un campo no puede tener
más de dos valores → no se necesita

(2NF) 1NF + Dependencia Parcial: todas las
columnas dependen únicamente de la PK
→ no se cumple, porque por ejemplo,
'vendedor' depende únicamente de 'rut_vendedor'

(3NF) 2NF + Dependencia Transitiva:
todas las columnas NO dependen
transitivamente de la PK
→ tampoco se cumple, porque por ejemplo,
'precio' depende de 'producto',
y 'producto' depende de 'código_producto'

Normalización 3NF propuesta:
dividir la tabla Inventario en las
siguientes tablas con los siguientes campos:
*/

-- Productos:
-- código del producto,
-- nombre producto, y
-- precio asociado
CREATE TABLE productos
(
    codigo_producto INTEGER,
    producto VARCHAR,
    precio FLOAT,
    PRIMARY KEY (codigo_producto)
)

-- Locales:
-- nombre local, y
-- provincia donde se ubica
CREATE TABLE locales
(
    nombre_local VARCHAR,
    provincia VARCHAR,
    PRIMARY KEY (locacion)
)

-- Bodegas:
-- número bodega,
-- a qué local pertenece,
-- qué producto contiene,
-- si tiene existencia de dicho producto, y
-- cuánto stock del mismo
CREATE TABLE bodegas
(
    numero_bodega INTEGER,
    FOREIGN KEY (locacion)
        REFERENCES locales (locacion)
    FOREIGN KEY (producto)
        REFERENCES productos (producto)
    existencia BOOLEAN,
    stock INTEGER,
    PRIMARY KEY (numero_bodega)
)
-- Transacciones:
-- número de la boleta,
-- producto vendido,
-- cantidad_vendida,
-- por quién,
-- a quién, y
-- en qué local
CREATE TABLE transacciones
(
    numero_boleta INTEGER,
    FOREIGN KEY producto,
        REFERENCES productos (producto)
    cantidad_vendida INTEGER,
    FOREIGN KEY vendedor,
        REFERENCES vendedores (vendedor)
    FOREIGN KEY cliente,
        REFERENCES clientes (cliente)
    FOREIGN KEY (locacion)
        REFERENCES locales (locacion)
    PRIMARY KEY (numero_boleta)
)

-- Vendedores:
-- RUT vendedor y nombre del vendedor
CREATE TABLE vendedores
(
    rut_vendedor INTEGER,
    vendedor VARCHAR,
    PRIMARY KEY (rut_vendedor)
)

-- Clientes:
-- RUT cliente y nombre del cliente
CREATE TABLE clientes
(
    rut_cliente INTEGER,
    cliente VARCHAR,
    PRIMARY KEY (rut_cliente)
)
