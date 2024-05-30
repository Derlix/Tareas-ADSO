"""Libreria mysql"""
import mysql.connector

#Defunur conexion a la base de datos
conexion_db = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password = "",
    #Aqui ya debemos especificar que DB usaremos
            #*Nombre de tu DB*
                #↓
    database ="zoo"

)


#Creamos una tabla en la base de datos:
query1 = """CREATE TABLE zoologico(
    id_zoo INT AUTO_INCREMENT PRIMARY KEY,
    nombre_zoo VARCHAR(65),
    limite_animales INT,
    limite_visitantes INT,
    estado_zoo ENUM('Abierto','Cerrado','En_mantenimiento')
    )"""



query2 = """CREATE TABLE animales(
    id_animal INT AUTO_INCREMENT PRIMARY KEY,
    id_zoo INT,
    especie VARCHAR(50),
    nombre_mascota_animal VARCHAR(65),
    alimentacion VARCHAR(100),
    habitad VARCHAR(150),
    pais_origen VARCHAR(150),
    FOREIGN KEY (id_zoo) REFERENCES zoologico(id_zoo)
)"""


query3 = """CREATE TABLE visitantes (
    id_visitante INT AUTO_INCREMENT PRIMARY KEY,
    id_zoo INT,
    nombre_visitante VARCHAR(65),
    zoo_visitados_cantidad INT,
    estado TINYINT(1) NOT NULL,
    FOREIGN KEY (id_zoo) REFERENCES zoologico(id_zoo)
)"""

#Crear un cursor:
cursor = conexion_db.cursor()

#Ejectuar el query
cursor.execute(query1)
cursor.execute(query2)
cursor.execute(query3)

#Actualizando cambios en la base de datos:
#confirmacion de la base de datos con respecto 
# a los cambios realizados por un usuario o una aplicación en la base de datos.
            #↓↓↓
conexion_db.commit()

#Cierra la conexion
cursor.close()
conexion_db.close()
