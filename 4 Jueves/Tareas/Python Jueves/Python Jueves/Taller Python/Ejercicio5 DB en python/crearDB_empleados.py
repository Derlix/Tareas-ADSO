import mysql.connector

conexion_db = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password = ""
)

cursor = conexion_db.cursor()

db_query = "CREATE DATABASE empleados_Departamentos"

cursor.execute(db_query)

cursor.close()
conexion_db.close()