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