class Usuario:
    def __init__(self, nombre, edad, email):
        self.nombre = nombre
        self.edad = edad
        self.email = email

class GestorUsuarios:
    def __init__(self):
        self.usuarios = []

    def crear_usuario(self, nombre, edad, email):
        nuevo_usuario = Usuario(nombre, edad, email)
        self.usuarios.append(nuevo_usuario)
        print(f"Usuario {nombre} creado con éxito.")

    def consultar_usuarios(self):
        print("Usuarios inscritos:")
        for usuario in self.usuarios:
            print(f"Nombre: {usuario.nombre}, Edad: {usuario.edad}, Email: {usuario.email}")

    def editar_usuario(self, nombre, nuevo_nombre=None, nueva_edad=None, nuevo_email=None):
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                if nuevo_nombre:
                    usuario.nombre = nuevo_nombre
                if nueva_edad:
                    usuario.edad = nueva_edad
                if nuevo_email:
                    usuario.email = nuevo_email
                print(f"Usuario {nombre} actualizado.")
                return
        print("Usuario no encontrado.")

    def borrar_usuario(self, nombre):
        for i, usuario in enumerate(self.usuarios):
            if usuario.nombre == nombre:
                del self.usuarios[i]
                print(f"Usuario {nombre} borrado.")
                return
        print("Usuario no encontrado.")

# Ejemplo de uso:
gestor = GestorUsuarios()
gestor.crear_usuario("Alice", 30, "alice@example.com")
gestor.consultar_usuarios()
gestor.editar_usuario("Alice", nuevo_nombre="Alicia", nueva_edad=31)
gestor.consultar_usuarios()
gestor.borrar_usuario("Alicia")
gestor.consultar_usuarios()
