import datetime

a = 3
print(type(a)) 
#print(dir(a))

new = dict()
new = {'pepe':1,2:3}
print(new  )


def saludo(nombre):
    print("Hola",nombre)

saludo(" Juanito ")

numeros = [10, 21, 4, 45, 66, 93]

Problema : 1
#Para que un numero sea par debe ser divisible entre 2 y nos debe dejar un 0 de lo contrario sera un numero impar
for i in range(len(numeros)):
    if (numeros[i] % 2 == 0):
        print(f"Par: {numeros[i]}")
    else:
        print(f"Impar:{numeros[i]}")

for numero in numeros:
    if numero % 2 == 0:
        print(f"Par: {numero}")
    else:
        print(f"Impar: {numero}")

Problema : 2
#inicialisamos la lista
precios = {'manzana': 10, 'banana': 5, 'cereza': 7}

#agregamos un nuevo producto
precios['Pera'] = 15

#imprimimos
print(f"Productos{precios}")

# inicializamos el diccionario
precios = {'manzana': 10, 'banana': 5, 'cereza': 7}

# agregamos un nuevo producto
precios['pera'] = 15  # Usualmente las claves en diccionarios son consistentes en mayúsculas y minúsculas

# imprimimos
print("Productos y precios:", precios)


inventario = [
    {'nombre': 'manzana', 'stock': 30},
    {'nombre': 'banana', 'stock': 45},
    {'nombre': 'cereza', 'stock': 20}
]

for i in range(len(inventario)):
    inventario[i]['stock'] += 10

print(f"Inventario: {inventario}")