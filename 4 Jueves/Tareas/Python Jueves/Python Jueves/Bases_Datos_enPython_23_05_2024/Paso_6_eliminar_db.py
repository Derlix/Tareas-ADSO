import mysql.connector

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
DELETE FROM estudiantes WHERE id =%s
"""
datos_paraBorrar = (2,)

#Ejectuar la consulta
cursor.execute(query,datos_paraBorrar)

#Actualizar la db:

conexion_db.commit()

conexion_db.close()
cursor.close()