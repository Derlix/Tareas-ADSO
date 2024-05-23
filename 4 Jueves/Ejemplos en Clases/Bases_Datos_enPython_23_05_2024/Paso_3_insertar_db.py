"""Libreria Mysql"""
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
INSERT INTO cursos (nombre_asignatura,horario,id_estudiante)VALUES (%s,%s,%s)
"""
#Datos que insertaremos
cod = [2670586,14422,255445,394242]
nombreAsign = ["ADSO","ADSI","Peluqueria","Potaxio"]
horario = ["mañana","Diurno","nocturna","mixto"]
id_estudiante = [5,7,4,3]

#For para insertar los datos anteriores a la DB 
for i in range (len(nombreAsign)):
    datos_curso = ( nombreAsign[i],horario[i],id_estudiante[i])

    cursor.execute(query, datos_curso)

#Ejectuar la consultas
cursor.execute(query,datos_curso)

#Actualizar la db:
conexion_db.commit()