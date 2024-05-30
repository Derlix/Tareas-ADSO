#num1 = int(input("Ingrese un número 1: "))
#num2 = int(input("Ingrese un número 2: "))




#suma = num1 + num2

#print(suma)

saludo = "hola"
print("saludo 1 es igual a",saludo[0])

#Impresion con formato:
print(f"saludo con formato es{saludo}")

# Usando Funciones basicas de string:

# 1. Find:
v1 = saludo.find("a")
print(F"Usando la funciona del metodo find con la variable string saludo ={v1}")

# 2. capitalize:
print("\n saludo.capitalize()")
print(saludo.capitalize())

#3. split

texto = "Hoy hace mucho calor"
visiodivision_texto = texto.split(" ")
print(f"Texto original{texto}")

print(f"Division texto = {visiodivision_texto}" )
print(visiodivision_texto[0][1])