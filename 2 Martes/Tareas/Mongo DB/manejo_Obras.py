from tkinter import messagebox
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import pymongo.errors

MONGO_TIME_OUT = 1000
cliente = MongoClient()
DB = cliente["teatro_obras"]
coleccion = DB['obras']

def mostrar():
    try:
        obras = list(coleccion.find())
        return obras
    except pymongo.errors.ServerSelectionTimeoutError as e:
        print('Tiempo excedido: ' + str(e))
        return []
    except Exception as ex:
        print(f"Error de conexion: {ex}")
        return []

def crearObra(nombre_obra, limite_participantes):
    obra = {
        "nombre_obra": nombre_obra,
        "participantes_limit": limite_participantes,
        "participantes_count": 0  
    }
    coleccion.insert_one(obra)

def editar_obra(id_obra, nombre_obra, limite_participantes):
    try:
        id_buscar = {"_id": ObjectId(id_obra)}
        nuevos_valores = {
            "nombre_obra": nombre_obra,
            "participantes_limit": limite_participantes
        }
        coleccion.update_one(id_buscar, {"$set": nuevos_valores})
    except pymongo.errors.ConnectionFailure as error:
        print(error)

def eliminar_obra(id_obra):
    try:
        id_buscar = {"_id": ObjectId(id_obra)}
        coleccion.delete_one(id_buscar)
    except pymongo.errors.ConnectionFailure as error:
        print(error)
        
def obtenerObras():
    return list(coleccion.find())


def actualizarParticipantes(obra_id, cantidad):
    coleccion.update_one(
        {"_id": ObjectId(obra_id)},
        {"$set": {"participantes_count": cantidad}}
    )
    
def obtenerObraPorNombre(nombre):
    try:
        obra = coleccion.find_one({"nombre_obra": nombre})
        return obra
    except Exception as ex:
        print(f"Error al obtener la obra por nombre: {ex}")
        return None

# manejo_Obras.py

def registrarParticipante(obra_id):
    obra = coleccion.find_one({"_id": ObjectId(obra_id)})
    if obra:
        if obra["participantes_count"] < obra["participantes_limit"]:
            nuevo_count = obra["participantes_count"] + 1
            actualizarParticipantes(obra_id, nuevo_count)
        else:
            messagebox.showinfo(message='Se ha alcanzado el límite de participantes para esta obra.')
    else:
        messagebox.showinfo(message='La obra especificada no existe')

def disminuirParticipante(id_obra):
    try:
        obra = coleccion.find_one({"_id": ObjectId(id_obra)})
        if obra:
            participantes_count = obra["participantes_count"]
            if participantes_count > 0:
                participantes_count -= 1
                coleccion.update_one({"_id": ObjectId(id_obra)}, {"$set": {"participantes_count": participantes_count}})
    except Exception as ex:
        print(f"Error al disminuir participante: {ex}")
