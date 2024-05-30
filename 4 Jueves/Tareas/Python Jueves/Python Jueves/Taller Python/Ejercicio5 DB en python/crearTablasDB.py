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
    database ="empleados_Departamentos"

)


#Creamos una tabla en la base de datos:
query1 = """CREATE TABLE departamentos(
    id_departamento INT AUTO_INCREMENT PRIMARY KEY,
    nombre_departamento VARCHAR(165)
    )"""



query2 = """CREATE TABLE empleados(
    id_empleado INT AUTO_INCREMENT PRIMARY KEY,
    id_departamento INT,
    nombre VARCHAR(50),
    apellidos VARCHAR(50),
    cedula VARCHAR(265),
    correo VARCHAR(150),
    genero ENUM('Masculino','Femenino'),
    FOREIGN KEY (id_departamento) REFERENCES departamentos(id_departamento)
)"""



#Crear un cursor:
cursor = conexion_db.cursor()

#Ejectuar el query
cursor.execute(query1)
cursor.execute(query2)

#Actualizando cambios en la base de datos:
#confirmacion de la base de datos con respecto 
# a los cambios realizados por un usuario o una aplicación en la base de datos.
            #↓↓↓
conexion_db.commit()

#Cierra la conexion
cursor.close()
conexion_db.close()
