import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import pymongo.errors
import manejo_Obras
from tkinter import Toplevel, messagebox, ttk

MONGO_TIME_OUT = 1000
cliente = MongoClient('mongodb+srv://Christian_Arias:mongobaby135@cluster0.uxfae4v.mongodb.net/', serverSelectionTimeoutMS=MONGO_TIME_OUT)
DB = cliente["teatro_obras"]
coleccion_actores = DB['actores']

def mostrar_actores():
    try:
        actores = list(coleccion_actores.find())
        return actores
    except pymongo.errors.ServerSelectionTimeoutError as e:
        print('Tiempo excedido: ' + str(e))
        return []
    except Exception as ex:
        print(f"Error de conexion: {ex}")
        return []

def crear_actor(nombre_actor, id_obra, nombre_obra):
    try:
        actor = {
            "nombre_actor": nombre_actor,
            "obra": {
                "_id": ObjectId(id_obra),
                "nombre_obra": nombre_obra
            }
        }
        coleccion_actores.insert_one(actor)
    except pymongo.errors.ConnectionFailure as error:
        print(error)

def editar_actor(id_actor, nombre_actor, id_obra, nombre_obra):
    try:
        id_buscar = {"_id": ObjectId(id_actor)}
        nuevos_valores = {
            "nombre_actor": nombre_actor,
            "obra": {
                "_id": ObjectId(id_obra),
                "nombre_obra": nombre_obra
            }
        }
        coleccion_actores.update_one(id_buscar, {"$set": nuevos_valores})
    except pymongo.errors.ConnectionFailure as error:
        print(error)

def eliminar_actor(id_actor):
    try:
        id_buscar = {"_id": ObjectId(id_actor)}
        coleccion_actores.delete_one(id_buscar)
    except pymongo.errors.ConnectionFailure as error:
        print(error)

def registrarActor(nombre_actor, obra_id):
    obra = manejo_Obras.coleccion.find_one({"_id": ObjectId(obra_id)})
    if obra:
        nombre_obra = obra["nombre_obra"]
        actor = {
            "nombre_actor": nombre_actor,
            "obra_id": ObjectId(obra_id),
            "obra_nombre": nombre_obra
        }
        coleccion_actores.insert_one(actor)
        manejo_Obras.registrarParticipante(obra_id)
    else:
        messagebox.showinfo(message='La obra especificada no existe')

def obtenerActores():
    return list(coleccion_actores.find())

def mostrarVentanaActores(ventana_padre, actualizarDatos):
    ventanaActores = Toplevel(ventana_padre)
    ventanaActores.title("Eliminar Actor de Obra")
    ventanaActores.geometry("650x400")

    tabla_actores = ttk.Treeview(ventanaActores, columns=(1, 2, 3), show="headings")
    tabla_actores.heading('#1', text="ID Actor")
    tabla_actores.heading('#2', text="Nombre Actor")
    tabla_actores.heading('#3', text="ID Obra")  

    actores = obtenerActores()
    for actor in actores:
        tabla_actores.insert('', 'end', values=(actor['_id'], actor['nombre_actor'], actor['obra_id']))  

    def on_double_click(event):
        item = tabla_actores.selection()[0]
        actor_id = tabla_actores.item(item, "values")[0]
        obra_id = tabla_actores.item(item, "values")[2]  
        confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar este actor?")
        if confirm:
            eliminar_actor(actor_id)
            manejo_Obras.disminuirParticipante(obra_id) 
            actualizarDatos()
            tabla_actores.delete(item)

    tabla_actores.bind("<Double-1>", on_double_click)
    tabla_actores.pack(fill='both', expand=True)

