"""————————————————
   Clase vertice
———————————————————"""
import json
class Vertice:

    # constructor
    def __init__(self, nombre, libros):
        self.nombre = nombre
        self.libros = libros
        self.listaAdyacentes = []

    @classmethod
    # constructor json
    def fromjson(cls, json_string):
        json_dict = json_string.loads(json_string)
        return Vertice(**json_dict)

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


    # for i in librerias:
        # print(i.getNombre())
        # print(i.getLibros())
        # print(i.getListaAdyacentes())
    """————————————————————————————————————————————GETS | SETS————————————————————————————————————————————————————"""




    """————————————————————————————————————————————FUNCIONES———————————————————————————————————————————————————————"""



