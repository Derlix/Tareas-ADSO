import mis_librerias.matematica as calculos
 
numero_1 = int(input("Ingresa numero 1: "))
numero_2 = int(input("Ingresa numero 2: "))

suma = calculos.suma(numero_1,numero_2)

calculos.guardarResultados("suma",numero_1,numero_2,suma)

print("-"*180)

div = calculos.division(numero_1,numero_2)

print(f"La division es {div}")

calculos.guardarResultados("division",numero_1,numero_2,div)

multiplicacion = calculos.multiplicacion(numero_1,numero_2)
calculos.guardarResultados("multiplicacion",numero_1,numero_2,multiplicacion)