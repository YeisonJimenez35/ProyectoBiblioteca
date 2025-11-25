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
    

