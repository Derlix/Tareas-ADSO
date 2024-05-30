#2 mayor y menor

lista2 = [10,5,20]

mayor = lista2[0]
menor = lista2[0]
for numero in lista2:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

mensajeInicial = "Ejercicio mayor y menor numero de una lista \n"
with open('C:/Users/arias/Desktop/MayorYmenor.txt','a+') as archivo1:
    archivo1.write(mensajeInicial)
    archivo1.write("\n Para saber que un numero es mayor en una lista debes comparar su posicion con las demas")
    archivo1.write("\n Lista: ")
    for lista in lista2:
        listaMostrar = str(lista)
        archivo1.write(f"[ {listaMostrar} ], ")
    Mayor = str(mayor)
    archivo1.write(f"\n El numero mayor de esa lista es:{Mayor} ")
    Menor = str(menor)
    archivo1.write(f"\n El numero menor de esa lista es:{Menor} ")



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

