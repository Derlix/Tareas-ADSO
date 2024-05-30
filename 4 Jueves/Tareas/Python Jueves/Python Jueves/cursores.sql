DELIMITER //
CREATE PROCEDURE calcular_final()
BEGIN
-- En MySql se debe declarar variables antes de cursores
DECLARE v_id FLOAT;
DECLARE v_n1 FLOAT;
DECLARE v_n2 FLOAT;
DECLARE v_n3 FLOAT;
DECLARE v_final FLOAT;
DECLARE v_hay_registros BOOLEAN DEFAULT TRUE; --Sacrificio
-- Declaramos el cursor
DECLARE c_calcular_nota CURSOR FOR SELECT id, nota1, nota2, nota3
FROM nota; 
-- Declaramos Handler o controlador de error
DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_hay_registros = FALSE; --cuano no lo encuentrase cambia a falso y el bucle se detiene

-- Abrimos el Cursor y asignamos valores a variables
OPEN c_calcular_nota;
FETCH c_calcular_nota INTO v_id, v_n1, v_n2, v_n3;
-- Bucle para hacer el proceso con todos los registros existentes
WHILE v_hay_registros DO
SET v_final = ((v_n1*20)/100)+((v_n2*30)/100)+((v_n3*50)/100);
UPDATE nota SET final = v_final WHERE id = v_id;
FETCH c_calcular_nota INTO v_id, v_n1, v_n2, v_n3;
END WHILE;
-- Cerramos el Cursor
CLOSE c_calcular_nota;
END;
//
DELIMITER ;


DELIMITER //
CREATE TRIGGER Actualizar_Estadisticas AFTER INSERT ON Libros
FOR EACH ROW
BEGIN
-- Declaro Variables
DECLARE v_hay_registros INT DEFAULT 1; condicional
DECLARE v_genero VARCHAR(20);
DECLARE v_cantidad INT;
DECLARE v_precio FLOAT;
-- Declaramos Cursor
DECLARE c_Estadisticas CURSOR FOR
SELECT genero, COUNT(genero) AS total_libros, AVG(precio) AS
precio_medio FROM Libros
GROUP BY genero;
-- Asignamos valor Controlador de registros
DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_hay_registros = 0;-- SI no hay registros el bucle se detiene y la variable cambia a 0
-- Borramos contenido tabla Estadisticas
DELETE FROM Estadisticas;
-- Abrimos Cursor
OPEN c_Estadisticas;
-- Iniciamos Ciclo
REPEAT
FETCH c_Estadisticas INTO v_genero, v_cantidad, v_precio;
IF v_hay_registros = 1 THEN
INSERT INTO Estadisticas (Genero, total_libros, precio_medio)
VALUES (v_genero, v_cantidad, v_precio);
END IF;
UNTIL v_hay_registros = 0 END REPEAT;
END;
//
DELIMITER ;


DELIMITER //
CREATE TRIGGER delete_libros AFTER DELETE ON Libros
FOR EACH ROW
BEGIN
    DECLARE v_hay_registros INT DEFAULT 1; 
    DECLARE v_genero VARCHAR(20);
    DECLARE v_cantidad INT;
    DECLARE v_precio FLOAT;
    DECLARE v_libro VARCHAR(10);

    DECLARE c_Estadisticas CURSOR FOR
    SELECT isbn AS idEstadisticas,genero, COUNT(genero) AS total_libros, AVG(precio) AS
    precio_medio FROM Libros
    GROUP BY genero;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_hay_registros = 0;

    OPEN c_Estadisticas;
    REPEAT
    FETCH c_Estadisticas INTO v_libro,v_genero, v_cantidad, v_precio;
    IF v_hay_registros = 1 THEN
        UPDATE Estadisticas SET Genero = v_genero, total_libros =          v_cantidad, precio_medio = v_precio
        WHERE idEstadisticas = v_libro;
    END IF;
    UNTIL v_hay_registros = 0 END REPEAT;
    END;
    //
DELIMITER ;