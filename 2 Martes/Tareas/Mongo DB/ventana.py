from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import manejo_Obras
import manejo_Actores


def mostrarDatos(opcion=None):
    try:
        tabla.delete(*tabla.get_children())

        if opcion == "Obras_Sin_Paricipantes":
            obras = [obra for obra in manejo_Obras.obtenerObras() if obra['participantes_count'] == 0]
        elif opcion == "Obras_Con_Mas_Participantes":
            max_participantes = max(obra['participantes_count'] for obra in manejo_Obras.obtenerObras())
            obras = [obra for obra in manejo_Obras.obtenerObras() if obra['participantes_count'] == max_participantes]
        else:
            obras = manejo_Obras.obtenerObras()

        for obra in obras:
            tabla.insert('', 'end', values=(obra['_id'], obra['nombre_obra'], f"{obra['participantes_count']}/{obra['participantes_limit']}"))
    except Exception as ex:
        print(f"Error de conexion: {ex}")
    finally:
        print("Conexion finalizada")
        
def crearObra():
    if len(nombreObra.get()) != 0 and len(limiteParticipantes.get()) != 0:
        try:
            manejo_Obras.crearObra(nombreObra.get(), int(limiteParticipantes.get()))
            nombreObra.delete(0, END)
            limiteParticipantes.delete(0, END)
        except Exception as error:
            print(error)
    else:
        messagebox.showinfo(message='Todos los campos son requeridos')
    mostrarDatos()

def registrarActor():
    if len(nombreActor.get()) != 0 and len(actorObra.get()) != 0:
        try:
            obra = manejo_Obras.obtenerObraPorNombre(actorObra.get())
            if obra:
                manejo_Actores.registrarActor(nombreActor.get(), str(obra['_id']))
                nombreActor.delete(0, END)
                actorObra.delete(0, END)
            else:
                messagebox.showinfo(message='La obra especificada no existe')
        except Exception as error:
            print(error)
    else:
        messagebox.showinfo(message='Todos los campos son requeridos')
    mostrarDatos()
    
def buscarObra():
    opcion = combo_busqueda.get()
    mostrarDatos(opcion)

def mostrarVentanaActores():
    manejo_Actores.mostrarVentanaActores(ventana, mostrarDatos)

ventana = Tk()

# Estilo para la tabla
style = ttk.Style()
style.configure("Treeview", background="#f2f5f5", foreground="black", fieldbackground="#347083")
style.map("Treeview", background=[('selected', 'black',)])

tabla = ttk.Treeview(ventana, columns=(1, 2, 3), show="headings", style="Treeview")
tabla.grid(row=15, column=0, columnspan=3, sticky='nsew')
tabla.heading('#1', text="ID")
tabla.heading('#2', text="Nombre Obra")
tabla.heading('#3', text="Participantes (Actual/Limite)")

Label(ventana, text="Nombre de la Obra: ", font='BOLD').grid(row=2, column=0)
nombreObra = Entry(ventana)
nombreObra.grid(row=3, column=0)

Label(ventana, text="Limite Participantes en la obra: ", font='Arial').grid(row=4, column=0)
limiteParticipantes = Entry(ventana)
limiteParticipantes.grid(row=5, column=0)

# Crear el botón sin el argumento de estilo
btn_crear = Button(ventana, text="Crear Obra", command=crearObra, bg="green", fg="White", font="BOLD", cursor="hand2")
btn_crear.grid(row=3, rowspan=2, column=1, sticky='nsew')

Label(ventana, text="Nombre del Actor: ", font='Arial').grid(row=6, rowspan=1, column=0)
nombreActor = Entry(ventana)
nombreActor.grid(row=7, column=0)

Label(ventana, text="Nombre Obra donde actuara: ", font='Arial').grid(row=8, column=0)
actorObra = Entry(ventana)
actorObra.grid(row=9, column=0)

btn_registrar = Button(ventana, text="Registrar Actor", command=registrarActor, cursor="hand2", font="BOLD", fg="White", bg="#053bff")
btn_registrar.grid(row=7, rowspan=2, column=1, sticky='nsew')


btn_actoresTabla = Button(ventana, text="Ver tabla eliminar actor de una obra", command=mostrarVentanaActores, bg="#8c37ed", fg="White", font="BOLD", cursor="hand2")
btn_actoresTabla.grid(row=12)

ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_rowconfigure(1, weight=1)

Label(ventana, text="Consulta  ➤➤➤", font='BOLD').grid(row=11, column=0)
combo_busqueda = ttk.Combobox(ventana, values=["Obras_Sin_Paricipantes", "Obras_Con_Mas_Participantes", "Todas"])
combo_busqueda.grid(row=11, column=1, sticky='nsew')
combo_busqueda.current(0)  

btn_buscar = Button(ventana, text="Buscar Obra", command=buscarObra, bg="#4037ed", fg="White", font="BOLD", cursor="hand2")
btn_buscar.grid(row=11, column=2)

ventana.geometry("650x400")
ventana.title('Obras de Teatro')
mostrarDatos()
ventana.mainloop()
