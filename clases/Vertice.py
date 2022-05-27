"""————————————————
   Clase vertice
———————————————————"""
import json
class Vertice:

    # constructor
    def __init__(self, nombre):
        self.nombre = nombre
        self.listaAdyacentes = []

    @classmethod
    # constructor json
    def fromjson(cls, json_string):
        json_dict = json_string.loads(json_string)
        return Vertice(**json_dict)

    """————————————————————————————————————————————GETS | SETS————————————————————————————————————————————————————"""
    # Set - Get | nombre
    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    # Set - Get | lista adyacentes
    def getListaAdyacentes(self):
        return self.listaAdyacentes

    def setListaAdyacentes(self,listaAdyacentes):
        self.listaAdyacentes = listaAdyacentes




