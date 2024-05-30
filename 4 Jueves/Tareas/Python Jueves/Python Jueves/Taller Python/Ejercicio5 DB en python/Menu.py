import mysql.connector
from tabulate import tabulate
import manejarDB as DB

conexion_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="empleados_departamentos"
)

opcion = 0

while opcion != 5:
    print(" *---------------------------------------*")
    print(" | 1. Ingresar Empleado o Departamento   |")
    print(" | 2. Leer                               |")
    print(" | 3. Actualizar Empleado o Departamento |")
    print(" | 4. Eliminar Empleado o Departamento   |")
    print(" | 5. Salir                              |")
    print(" *---------------------------------------*")
    opcion = int(input(" Ingresa una opcion: "))

    if opcion == 1:
        print(" ¿Que deseas ingresar?")
        print(" 1. Departamento")
        print(" 2. Empleado")
        opcionB = int(input("Ingresa una opcion: "))
        if opcionB == 1:
            nombreDepartamento = input(" Ingresa el nombre del nuevo departamento: ")
            DB.ingresaDepartamentos(conexion_db, nombreDepartamento)
        if opcionB == 2:
            DB.mostrarDepartamentos(conexion_db)
            DB.ingresarEmpleados(conexion_db)
    if opcion == 2:
        print("1. Ver todos los empleados de todos los departamentos ")
        print("2. Ver los departamentos ")
        print("3. Ver empleados de un departamento especifico ")
        opcionC = int(input(" Ingresa una opcion: "))
        if opcionC == 1:
            DB.mostrarTodoslosEmpleados(conexion_db)
        if opcionC == 2:
            DB.mostrarDepartamentos(conexion_db)
        if opcionC == 3:
            DB.mostrarDepartamentos(conexion_db)
            departamento_seleccion = int(input(" Ingresa un departamento: "))
            DB.mostrarEmpleadosDepartamento(departamento_seleccion, conexion_db)
    if opcion == 3:
        print("1. Actualizar Empleado ")
        print("2. Actualizar Departamento ")
        opcionD = int(input(" Ingresa una opcion: "))
        if opcionD == 1:
            DB.mostrarTodoslosEmpleados(conexion_db)
            seleccionarEmpleado = int(input(" Ingresa el empleado a actualizar: "))
            DB.actualizarEmpleadoid(seleccionarEmpleado, conexion_db)
        if opcionD == 2:
            DB.mostrarDepartamentos(conexion_db)
            seleccionarDepartamento = int(input(" Ingresa el departamento: "))
            DB.actualizarDepartamento(seleccionarDepartamento, conexion_db)
    if opcion == 4:
        print(" 1. Eliminar Empleado")
        print(" 2. Eliminar departamento")
        opcionE = int(input(" Ingresa una opcion: "))
        if opcionE == 1:
            DB.mostrarTodoslosEmpleados(conexion_db)
            empleadoDelete = int(input(" Selecciona un empleado: "))
            DB.eliminarEmpleado(empleadoDelete, conexion_db)
        if opcionE == 2:
            DB.mostrarDepartamentos(conexion_db)
            departamentoDelete = int(input(" Ingresa el departamento a eliminar: "))
            DB.eliminarDepartamento(departamentoDelete, conexion_db)
    if opcion == 5:
        print("*-------------------------*")
        print("|        SALIENDO....     |")
        print("+-------------------------+")
