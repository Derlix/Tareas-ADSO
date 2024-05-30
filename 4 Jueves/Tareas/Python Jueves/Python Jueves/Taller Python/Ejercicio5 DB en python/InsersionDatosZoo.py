import mysql.connector

# Conexión a la base de datos
conexion_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="empleados_Departamentos"
)

# Crear un cursor
cursor = conexion_db.cursor()

#Consulta para insertar departamentos
query = """
    INSERT INTO departamentos (nombre_departamento) VALUES (%s)
"""

# Datos que insertaremos
nombre_departamento = ['software', 'ingenieria', 'recursos humanos', 'relaciones internacionales']

# Insertar los datos en la tabla departamentos
for nombre in nombre_departamento:
    cursor.execute(query, (nombre,))

# Consulta para insertar empleados
query2 = """
INSERT INTO empleados (id_departamento, nombre, apellidos, cedula, correo, genero) VALUES (%s, %s, %s, %s, %s, %s)
"""

# Datos que insertaremos
id_departamento = [1, 2, 3, 4, 1, 1, 1, 1, 2, 2, 3, 4, 4]
nombre = ['Juanito', 'Rafa', 'Pepe', 'Juan', 'Pancrasia', 'Juanita', 'Panchito', 'Lilia', 'Juliana', 'Rias', 'Luciana', 'Panchita', 'Potatito']
apellidos = ['Juancho', 'Lopez', 'Arias', 'Loaiza', 'Lolita', 'Arias', 'Cervantes', 'Kindio', 'Gremory', 'Jimenez', 'Loaiza', 'Papa','potario']
cedula = ['1231244', '1882933', '2043444', '29384', '929394', '2949855', '29949494', '1240053', '109583333', '129402221', '1028442', '10242', '13943032']
correo = ['Juanito@.com', 'Rafa@.com', 'Pepe@.com', 'Juan@.co', 'pancracio@G.com', 'juanita_@.com', 'pancho@gmail.com', 'lilia@.com', 'Juliana@.com', 'Rias@gmail.com', 'luciana@gmail.com', 'pancha@.com', 'potaru@.com']
genero = ['Masculino', 'Masculino', 'Masculino', 'Masculino', 'Femenino', 'Femenino', 'Masculino', 'Femenino', 'Femenino', 'Femenino', 'Femenino', 'Femenino', 'Masculino']

# Insertar los datos en la tabla empleados
for i in range(len(id_departamento)):
    datos_empleados = (id_departamento[i], nombre[i], apellidos[i], cedula[i], correo[i], genero[i])
    cursor.execute(query2, datos_empleados,)

# Actualizar la base de datos
conexion_db.commit()

# Cerrar el cursor y la conexión
cursor.close()
conexion_db.close()
