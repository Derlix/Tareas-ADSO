from tabulate import tabulate
class Visitante:
    """Clase que representa un visitante del zoológico."""

    def __init__(self, id_visitante, nombre_visitante, veces_visitadas, animales_visitados, activo):
        self._id_visitante = id_visitante
        self._nombre_visitante = nombre_visitante
        self._veces_visitadas = veces_visitadas
        self._animales_visitados = animales_visitados
        self._activo = activo

    @property
    def id_visitante(self):
        return self._id_visitante

    @property
    def nombre_visitante(self):
        return self._nombre_visitante

    @property
    def veces_visitadas(self):
        return self._veces_visitadas

    @property
    def animales_visitados(self):
        return self._animales_visitados

    @property
    def activo(self):
        return self._activo

    @nombre_visitante.setter
    def nombre_visitante(self, valor):
        self._nombre_visitante = valor

    @veces_visitadas.setter
    def veces_visitadas(self, valor):
        if valor >= 0:
            self._veces_visitadas = valor
        else:
            raise ValueError("El número de veces visitadas debe ser un número positivo")

    @animales_visitados.setter
    def animales_visitados(self, valor):
        self._animales_visitados = valor

    @activo.setter
    def activo(self, estado):
        if estado in [0, 1]:
            self._activo = estado
        else:
            raise ValueError("El estado debe ser 0 (inactivo) o 1 (activo)")

    def to_dict(self):
        return {
            'id_visitante': self._id_visitante,
            'nombre_visitante': self._nombre_visitante,
            'veces_visitadas': self._veces_visitadas,
            'animales_visitados': self._animales_visitados,
            'activo': self._activo
        }

    def __str__(self):
        return f"Visitante(ID: {self._id_visitante}, Nombre: {self._nombre_visitante}, Veces Visitadas: {self._veces_visitadas}, Animales Visitados: {self._animales_visitados}, Activo: {self._activo})"

    @staticmethod
    def ingresar_visitante(conexionDB, nombre_visitante, veces_visitadas, animales_visitados, activo):
        cursor = conexionDB.cursor()
        query = """
            INSERT INTO visitantes (nombre_visitante, veces_visitadas, animales_visitados, activo)
            VALUES (%s, %s, %s, %s)
        """
        valores = (nombre_visitante, veces_visitadas, animales_visitados, activo)
        cursor.execute(query, valores)
        conexionDB.commit()
        cursor.close()

    @staticmethod
    def mostrar_visitantes(conexionDB):
        cursor = conexionDB.cursor()
        query = """
            SELECT id_visitante AS Identificador, nombre_visitante AS Nombre, veces_visitadas AS Veces_Visitadas, animales_visitados AS Animales_Visitados, activo AS Activo
            FROM visitantes
        """
        cursor.execute(query)
        visitantes = cursor.fetchall()
        colum_names = [desc[0] for desc in cursor.description]
        print(tabulate(visitantes, headers=colum_names, tablefmt='pretty'))
        cursor.close()

    @staticmethod
    def actualizar_visitante(conexionDB, id_visitante, nuevo_nombre, nuevas_veces, nuevos_animales, nuevo_activo):
        cursor = conexionDB.cursor()
        query = """
            UPDATE visitantes 
            SET nombre_visitante = %s, veces_visitadas = %s, animales_visitados = %s, activo = %s
            WHERE id_visitante = %s
        """
        datos_update = (nuevo_nombre, nuevas_veces, nuevos_animales, nuevo_activo, id_visitante)
        cursor.execute(query, datos_update)
        conexionDB.commit()
        cursor.close()

    @staticmethod
    def eliminar_visitante(conexionDB, id_visitante):
        cursor = conexionDB.cursor()
        query = """
            DELETE FROM visitantes WHERE id_visitante = %s
        """
        cursor.execute(query, (id_visitante,))
        conexionDB.commit()
        cursor.close()
