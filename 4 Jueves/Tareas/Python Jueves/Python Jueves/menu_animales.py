import json
import os
opcion = 0

datos_animales = {
    'id_animal':"",
    'Nombre':"" ,
    'Especie': "",
    'Alimentacion':"",
    'Habitad':"",
    'Pais_Origen':"",
}

ruta = os.getcwd()

while opcion != 5:
    print("*--------------------------*")
    print("| 1. Ingresar datos animal |")
    print("| 2. Eliminar datos animal |")
    print("| 3. Actualizar animal     |")
    print("| 4. No se                 |")
    print("| 5. Salir                 |")
    print("*--------------------------*")
    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        print(datos_animales)

        id = input(" Ingresa su identificador ")
        nombre = input(" Ingresa el nombre del animal")
        especie = input(" Ingresa la especie del animal")
        alimentacion = input(" Ingresa su tipo de alimentacion animal (heviboro etc)")
        habitad = input(" Ingresa el habitad del animal")
        pais = input(" Ingresa el pais del que proviene el animal")
            
        datos_animales['id_animal'] = id  
        datos_animales['Nombre'] = nombre
        datos_animales ['Especie'] = especie
        datos_animales['Alimentacion'] = alimentacion
        datos_animales['Habitad'] = habitad
        datos_animales['Pais_Origen'] = pais
        
        print(datos_animales)
        
    if opcion == 5:
        print("*---------------------------*")
        print("|         SALIENDO          |")
        print("*---------------------------*")


