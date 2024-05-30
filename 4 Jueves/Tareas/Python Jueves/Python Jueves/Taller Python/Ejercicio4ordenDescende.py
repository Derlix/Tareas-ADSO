diccionario_1 = {'Naranjas': 150, 'Manzanas': 200, 'Mangos': 40, 'Peras': 60,'Potaxio':500,'Palomitas':680}
diccionario_vacio = {}


llaves = list(diccionario_1.keys())
valores = list(diccionario_1.values())


for i in range(len(valores)):
    limite = i
    for j in range(i + 1, len(valores)):
        if valores[j] > valores[limite]:
            limite = j

    valores[i], valores[limite] = valores[limite], valores[i]
    llaves[i], llaves[limite] = llaves[limite], llaves[i]

for i in range(len(llaves)):
    diccionario_vacio[llaves[i]] = valores[i]

print(diccionario_1)
print(diccionario_vacio)