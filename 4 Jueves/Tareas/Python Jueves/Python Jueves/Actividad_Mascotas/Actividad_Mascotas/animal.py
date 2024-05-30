import mysql.connector
from tabulate import tabulate
class Animal:
    """Clase que representa un animal en el zoológico."""
    
    def __init__(self, id_animal, nombre, especie, alimentacion, habitad, pais_origen):
        self._id_animal = id_animal
        self._nombre = nombre
        self._especie = especie
        self._alimentacion = alimentacion
        self._habitad = habitad
        self._pais_origen = pais_origen

    @property
    def id_animal(self):
        return self._id_animal

    @property
    def nombre(self):
        return self._nombre

    @property
    def especie(self):
        return self._especie

    @property
    def alimentacion(self):
        return self._alimentacion

    @property
    def habitad(self):
        return self._habitad

    @property
    def pais_origen(self):
        return self._pais_origen

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @especie.setter
    def especie(self, valor):
        self._especie = valor

    @alimentacion.setter
    def alimentacion(self, valor):
        self._alimentacion = valor

    @habitad.setter
    def habitad(self, valor):
        self._habitad = valor

    @pais_origen.setter
    def pais_origen(self, valor):
        self._pais_origen = valor

    def to_dict(self):
        return {
            'id_animal': self._id_animal,
            'nombre': self._nombre,
            'especie': self._especie,
            'alimentacion': self._alimentacion,
            'habitad': self._habitad,
            'pais_origen': self._pais_origen
        }

    def __str__(self):
        return f"Animal(ID: {self._id_animal}, Nombre: {self._nombre}, Especie: {self._especie}, Alimentación: {self._alimentacion}, Hábitat: {self._habitad}, País de Origen: {self._pais_origen})"

    @staticmethod
    def ingresar_animal(conexionDB, id_zoo, especie, nombre_mascota, alimentacion, habitad, pais_origen):
        cursor = conexionDB.cursor()
        query = """
            INSERT INTO animales (id_zoo, especie, nombre_mascota_animal, alimentacion, habitad, pais_origen)
            VALUES (%s,%s,%s,%s,%s,%s)
        """
        valores = (id_zoo, especie, nombre_mascota, alimentacion, habitad, pais_origen)
        cursor.execute(query, valores)
        conexionDB.commit()
        cursor.close()

    @staticmethod
    def mostrar_animales(conexionDB):
        cursor = conexionDB.cursor()
        query = """
            SELECT id_animal AS Identificador, nombre_mascota_animal AS Nombre, especie, alimentacion, habitad, pais_origen 
            FROM animales
        """
        cursor.execute(query)
        animales = cursor.fetchall()
        colum_names = [desc[0] for desc in cursor.description]
        print(tabulate(animales, headers=colum_names, tablefmt='pretty'))
        cursor.close()

    @staticmethod
    def actualizar_animal(conexionDB, id_animal, nueva_especie, nuevo_nombre, nueva_alimentacion, nuevo_habitad, nuevo_pais):
        cursor = conexionDB.cursor()
        query = """
            UPDATE animales 
            SET especie = %s, nombre_mascota_animal = %s, alimentacion = %s, habitad = %s, pais_origen = %s 
            WHERE id_animal = %s
        """
        datos_update = (nueva_especie, nuevo_nombre, nueva_alimentacion, nuevo_habitad, nuevo_pais, id_animal)
        cursor.execute(query, datos_update)
        conexionDB.commit()
        cursor.close()

    @staticmethod
    def eliminar_animal(conexionDB, id_animal):
        cursor = conexionDB.cursor()
        query = """
            DELETE FROM animales WHERE id_animal = %s
        """
        cursor.execute(query, (id_animal,))
        conexionDB.commit()
        cursor.close()
