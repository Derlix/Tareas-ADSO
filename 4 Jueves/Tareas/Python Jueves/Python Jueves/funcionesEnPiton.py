# Funciones:
#Bloque de codigo que puede ser reutilizable
#Caracteristicas
#1. Recibe parametros 
#2, puede tener retorno

def nombre_de_la_Funcion(parametros):
    pass

#Ejemplo

def saludar(nombre):
    print(f"Hola {nombre}, esto sirve para saludar ")

# llamamos a la funcion
nombre = " Re gay "
saludar(nombre=nombre)

# Ejemplo:

frutas = ["narangas","peras","moras",2,15,50]

def imprimir_frutas(lista_frutas):
    i = 3
    for fruta in lista_frutas:
        print(f"\n Fruta: {fruta}, Cantidad: {lista_frutas[i]}")
        i+=1
        if(i==6):
            break
imprimir_frutas(frutas)

#Ejemplo 3:

def contarVocales(palabra):
    """ Funcion para contar vocales en una palabra"""
    contador = 0
    for caracter in palabra:
        
        if(caracter in "aeiou"):
            contador +=1 
    return contador

palabra = input(" Introducir una palabra: ")

numero_voales =  contarVocales(palabra)

print(f"Cantidad de vocales {numero_voales}")

contarVocales

#Ejercicio:
#Generar una funcion que determine los numeros primos de una lista 
#aleatoria de datos 
#Guardar el resultado utilizando una funcion para guardar
#Informacion que hayamos creado

listaAleatori = [1,2,3,4,5,6,7,8,9,10]

def calcularPrimos(listaAleatoria):
    """Funcion para saber que numeros son primos"""
    nums_primos = []
    for lista in listaAleatoria:
        cont = 0
        for i in range(1,lista):
            if lista % i == 0:
                cont +=1
            elif cont > 2:
        nums_primos.append(lista)

for i in range(10):
    for j in range(10):
        if i / j:
            pass


#Ejercicio:
#Los numeros pefectos son aquellos numeros enteros
#positivos para los cuales la suma (sin incluir al mismo numer)
#de sus divisores es igual al numero evaluado
#esriba un programa usando funciones, que permita encontrar tres numeros perfectos en el conjhntos de numeros enteros N.

#Funciona que ingrese una lista 