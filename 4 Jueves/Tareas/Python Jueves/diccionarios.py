# Método útiles para trabajar con diccionarios:

colores = { "amarillo": 1, "azul": 2, "verde": 3}

# MÉTODO GET:
# Busca un elemento a partir de su clave y si no lo encuentra devuelve un valor por defecto.
print("*"*64)
print("Método get():")

encontrar_color = colores.get("negro", "Color no encontrado en diccionario colores")
print(encontrar_color)

# MÉTODO KEYS:
# Genera una lista con la llave de los registros del diccionario
print("*"*64)
print("Método keys():")
print(colores.keys())

# MÉTODO VALUES:
# Genera una lista con los valores de los registros del diccionario
print("*"*64)
print("Método values():")
print(colores.values())

# MÉTODO ITEMS:
# Genera una lista con los pares (llave, valor) que contiene el diccionario
print("*"*64)
print("Método items():")
print(colores.items())

## La principal utilidad del método items es generar un elemento para itererar sobre el diccionario:
for clave, valor in colores.items():
    print(clave, valor)

# MÉTODO POP:
# Extrae un registro de un diccionario a partir de su clave y lo borra, acepta valor por defecto
print("*"*64)
print("Método pop():")
colores.pop("amarillo", "color no encontrado")
print(f"colores = {colores}")

# MÉTODO CLEAR:
# Borra el contenido del diccionario
print("*"*64)
print("Método clear():")
colores.clear()
print(f"colores = {colores}")
