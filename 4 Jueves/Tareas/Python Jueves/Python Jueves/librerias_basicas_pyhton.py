import os 

# Obtenemos la ruta actual del directorio de trabajo
ruta = os.getcwd()
print(f"Mi ruta actual de trabajo es: {ruta}")

# Con esto creamos una nueva capeta en el directorio acutal de trabajo

os.system("mkdir directorio_rutas" ) 

#Guardamos un archiv en la nueva carpeta

with open("directorio_rutas/rutas_PC.txt","w+") as archivo:
    archivo.write(ruta)

import json

datos_cliente = {
    'id': 101,
    'nombre': "Juanito",
    'apellido':"Alvarez",
    'correo':"ja@correo.com"
}

with open("clientes.json","w") as archivo:
    json.dump(datos_cliente,archivo)