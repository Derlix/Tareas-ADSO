"""Libreria SQL"""
import mysql.connector

conexion_db = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password = "",
    database ="db_jueves"
)
#Crear un cursor:
cursor = conexion_db.cursor()

#Consulta el query/consulta:
query ="""
SELECT * FROM estudiantes
"""

#Ejecutar la consulta:
cursor.execute(query)

#empaqeta los datos de la consulta en una tupla:
estudiantes = cursor.fetchall()
print("*"*70 )
print("Informacion ontenida con Select a la tala estudiantes \n")
print(estudiantes)

for estudiante in estudiantes:
    print("\n")
    print("|------------------|")
    print("|Tabla Estudiantes |")
    print("|------------------|")
    print(f"|id = {estudiante[0]}")
    print(f"|Nombre = {estudiante[1]}")
    print(f"|Apellidos = {estudiante[2]}")
    print(f"|Correo = {estudiante[3]}")
    print("|------------------|")