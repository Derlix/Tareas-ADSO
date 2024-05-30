import manejo_DB as DB
import mysql.connector

conexion_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="zoo"
)

class Animal:
    """Clase animal"""

    def __init__(self, id_animal, nombre, especie, alimentacion, habitad, pais_origen):
        self.id_animal = id_animal
        self.nombre = nombre
        self.especie = especie
        self.alimentacion = alimentacion
        self.habitad = habitad
        self.pais_origen = pais_origen


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


opcion = 0
lista_animales = []
lista_visitantes = []

visitante_1 = Visitante('1', 'Carlos', 0, '', 1)
visitante_2 = Visitante('2', 'pepito', 0, '', 1)
visitante_3 = Visitante('3', 'juanito', 0, '', 1)
visitante_4 = Visitante('4', 'pancracia', 0, '', 1)
visitante_5 = Visitante('5', 'panchito', 0, '', 0)
visitante_6 = Visitante('6', 'potaxio', 0, '', 1)
visitante_7 = Visitante('7', 'Carlos seven', 0, '', 1)

lista_visitantes.append(visitante_1)
lista_visitantes.append(visitante_2)
lista_visitantes.append(visitante_3)
lista_visitantes.append(visitante_4)
lista_visitantes.append(visitante_5)
lista_visitantes.append(visitante_6)
lista_visitantes.append(visitante_7)

def contar_visitantes_activos(visitantes):
    return sum(visitante.activo for visitante in visitantes)

while opcion != 5:
    contador_visitantes = contar_visitantes_activos(lista_visitantes)
    print("*--------------------------*")
    print(f"| Visitantes activos: {contador_visitantes} ")
    print("| 1. Ingresar datos animal |")
    print("| 2. Eliminar datos animal |")
    print("| 3. Actualizar animal     |")
    print("| 4. Consultar             |")
    print("| 5. Salir                 |")
    print("*--------------------------*")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        id_zoo = int(input("Ingresa a qué Zoológico va a pertenecer: "))
        especie = input("Ingresa la especie del animal: ")
        nombre = input("Ingresa el nombre del animal: ")
        alimentacion = input("Ingresa su tipo de alimentación (herbívoro, etc.): ")
        habitad = input("Ingresa el hábitat del animal: ")
        pais_origen = input("Ingresa el país de origen del animal: ")  
        
        DB.ingresar_Animal(id_zoo, especie, nombre, alimentacion, habitad, pais_origen, conexion_db)
        print("Animal agregado correctamente!")
        
    elif opcion == 2:
        DB.mostrar_zoo(conexion_db)
        identificador_zoo = int(input("Ingresa el ID (Identificador) del Zoológico al que deseas eliminar animales: "))
        
        DB.mostrar_animal(identificador_zoo, conexion_db)
        identificador_animal_delete = int(input("Ingresa el ID del animal a eliminar: "))
        
        DB.eliminarAnimal(identificador_animal_delete, identificador_zoo, conexion_db)
        print("Animal Eliminado Correctamente!")
        
    elif opcion == 3:
        DB.mostrar_zoo(conexion_db)
        id_zooAct = int(input("Ingresa el ID (Identificador) del Zoológico al que deseas actualizar un animal: "))
        DB.mostrar_animal(id_zooAct, conexion_db)
        id_animalAct = int(input("Ingresa el ID del animal a actualizar: "))
        if id_animalAct != 0:
            nuevaEspecie = input("Ingresa la nueva Especie: ")
            NuevoNombre = input("Ingresa el nuevo nombre: ")
            NuevaAlimentacion = input("Ingresa la nueva Alimentación: ")
            NuevoHabitad = input("Ingresa el nuevo hábitat: ")
            NuevoPais = input("Ingresa el nuevo país: ")
            DB.actualizar_animal(id_zooAct, id_animalAct, nuevaEspecie, NuevoNombre, NuevaAlimentacion, NuevoHabitad, NuevoPais, conexion_db)
            print("Animal Actualizado con éxito!")
        else:
            print("El ID del animal que ingresaste no existe")
    elif opcion == 4:
        print("1. Ver animales de todos los Zoológicos")
        print("2. Ver animales de un Zoológico en específico")
        print("3. Ver zoológicos")
        print("4. Ver visitantes activos")
        opcion4 = int(input("Ingresa lo que deseas ver: "))
        if opcion4 == 1:
            DB.mostrar_animales(conexion_db)
        elif opcion4 == 2:
            DB.mostrar_zoo(conexion_db)
            leer_zoo = int(input("Ingresa el Zoológico que deseas ver sus animales: "))
            DB.mostrar_animal(leer_zoo, conexion_db)
        elif opcion4 == 3:
            DB.mostrar_zoo(conexion_db)
    elif opcion == 5:
        print("*---------------------------*")
        print("|         SALIENDO          |")
        print("*---------------------------*")

conexion_db.close()
