import mysql.connector # -> Liberia mysql para trabajar en bases de datos 

conexion_db = mysql.connector.connect( 
    host = "localhost", 
    user= "root",
    password = "",
    database ="db_jueves"
)
#Crear un cursor:
cursor = conexion_db.cursor()

# Generar la consulta:
query ="""
UPDATE estudiantes SET nombre = %s,apellido=%s, correo = %s WHERE id =1
"""
datos_estudianteNuevos = ("Juanitossss", "Perezddd", "jp@correo.sscom")

#Ejectuar la consulta
cursor.execute(query,datos_estudianteNuevos)

#Actualizar la db:
conexion_db.commit()