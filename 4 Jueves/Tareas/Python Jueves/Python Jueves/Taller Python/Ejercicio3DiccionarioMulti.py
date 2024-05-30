elementos_diccionario = 7

i = 1
multiplo = 1
dicionario_vacio = {}
while i <= elementos_diccionario:
    dicionario_vacio[i] = i * multiplo 
    i += 1 
    multiplo+=1
    

print(f"Resultado Dict: {dicionario_vacio}")
