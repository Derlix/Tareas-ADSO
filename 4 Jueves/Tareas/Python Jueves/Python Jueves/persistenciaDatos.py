#Guardar iformacion para que no se borre cuando apaga el equipo

#1er Opcion:
nombres = ["Juan ","pepito","juanito"]

archivo = open("Nombres.txt",'a')

mensahe = " \n Los nombres en la lista son: \n" + nombres[0] +"\n"+ nombres[1] +"\n"+ nombres[2]

archivo.write(mensahe)
archivo.close()


#2da Opcion:

with open("Nombres_2.txt",'a+') as archivo2:
    for nombre in nombres:
        mensaje = " \n Hola, "+ nombre + "Bienvenido a Piton"
        archivo2.write(mensaje)

#Leer informacion de un archivo:
with open("Nombres_2.txt",'r') as archivo3:
    datos = archivo3.read()
    print(datos)

#Ejemplo 1:

mascotas = [
    {
        'nombre':'copito',
        'tipo': 'gato',
        'raza': 'N/A',
        'edad': 6,
    },
    {
        'nombre':'toby',
        'tipo':'perro',
        'raza':'pomerania',
        'edad':18,

    },
    {
        'nombre':'Diomedez',
        'tipo':'Loro',
        'raza':'N/A',
        'edad':20

    },
    {
        'nombre':'juanita',
        'tipo':'conejo',
        'raza':'N/A',
        'edad':24

    },
]

mensage_inicial = "Base de datos para mascota \n "

with open('C:/Users/arias/Desktop/Mascotas.txt','a+') as archivo4:
    archivo4.write(mensage_inicial)
    for dict in mascotas:
        nombre = dict['nombre']
        tipo  = dict['tipo']
        raza = dict['raza']
        edad = str(dict['edad'])
        mensage_Temporal = "\tNombre mascota " + nombre + " \n "+ "\ttipo masctoa: "+ tipo + " \n "+ "\traza masctoa: "+ raza + " \n "  + "\tedad masctoa: "+ edad + " \n "
        archivo4.write(mensage_Temporal)
