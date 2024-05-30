import mysql.connector
from tabulate import tabulate

def ingresaDepartamentos(conexionDB, nombreDepartamento):
    cursor = conexionDB.cursor()
    query = """
        INSERT INTO departamentos (nombre_departamento) VALUES (%s)
    """
    valor = (nombreDepartamento,)
    cursor.execute(query, valor)
    conexionDB.commit()
    cursor.close()

def ingresarEmpleados(conexionDB):
    cursor = conexionDB.cursor()
    query = """
        INSERT INTO empleados (id_departamento, nombre, apellidos, cedula, correo, genero) VALUES (%s, %s, %s, %s, %s, %s)
    """
    id_departamento = int(input("Ingresa el ID del departamento al que pertenecerá el empleado: "))
    nombre = input("Ingresa el nombre del empleado: ")
    apellidos = input("Ingresa el apellido del empleado: ")
    cedula = input("Ingresa la cédula del empleado: ")
    correo = input("Ingresa el correo del empleado: ")
    genero = input("Ingresa el género del empleado (Masculino, Femenino): ")

    datosEmpleados = (id_departamento, nombre, apellidos, cedula, correo, genero)
    cursor.execute(query, datosEmpleados)
    conexionDB.commit()
    cursor.close()

def mostrarTodoslosEmpleados(conexionDB):
    cursor = conexionDB.cursor()
    query = """
        SELECT * FROM empleados
    """
    cursor.execute(query)
    resultados = cursor.fetchall()
    print(tabulate(resultados, headers=["ID Empleado", "ID Departamento", "Nombre", "Apellidos", "Cédula", "Correo", "Género"]))
    cursor.close()

def mostrarDepartamentos(conexionDB):
    cursor = conexionDB.cursor()
    query = """
        SELECT * FROM departamentos
    """
    cursor.execute(query)
    resultados = cursor.fetchall()
    print(tabulate(resultados, headers=["ID Departamento", "Nombre Departamento"]))
    cursor.close()

def mostrarEmpleadosDepartamento(departamento_id, conexionDB):
    cursor = conexionDB.cursor()
    query = """
        SELECT * FROM empleados WHERE id_departamento = %s
    """
    cursor.execute(query, (departamento_id,))
    resultados = cursor.fetchall()
    print(tabulate(resultados, headers=["ID Empleado", "ID Departamento", "Nombre", "Apellidos", "Cédula", "Correo", "Género"]))
    cursor.close()

def actualizarEmpleadoid(empleado_id, conexionDB):
    cursor = conexionDB.cursor()
    nombre = input("Ingresa el nuevo nombre del empleado: ")
    apellidos = input("Ingresa el nuevo apellido del empleado: ")
    cedula = input("Ingresa la nueva cédula del empleado: ")
    correo = input("Ingresa el nuevo correo del empleado: ")
    genero = input("Ingresa el nuevo género del empleado (Masculino, Femenino): ")

    query = """
        UPDATE empleados
        SET nombre = %s, apellidos = %s, cedula = %s, correo = %s, genero = %s
        WHERE id_empleado = %s
    """
    cursor.execute(query, (nombre, apellidos, cedula, correo, genero, empleado_id))
    conexionDB.commit()
    cursor.close()

def actualizarDepartamento(departamento_id, conexionDB):
    cursor = conexionDB.cursor()
    nombre_departamento = input("Ingresa el nuevo nombre del departamento: ")

    query = """
        UPDATE departamentos
        SET nombre_departamento = %s
        WHERE id_departamento = %s
    """
    cursor.execute(query, (nombre_departamento, departamento_id))
    conexionDB.commit()
    cursor.close()

def eliminarEmpleado(empleado_id, conexionDB):
    cursor = conexionDB.cursor()
    query = """
        DELETE FROM empleados WHERE id_empleado = %s
    """
    cursor.execute(query, (empleado_id,))
    conexionDB.commit()
    cursor.close()

def eliminarDepartamento(departamento_id, conexionDB):
    cursor = conexionDB.cursor()
    query = """
        DELETE FROM departamentos WHERE id_departamento = %s
    """
    cursor.execute(query, (departamento_id,))
    conexionDB.commit()
    cursor.close()
