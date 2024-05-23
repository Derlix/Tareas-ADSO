import json
import os

class Animal:
    """Clase animal"""

    def __init__(self, id_animal, nombre, especie, alimentacion, habitad, pais_origen):
        self.id_animal = id_animal
        self.nombre = nombre
        self.especie = especie
        self.alimentacion = alimentacion
        self.habitad = habitad
        self.pais_origen = pais_origen

    def to_dict(self):
        return {
            'id_animal': self.id_animal,
            'nombre': self.nombre,
            'especie': self.especie,
            'alimentacion': self.alimentacion,
            'habitad': self.habitad,
            'pais_origen': self.pais_origen
        }

class Visitante:
    """Clase visitante"""

    def __init__(self, id_visitante, nombre_visitante, veces_visitadas, animales_visitados, activo):
        self.id_visitante = id_visitante
        self.nombre_visitante = nombre_visitante
        self.veces_visitadas = veces_visitadas
        self.animales_visitados = animales_visitados
        self.activo = activo

    def set_activo(self, estado):
        if estado in [0, 1]:
            self.activo = estado
        else:
            raise ValueError("El estado debe ser 0 o 1")

    def to_dict(self):
        return {
            'id_visitante': self.id_visitante,
            'nombre_visitante': self.nombre_visitante,
            'veces_visitadas': self.veces_visitadas,
            'animales_visitados': self.animales_visitados,
            'activo': self.activo
        }

opcion = 0
lista_animales = []
lista_visitantes = []

ruta = os.path.join(os.getcwd(), "Actividad_Mascotas")

if not os.path.exists(ruta):
    os.makedirs(ruta)

visitante_1 = Visitante('1', 'Carlos', 0, '', 1)
lista_visitantes.append(visitante_1)

def contar_visitantes_activos(visitantes):
    """Hola """
    return sum(visitante.activo for visitante in visitantes)

while opcion != 5:
    contador_visitantes = contar_visitantes_activos(lista_visitantes)
    print("*--------------------------*")
    print(f"| Visitantes activos: {contador_visitantes} ")
    print("| 1. Ingresar datos animal |")
    print("| 2. Eliminar datos animal |")
    print("| 3. Actualizar animal     |")
    print("| 4. No se                 |")
    print("| 5. Salir                 |")
    print("*--------------------------*")
    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        datos_animales = {
            'id_animal': input("Ingresa su identificador: "),
            'nombre': input("Ingresa el nombre del animal: "),
            'especie': input("Ingresa la especie del animal: "),
            'alimentacion': input("Ingresa su tipo de alimentación (herbívoro, etc.): "),
            'habitad': input("Ingresa el hábitat del animal: "),
            'pais_origen': input("Ingresa el país de origen del animal: ")
        }

        animal = Animal(**datos_animales)
        lista_animales.append(animal)

        print("Animal agregado correctamente!")

    elif opcion == 5:
        with open(os.path.join(ruta, 'animales.json'), 'w') as archivo:
            json.dump([animal.to_dict() for animal in lista_animales], archivo, indent=4)
        with open(os.path.join(ruta, 'visitantes.json'), 'w') as archivo:
            json.dump([visitante.to_dict() for visitante in lista_visitantes], archivo, indent=4)

        print("*---------------------------*")
        print("|         SALIENDO          |")
        print("*---------------------------*")
