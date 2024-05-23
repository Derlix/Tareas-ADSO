import json as jason
import os 
import datetime
lista_de_Consignaciones = []  

ruta = os.path.join(os.getcwd(), "Jueves16Mayo_Clases")

class Banco:
    """
    Clase que crea bancos
    """
    def __init__(self, nombre, direccion, dinero,  trabajadores , sucursales):
        self.nombre = nombre
        self.direccion = direccion
        self.dinero = dinero
        self.trabajadores = trabajadores
        self.sucursales = sucursales

    def invertir_bolsa(self):
        print(f"{self.dinero} esta siendo invertido 😨")

    def cobrar_intereses(self,nombre_cliente, deuda, interes):
        valor_a_pagar = deuda + (deuda*interes)

        print(f"Estimado {nombre_cliente} tu deuda es de {valor_a_pagar} del banco {self.nombre}  😥")

    def entregar_dinero(self, nombre_cliente, cantidad):
        print(f"El usuario {nombre_cliente}, retiro {cantidad} pesos 😀")


    def recibir_dinero(self, nombre_cliente, cantidadConsignar, fecha):
        listaTemporal = {
            "nombre_cliente":nombre_cliente,
            "cantidad":cantidadConsignar,
            "fecha":fecha,
        }


        # lista_de_Consignaciones.append(listaTemporal)

        
        # with open(os.path.join(ruta, 'Historial_consignaciones.json'), 'w') as archivo:
        #     jason.dump(listaTemporal, archivo, indent=4)


        try:
            with open(os.path.join(ruta, 'clientes.json'),"r") as archivo:
                clientes = archivo.load()
                clientes.append(listaTemporal)

            with open(os.path.join(ruta, 'clientes.json'),"w") as archivo:
                jason.dump(clientes,archivo,indent=4)
        except:
            clientes = [listaTemporal]
            with open(os.path.join(ruta, 'clientes.json'),"w") as archivo:
                jason.dump(clientes,archivo,indent=4)

        print(f"El suario {nombre_cliente}, consigno {cantidadConsignar} 😊")

banco1 = Banco(nombre = "DMG",direccion="Calle 20 Cra 6ta",dinero=500000000,trabajadores=50, sucursales=10)

print(f"Bienvenido al banco {banco1.nombre} 👋")

print("\n")
banco1.cobrar_intereses("Arce",100000000,0.05)
banco1.recibir_dinero(nombre_cliente="Juanito",cantidadConsignar=5000,fecha="15")

banco2 = Banco(nombre = "Adso",direccion="Calle 20 Cra 6ta",dinero=500000000,trabajadores=50, sucursales=10)

banco1.entregar_dinero("Ana Maria",2000000)

banco1.recibir_dinero(nombre_cliente="panchito",cantidadConsignar=500000,fecha="1523")

pepe = {"pepe":1}

print(pepe["pepe"])