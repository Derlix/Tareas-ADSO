from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import pymongo.errors

MONGO_TIME_OUT = 1000
cliente = MongoClient('localhost', 27017, serverSelectionTimeoutMS=MONGO_TIME_OUT)

DB = cliente["teatro_obras"]
coleccion = DB['obras']

ID_OBRA = ""
def mostrarDatos(nombre=""):
    objetoBuscar={}
    if len(nombre) != 0:
        objetoBuscar["nombre_obra"]=nombre
    try:
        tabla.delete(*tabla.get_children()) 

        obras = coleccion.find(objetoBuscar)
        for document in obras:
            # Insertamos los datos de la obra en sus respectivas columnas
            tabla.insert('', 'end', values=(document['_id'], document['nombre_obra'], str(document['participantes_limit'])))
            print(f"Obra insertada: {document['_id']}: {document['nombre_obra']} Limite: {str(document['participantes_limit'])}/")
            
            
    except pymongo.errors.ServerSelectionTimeoutError as TimeError:
        print('Tiempo excedidop' + TimeError)
    except Exception as ex:
        print(f"Error de conexion: {ex}")
    finally:
        print("Conexion finalizada")

def dobleClickTable(event):
    global ID_OBRA
    item = tabla.selection()[0]
    ID_OBRA = tabla.item(item, "values")[0]  
    documento = coleccion.find({"_id":ObjectId(ID_OBRA)})[0]
    print(documento)
    nombreObra.delete(0,END)
    nombreObra.insert(0,documento["nombre_obra"])
    limiteParticipantes.delete(0,END)
    limiteParticipantes.insert(0,documento["participantes_limit"])
    btn_crear["state"]="disabled"
    btn_editar["state"]="normal"
    btn_eliminar["state"]="normal"

def crearObra():
    if len(nombreObra.get()) != 0 and len(limiteParticipantes.get()) != 0:
        try:
            obra = {
                "nombre_obra": nombreObra.get(),
                "participantes_limit": limiteParticipantes.get()
            }
            coleccion.insert_one(obra)
            nombreObra.delete(0, END)
            limiteParticipantes.delete(0, END)
        except pymongo.errors.ConnectionFailure as error:
            print(error)
    else:
        messagebox.showinfo(message='Todos los campos son requeridos')
    mostrarDatos()

def editarObra():
    global ID_OBRA
    if len(nombreObra.get()) != 0 and len(limiteParticipantes.get()) != 0:
        try:
            idBuscar = {"_id": ObjectId(ID_OBRA)}
            nuevos_valores = {
                "nombre_obra": nombreObra.get(),
                "participantes_limit": limiteParticipantes.get()
            }
            
            coleccion.update_one(
                idBuscar,
                {"$set": nuevos_valores}
            )
            nombreObra.delete(0, END)
            limiteParticipantes.delete(0, END)
            mostrarDatos()
        except pymongo.errors.ConnectionFailure as error:
            print(error)
    else:
        messagebox.showinfo(message='Todos los campos son requeridos')
    btn_crear["state"] = "normal"
    btn_editar["state"] = "disabled"
    btn_eliminar["state"]="disabled"


def eliminarObra():
    global ID_OBRA
    try:
        idBuscar = {"_id": ObjectId(ID_OBRA)}
        coleccion.delete_one(idBuscar)
        
        nombreObra.delete(0, END)
        limiteParticipantes.delete(0, END)
        
        
    except pymongo.errors.ConnectionFailure as error:
        print(error)
    btn_crear["state"] = "normal"
    btn_editar["state"] = "disabled"
    btn_eliminar["state"]="disabled"
    mostrarDatos()
    
def buscarObra():
    mostrarDatos(buscarX_nombre.get())

ventana = Tk()
tabla = ttk.Treeview(ventana, columns=(1,2,3), show="headings")  # Añadimos tres columnas para mostrar el ID, el nombre de la obra y el límite de participantes
tabla.grid(row=1, column=0, columnspan=3)
tabla.heading('#1', text="ID")
tabla.heading('#2', text="Nombre Obra")
tabla.heading('#3', text="Limite Participantes")
tabla.bind("<Double-1>", dobleClickTable)

Label(ventana, text="Nombre Obra").grid(row=2, column=0)
nombreObra = Entry(ventana)
nombreObra.grid(row=2, column=1)
nombreObra.focus()

Label(ventana, text="Limite Participantes").grid(row=3, column=0)
limiteParticipantes = Entry(ventana)
limiteParticipantes.grid(row=3, column=1)

btn_crear = Button(ventana, text="Crear Obra", command=crearObra, bg="green", fg="white")
btn_crear.grid(row=5, columnspan=2)

btn_editar = Button(ventana,text="Editar obra",command=editarObra,bg="blue",fg="white")
btn_editar.grid(row =6,columnspan=2)
btn_editar["state"] = "disabled"

btn_eliminar = Button(ventana,text="Eliminar Obra",command=eliminarObra,bg="red",fg="white")
btn_eliminar.grid(row=7,columnspan=2)
btn_eliminar["state"] = "disabled"

Label(ventana, text="Buscar Obra").grid(row=8, column=0)
buscarX_nombre = Entry(ventana)
buscarX_nombre.grid(row=8, column=1)


btn_buscar = Button(ventana,text="Encontrar obra",command=buscarObra,bg="white")
btn_buscar.grid(row=9,columnspan=2)


ventana.title('Obras de Teatro')
mostrarDatos()
ventana.mainloop()
cliente.close()



