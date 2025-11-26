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
