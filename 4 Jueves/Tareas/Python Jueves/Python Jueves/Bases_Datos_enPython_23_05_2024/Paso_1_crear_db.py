"""Liberia para trabajar con Mysql con Python  """
#      ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
import mysql.connector

#Conexion a cliente de la base de datos
            #usamos este metodo  ↓
conexion_db = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password = ""
)

#Crear un cursor para intercambiar entre Python y MYSQl

cursor = conexion_db.cursor()

#Definir el Query(consulta/Operacion) que queramos realizar :

db_query = "CREATE DATABASE db_jueves"

#Este metodo ejecuta el query/consulta que definimos anteriormente:
#      ↓↓↓↓↓↓↓
cursor.execute(db_query)

#cerrar la conexion y el cursor:
cursor.close()
conexion_db.close()