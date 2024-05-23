# Clases

#Clase (molde) perros:

class Perro:
    """Esta clas cre instacias de perros"""

    def __init__(self, nombre, raza, edad):
        """"Constructor de la clase perro"""
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        pass

    #Metodos de las clases:

    def ladrar(self):
        print(f"el perro {self.nombre} esta ladrando 😨")

    def comer (self):
        print(f"El perro {self.nombre} esta comiendo 🥓")


class SuperPerro(Perro):

    def volar(self):
        print(f"El perro {self.nombre} esta volando 🤯")

    def telekinesis(self):
        print(f"El perro {self.nombre} te esta leyendo la mente 🧠")
    


perro2 = Perro(nombre="Egue",raza="bito",edad=16)


perro1 = Perro("","",0)
perro1.nombre = "Toby"
perro1.raza = "Criollito"
perro1.edad = 2

print(f"El perro {perro1.nombre} es de raza {perro1.raza} y tiene una edad de {perro1.edad}")
print(f"Soy {perro1.nombre}")

perro1.ladrar()
perro1.comer()


#
print("\n")
Super_perro_1 = SuperPerro(nombre="Cerebro", raza="Golden", edad=11)


Super_perro_1.volar()
Super_perro_1.ladrar()

