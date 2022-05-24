"""————————————————
   Clase vertice
———————————————————"""
class Vertice:

    # constructor
    def __init__(self, nombre, libros):
        self.nombre = nombre
        self.libros = libros
        self.listaAdyacentes = []

    """————————————————————————————————————————————GETS | SETS————————————————————————————————————————————————————"""

    # Set - Get | nombre
    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    # Set - Get | libros
    def getLibros(self):
            return self.libros

    def setLibros(self, libros):
        self.libros = libros

    # Set - Get | lista adyacentes
    def getListaAdyacentes(self):
        return self.listaAdyacentes

    def setListaAdyacentes(self,listaAdyacentes):
        self.listaAdyacentes = listaAdyacentes


    """————————————————————————————————————————————FUNCIONES———————————————————————————————————————————————————————"""



