#Diccionarios:

dic1 = {"llave_1":1,"llave_2":30,"llave_3":"Hola mundo"}

#print(type(dic1))

#print(dic1)
print(dic1['llave_1'])

#metodo get:
print(dic1.get(20," Estas loco eso no existe"))

#añadiendo info al diccionario
dic1 = {500:'contraseña'}
print('+',64)
print("Diccionar actualizado es",dic1)


#metodo update meotod que actualiza
dic1.update({'nueva_llave':1000})
print(dic1)
dic1.update({'nueva_llave':2000})
print(dic1)



dic2 = {'nombres':["juan","carlos","sofia", "susana"],
        'apellidos:':["pena","rodriguez","herrera","castro"],
        'nota_final':[3.8, 4, 5, 3.5]
        }

print(dic2)

dic2.update({'nombres':"pepe", 'apellido': "solano",'nota_final':4})

print(dic2)