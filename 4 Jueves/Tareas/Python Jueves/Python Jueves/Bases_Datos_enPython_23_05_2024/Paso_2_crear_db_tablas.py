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
    database ="db_jueves"

)


#Creamos una tabla en la base de datos:
# query = """CREATE TABLE estudiantes(
    # id INT AUTO_INCREMENT PRIMARY KEY,
    # nombre VARCHAR(65),
    # apellido VARCHAR(50),
    # correo VARCHAR(100)
# )"""

query = """CREATE TABLE cursos(
    cod_asignatura INT AUTO_INCREMENT PRIMARY KEY,
    nombre_asignatura VARCHAR(65),
    horario VARCHAR(50),
    id_estudiante INT,
    FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id)
    )"""

#Crear un cursor:
cursor = conexion_db.cursor()

#Ejectuar el query
cursor.execute(query)

#Actualizando cambios en la base de datos:
#confirmacion de la base de datos con respecto 
# a los cambios realizados por un usuario o una aplicación en la base de datos.
            #↓↓↓
conexion_db.commit()

#Cierra la conexion
cursor.close()
conexion_db.close()
