from collections import deque
from datetime import datetime

hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Libro:
    def __init__(self, nombre, autor, isbn):
        self.nombre = nombre
        self.autor = autor
        self.isbn = isbn
        self.prestado = False
        self.prestado_a = None

    def estado(self):
        return "Disponible" if not self.prestado else f"Prestado a {self.prestado_a}"

    def info(self):
        return f"[{self.estado()}] - {self.nombre} | Autor: {self.autor} | ISBN: {self.isbn}"
    
# primer avance del proyecto

class Biblioteca:

#definimos los tipos de listas, pilas y colas que itulizaremos en el programa
    def __init__(self):
        self.libros = []  # Lista de los libros disponibles
        self.librosPrestados = deque()  # Cola de libros que son prestados
        self.librosDevueltos = []  # Pila de los libros que son devueltos

#Definimos la funcion para agregar libros
    def agregarLibro(self, nombre, autor, isbn):
        for libro in self.libros + list(self.librosPrestados):
            if libro.isbn == isbn:
                print(" \n -- El libro que intenta ingresar ya existe en la biblioteca.")# si el isbn es repetido, no permitira agregar
                print("\n" * 2)
                return
        nuevoLibro = Libro(nombre, autor, isbn)
        self.libros.append(nuevoLibro)
        print(f" \n -- El libro '{nombre}' fue agregado exitosamente a la biblioteca el '{hora}.")
        print("\n" * 2)

# Segundo avance del proyecto

#definimos la funcion prestar libros
    def prestarLibro(self, clave, persona):
        for libro in self.libros:
            if (libro.isbn.lower() == clave.lower() or libro.nombre.lower() == clave.lower()) and not libro.prestado:
                libro.prestado = True
                libro.prestado_a = persona
                self.libros.remove(libro)
                self.librosPrestados.append(libro)
                print(f"\n  -- El libro '{libro.nombre}' ha sido prestado a {persona} ' el ' {hora}.")
                print("\n" * 2)
#si el libro no se encuentra en la lista por estar prestado o mal escrito la busqueda
                return
        print("\n  -- El libro que busca no se encuentra o ya fue prestado con anterioridad.")
        print("\n" * 2)

#definimos la funcion devolver
    def devolverLibro(self, clave):
        for libro in self.librosPrestados:
            if libro.isbn.lower() == clave.lower() or libro.nombre.lower() == clave.lower():
                persona = libro.prestado_a
                libro.prestado = False
                libro.prestado_a = None
                self.librosPrestados.remove(libro)
                self.librosDevueltos.append(libro)
                self.libros.append(libro)
                print(f"\n  -- El libro '{libro.nombre}' fue devuelto el ' {hora} 'por el usuario' {persona}.")
                return
        print("\n  -- El libro que busca, no se encuentra en la biblioteca de libros prestados.")
        print("\n" * 2)

# tercer avance del proyecto

#Funcion para mostrar la biblioteca de libros
    def mostrarLaBiblioteca(self):
        print("\n  -- Los libros con los que cuenta actualmente la bliblioteca son:")
        libreria = self.libros + list(self.librosPrestados)# este atributo nos permite ver la totalidad de la biblioteca, sumando las listas de prestados y no prestados y los estados de cada libro
        if not libreria:
            print("\n  --X .ERROR. La biblioteca no cuenta con libros guardados. X--")
            print("\n" * 2)
        for libro in libreria:
            print(" -", libro.info())
            print("\n" * 2)

#Funcion para realizar la busqueda de los libros en la biblioteca, mediante cualquiera de los datos guardados con el
    def buscarLibro(self, clave):
        resultadoBusqueda = []
        for libro in self.libros + list(self.librosPrestados):#Busca los libros en cualquiera de las listas del programa
            if (clave.lower() in libro.isbn.lower() or
                clave.lower() in libro.nombre.lower() or
                clave.lower() in libro.autor.lower()):
                resultadoBusqueda.append(libro)

        if resultadoBusqueda:
            print(f"\n   -- Con los parametros dados este es el resultado para '{clave}':")
            for libro in resultadoBusqueda:
                print(" -", libro.info())
                print("\n" * 2)
        else:
            print("\n  -- No se encontraron coincidencias.")
            print("\n" * 2)

#Funcion para eliminar libros
#Para eliminar libros, se debe realizar con la informacion exacta, nombre completo o isbn exacto
    def eliminarLibro(self, clave):
        for libro in self.libros:
            if clave.lower() == libro.isbn.lower() or clave.lower() == libro.nombre.lower():
                self.libros.remove(libro)
                print(f"\n  -- El lLibro '{libro.nombre}' fue eliminado de la biblioteca el ' {hora}.")
                print("\n" * 2)
                return
        print("\n  -- No se puede eliminar este libro (no existe o se encuentra prestado).")
        print("\n" * 2)

#Funcion para Modificar libros
#Para Modificar libros, se debe realizar con la informacion exacta, nombre completo o isbn exacto
    def modificarLibro(self, clave):
        for libro in self.libros:
            if libro.isbn.lower() == clave.lower() or libro.nombre.lower() == clave.lower():
                print(f"  -- Se esta realizando una modificacion al libro: {libro.info()}")
                print("\n" * 2)
                nuevoNombre = input("\n  -- Ingresar nuevo nombre (Si no desea cambiar nombre, dejar en blanco): ")
                nuevoAutor = input("\n  -- Ingresar nuevo autor (Si no desea cambiar autor, dejar en blanco): ")
                nuevoIsbn = input("\n  -- Ingresar nuevo ISBN (Si no desea cambiar ISBN, dejar en blanco): ")

                if nuevoNombre:
                    libro.nombre = nuevoNombre
                if nuevoAutor:
                    libro.autor = nuevoAutor
                if nuevoIsbn:
 #ciclo para identificar que el nuevo ISBN no exista ya en la biblioteca
                    for verificarIsbn in self.libros:
                        if verificarIsbn != libro and verificarIsbn.isbn == nuevoIsbn:
                            print("\n  -- El nuevo ISBN ya existe. No se pudo realizar la modificaciòn.")
                            print("\n" * 2)
                            return
                    libro.isbn = nuevoIsbn

                print(f"\n  -- El libro fue modificado correctamente el: {hora}")
                print(" -", libro.info())
                return
        print("  -- El libro no se encuentra o está prestado (no se puede modificar los datos).")
        print("\n" * 2)