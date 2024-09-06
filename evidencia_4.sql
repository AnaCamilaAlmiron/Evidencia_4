CREATE DATABASE Evidencia_4;
USE Evidencia_4;

-- Tabla Maquina
CREATE TABLE Maquina (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(50) NOT NULL,
    Descripcion TEXT,
    EstadoMaquina VARCHAR(50) NOT NULL
);

-- Tabla Color
CREATE TABLE Color (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(50) NOT NULL,
    Descripcion TEXT
);

-- Tabla Proceso
CREATE TABLE Proceso (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    ID_Maquina INT,
    Derretir_Cera BOOLEAN NOT NULL,
    ID_Color INT,
    Verter_Cera BOOLEAN NOT NULL,
    Fecha_Proceso DATE NOT NULL,
    FOREIGN KEY (ID_Maquina) REFERENCES Maquina(ID),
    FOREIGN KEY (ID_Color) REFERENCES Color(ID)
);

-- Tabla Temperatura
CREATE TABLE Temperatura (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    ID_Proceso INT,
    Temperatura INT NOT NULL,
    Tiempo_Segundos INT NOT NULL,
    Descripcion TEXT,
    FOREIGN KEY (ID_Proceso) REFERENCES Proceso(ID)
);

-- Tabla Molde
CREATE TABLE Molde (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    ID_Proceso INT,
    Verter_Cera BOOLEAN NOT NULL,
    Descripcion TEXT,
    FOREIGN KEY (ID_Proceso) REFERENCES Proceso(ID)
);

INSERT INTO Maquina (Nombre, Descripcion, EstadoMaquina)
VALUES ('Maquina 1', 'Maquina para derretir cera', 'Operativa');

INSERT INTO Maquina (Nombre, Descripcion, EstadoMaquina)
VALUES ('Maquina 2', 'Maquina de derretido de cera', 'Mantenimiento');

INSERT INTO Color (Nombre, Descripcion)
VALUES ('Rojo', 'Cera de color rojo brillante');

INSERT INTO Color (Nombre, Descripcion)
VALUES ('Azul', 'Cera de color azul');

INSERT INTO Proceso (ID_Maquina, Derretir_Cera, ID_Color, Verter_Cera, Fecha_Proceso)
VALUES (1, TRUE, 1, FALSE, '2024-09-01');

INSERT INTO Proceso (ID_Maquina, Derretir_Cera, ID_Color, Verter_Cera, Fecha_Proceso)
VALUES (2, FALSE, 2, TRUE, '2024-09-02');

INSERT INTO Temperatura (ID_Proceso, Temperatura, Tiempo_Segundos, Descripcion)
VALUES (1, 80, 30, 'Temperatura óptima para derretir parafina roja');

INSERT INTO Temperatura (ID_Proceso, Temperatura, Tiempo_Segundos, Descripcion)
VALUES (2, 80, 30, 'Temperatura ideal para verter cera de soja azul');

INSERT INTO Molde (ID_Proceso, Verter_Cera, Descripcion)
VALUES (2, TRUE, 'Vertido en molde cilíndrico');

INSERT INTO Molde (ID_Proceso, Verter_Cera, Descripcion)
VALUES (1, FALSE, 'Cera derretida, pero no vertida en molde');

SELECT * FROM Maquina
WHERE EstadoMaquina = 'Operativa';

SELECT * FROM Proceso
WHERE Fecha_Proceso = '2024-09-01';

SELECT * FROM Temperatura
WHERE ID_Proceso = 1;

SELECT p.ID, c.Nombre AS Color, p.Fecha_Proceso 
FROM Proceso p
JOIN Color c ON p.ID_Color = c.ID;

SELECT m.ID, m.Descripcion, m.Verter_Cera, p.Fecha_Proceso
FROM Molde m
JOIN Proceso p ON m.ID_Proceso = p.ID;
