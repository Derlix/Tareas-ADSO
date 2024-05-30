import mysql.connector
import manejarDB as DB
from tabulate import tabulate

conexion_db = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password = "",
    database ="zoo"
)

def ingresar_Animal(id_zoo, especie, nombre_mascota, alimentacion, habitad, pais_origen,conexionDB):
    cursor = conexionDB.cursor()
    # Generar la consulta:
    query ="""
    INSERT INTO animales (id_zoo, especie, nombre_mascota_animal, alimentacion, habitad, pais_origen)
    VALUES (%s,%s,%s,%s,%s,%s)
    """
    valores = (id_zoo,especie,nombre_mascota,alimentacion,habitad,pais_origen)
    cursor.execute(query,valores)
    conexionDB.commit()
    cursor.close()

def mostrar_zoo(conexionDB):
    cursor = conexionDB.cursor()
    
    query = """
        SELECT id_zoo AS Zoologico_ID, nombre_zoo AS Nombre_del_Zoologico FROM zoologico 
    """
    
    cursor.execute(query)
    zoologicos = cursor.fetchall()

    column_names = [desc[0] for desc in cursor.description]
    

    print(tabulate(zoologicos, headers=column_names, tablefmt='pretty'))

    cursor.close()
    
def mostrar_animal(id_zoo, conexionDB):
    cursor = conexionDB.cursor()
    
    query = """
        SELECT id_animal AS Identificador, nombre_mascota_animal AS Nombre, especie 
        FROM animales
        INNER JOIN zoologico ON animales.id_zoo = zoologico.id_zoo
        WHERE animales.id_zoo = %s
    """
    cursor.execute(query, (id_zoo,))
    animales = cursor.fetchall()
    
    colum_names = [desc[0] for desc in cursor.description]
    print(tabulate(animales, headers=colum_names, tablefmt='pretty'))
    
    cursor.close()

def eliminarAnimal(id_animal,id_zoo,conexionDB):
    cursor = conexionDB.cursor()
    
    query = """
        DELETE FROM animales WHERE id_animal = %s AND id_zoo = %s
    """
    identificadores = (id_animal,id_zoo)
    
    cursor.execute(query,identificadores)
    
    conexionDB.commit()
    
    conexionDB.close()
    cursor.close()
    
def actualizar_animal(id_zooAct, id_animalAct, nuevaEspecie, NuevoNombre, NuevaAlimentacion, NuevoHabitad, NuevoPais, conexionDB):
    cursor = conexionDB.cursor()
    
    query = """
        UPDATE animales 
        SET especie = %s, nombre_mascota_animal = %s, alimentacion = %s, habitad = %s, pais_origen = %s 
        WHERE id_animal = %s AND id_zoo = %s
    """
    datos_update = (nuevaEspecie, NuevoNombre, NuevaAlimentacion, NuevoHabitad, NuevoPais, id_animalAct, id_zooAct)
    cursor.execute(query, datos_update)
    conexionDB.commit()
    cursor.close()

def mostrar_animales(conexionDB):
    cursor = conexionDB.cursor()
    
    query= """
        SELECT * FROM animales
    """
    
    cursor.execute(query)
    animales = cursor.fetchall()
    
    colum_names = [desc[0] for desc in cursor.description]
    print(tabulate(animales, headers=colum_names, tablefmt='pretty'))
    
    cursor.close()
    
    
conexion_db.close()