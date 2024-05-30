lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print(lista)

resultado = 0
#Sumar en cada iteracion 
for i in range(len(lista)):
    resultado = lista[i] + resultado

print(resultado)

#2 mayor y menor

lista2 = [10,5,20]

mayor = lista2[0]
menor = lista2[0]
for numero in lista2:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

print(f"Numero mayor{mayor}")

print(f"Numero menor{menor}")

# 3 cadena de caractares

lista3 = ['abc','xyz','aba','1221']
posicionI = 0
posicionF = -1
contador = 0

for iterador in lista3:
    if iterador[posicionI]== iterador[posicionF]:
        contador+= 1

        
print(contador)
lista3 = ['abc', 'xyz', 'aba']
print(lista3[1][-1],lista3[1][0]) 

#4 Remover elementos duplicados de una lista

lista4 = [1, 1, 2, 3, 4, 5, 6, 5]
print("Lista original:", lista4)

i = 0
while i < len(lista4):
    j = 0
    while j < len(lista4):
        if i != j and lista4[i] == lista4[j]:
            lista4.pop(j)
        else:
            j += 1
    i += 1

print("Lista sin duplicados:", lista4)

#5 Retornar Verdadero si su ambas tienen algo en conmun

listaP = [1, 2, 3, 4, 5, 16]
listaS = ['s', 'f', 'p', 16]

encontrado = False  
for elementoP in listaP:
    for elementoS in listaS:
        if elementoP == elementoS:
            encontrado = True
            print(True)  
            break 
    if encontrado:
        break  

if not encontrado:
    print(False)  


diccionario = {'manzana': 2, 'banana': 3, 'cereza': 1}

# Convertir el diccionario en una lista de tuplas (clave, valor)
lista_de_tuplas = list(diccionario.items())

# Algoritmo de seleccion para ordenar la lista de tuplas por el valor
for i in range(len(lista_de_tuplas)):
    min_idx = i
    for j in range(i+1, len(lista_de_tuplas)):
        if lista_de_tuplas[min_idx][1] > lista_de_tuplas[j][1]:
            min_idx = j
    # Intercambiar la tupla con el mínimo encontrado
    lista_de_tuplas[i], lista_de_tuplas[min_idx] = lista_de_tuplas[min_idx], lista_de_tuplas[i]

# Convertir la lista ordenada de nuevo a un diccionario
diccionario_ordenado = dict(lista_de_tuplas)

print(diccionario_ordenado)


diccionario1 = {'a': 1, 'b': 2}
diccionario2 = {'b': 3, 'c': 4}
diccionario3 = {'d': 5, 'e': 6}

diccionario_final ={}

for gran_diccionario in (diccionario1,diccionario2,diccionario3):
    
    for clave, valor in gran_diccionario.items():
        diccionario_final [clave]= valor 
    
    
print(diccionario_final)


diccionario_vacio = {}

multiplo = 1
multiplicador = 1
i = 0
for i in range(1,6):
    
   
        diccionario_vacio[i] = i * i
         
print(diccionario_vacio)

# Ordenar diccionario
diccionariodesd = {'b': 2, 'c': 3, 'a': 1}
claves1 = list(diccionariodesd.keys())

print(claves1)


for pasada in range(len(claves1) - 1):
    for i in range(len(claves1) - 1 - pasada):
        if claves1[i] > claves1[i + 1]:

            claves1[i], claves1[i + 1] = claves1[i + 1], claves1[i]

print(claves1)


diccionarioorder = {}
for clave in claves1:
    diccionarioorder[clave] = diccionariodesd[clave]

print("Diccionario ordenao:", diccionarioorder)

#diccionario suma iguales

# Diccionarios originales
dicionarioPrimero = {'a': 3, 'b': 5}
diccionarioSegundo = {'a': 7, 'c': 9}

# Diccionario para almacenar la suma
sumaDict = {}

# Sumar valores del primer diccionario
for clave in dicionarioPrimero:
    if clave in sumaDict:
        sumaDict[clave] += dicionarioPrimero[clave]
    else:
        sumaDict[clave] = dicionarioPrimero[clave]

# Sumar valores del segundo diccionario
for clave in diccionarioSegundo:
    if clave in sumaDict:
        sumaDict[clave] += diccionarioSegundo[clave]
    else:
        sumaDict[clave] = diccionarioSegundo[clave]

# Imprimir el diccionario resultante
print("Diccionario con sumas:", sumaDict)
