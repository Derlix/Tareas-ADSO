DELIMITER //
CREATE FUNCTION suma_puntos (n1 INT, n2 INT) 
RETURNS INT
BEGIN
    DECLARE var_suma INT;
    SET var_suma = n1 + n2;
    RETURN var_suma;
    IF var_suma 
END;
//
DELIMITER ;


DELIMITER //
CREATE FUNCTION ganador ()

DELIMITER //
CREATE FUNCTION ganador (id INT,n1 INT, n2 INT) 
RETURNS INT
BEGIN
    DECLARE ganador INT;
    DECLARE var_suma INT;
    SET var_suma = n1 + n2;
    SET ganador = 0;


    IF ganador < var_suma THEN
        SET ganador = id;
    END IF;
    RETURN ganador_;
END;
//
DELIMITER ;


--Ejercicio, realizar una función que enviado un número, devuelva el 
--resultado de sumar sus 5 primeros múltiplos, usando ciclos.
--Ejemplo si envió por parámetros el 7
--Resultado=(7*1)+7*2)+(7*3)+(7*4)+(7*5)

DROP FUNCTION suma_multiplos;
DELIMITER //
CREATE FUNCTION suma_multiplos(numero INT) RETURNS INT
BEGIN
DECLARE contador INT DEFAULT 1;
DECLARE resultado INT DEFAULT 1;
DECLARE suma INT DEFAULT 0;
WHILE contador <=  5 DO
    SET resultado = numero * contador;
    SET suma = suma + resultado;
    SET contador = contador + 1;
END WHILE;
RETURN suma;
END;
//
DELIMITER ;





DROP FUNCTION calcularNota; 
DELIMITER // 
CREATE FUNCTION calcularNota (nota1 FLOAT, nota2 FLOAT, nota3 FLOAT) RETURNS FLOAT
    BEGIN
    DECLARE notasumada FLOAT DEFAULT 0.0;
    SET notasumada = (nota1 / 2)+(nota2 / 3 )+ (nota3 / 5);
    RETURN notasumada;
    END;
//
DELIMITER ;




DROP FUNCTION calcularNota;
DELIMITER //
CREATE FUNCTION calcularNota(nota1 FLOAT, nota2 FLOAT, nota3 FLOAT) RETURNS FLOAT
BEGIN
DECLARE suma FLOAT DEFAULT 0.0;
    SET suma = (nota1 / 2)+(nota2 / 3 )+ (nota3 / 5);
RETURN suma;
END;
//
DELIMITER ;


DELIMITER //
CREATE PROCEDURE listar_participantes ()
SELECT id_participante FROM puntos;
//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE consultarGenero (generoP CHAR)
SELECT genero, id_participante FROM puntos
WHERE genero LIKE generoP;
//
DELIMITER ;


DELIMITER //
CREATE PROCEDURE insertar_puntos(nuevo_genero CHAR(1),
                                 nuevo_puntos_1 INT,nuevo_puntos_2 INT)
    INSERT INTO puntos ( genero, competencia_1, competencia_2)
    VALUES ( nuevo_genero, nuevo_puntos_1, nuevo_puntos_2);
//
DELIMITER ;