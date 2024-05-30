"""Libreria Mysql"""
import mysql.connector

conexion_db = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password = "",
    database ="zoo"
)

#Crear un cursor:
cursor = conexion_db.cursor()

# Generar la consulta:
query ="""
INSERT INTO zoologico (nombre_zoo,limite_animales,limite_visitantes,estado_zoo)VALUES (%s,%s,%s,%s)
"""
#Datos que insertaremos
nombre_zoo = ["Henry Doorly Zoo","Zoologico de San Diego","Loro parque","Zoologico San Luis"]
limite_animales = [100,30,40,60]
limite_visitantes = [50,15,20,30]
estado_zoo = ['Abierto','En_mantenimiento','Cerrado','Cerrado']


#For para insertar los datos anteriores a la DB 
for i in range (len(nombre_zoo)):
    datos_zoo = ( nombre_zoo[i],limite_animales[i],limite_visitantes[i],estado_zoo[i])

    cursor.execute(query, datos_zoo)
    
    
query2 ="""
INSERT INTO animales (id_zoo,especie,nombre_mascota_animal,alimentacion,habitad,pais_origen)VALUES (%s,%s,%s,%s,%s,%s)
"""
#Datos que insertaremos
id_zoo = [1,1,2,4]
especie = ['Leon','Jirafa','Cebra','Oso']
nombre_mascota_animal = ['Panchito','Rafita','Rayitas','Papucho']
alimentacion = ['Carnivoro','Omnivoro','Omnivoro','Carnivoro']
habitad = ['Caluroso','Caluroso','Sabana','Bosque']
pais_origen = ['Amazonas','Africa','Desconocido','Bosque los andes']



#For para insertar los datos anteriores a la DB 
for i in range (len(id_zoo)):
    datos_animales = ( id_zoo[i],especie[i],nombre_mascota_animal[i],alimentacion[i],habitad[i],pais_origen[i])

    cursor.execute(query2, datos_animales)

query3 = """
    INSERT INTO visitantes (id_zoo,nombre_visitante,zoo_visitados_cantidad,estado) VALUES (%s,%s,%s,%s)
""" 

id_zoVisitante = [3,1,1,2]
nombre_visitante = ['Chris Arias','Helena moyano','Como fue','Que de papel cambie']
zoo_visitados =[1,2,1,4]
estado = [1,1,0,1]
for i in range (len(id_zoVisitante)):
    datos_visitantes = (id_zoVisitante[i],nombre_visitante[i],zoo_visitados[i],estado[i])
    
    cursor.execute(query3,datos_visitantes)
    

#Ejectuar la consultas
cursor.execute(query,datos_zoo)
cursor.execute(query2,datos_animales)
cursor.execute(query3,datos_visitantes)

#Actualizar la db:
conexion_db.commit()