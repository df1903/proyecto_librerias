"""————————————————
   Vertice class
———————————————————"""
class Vertice:

    # builder
    def __init__(self, dato):
        self.dato = dato
        self.listaAdyacentes = []

    """————————————————————————————————————————————GETS | SETS————————————————————————————————————————————————————"""

    # Set - Get | dato
    def getDato(self):
            return self.dato

    def setDato(self,dato):
        self.dato = dato

    # Set - Get | lista adyacentes
    def getListaAdyacentes(self):
        return self.listaAdyacentes

    def setListaAdyacentes(self,listaAdyacentes):
        self.listaAdyacentes = listaAdyacentes


    """————————————————————————————————————————————METHODS———————————————————————————————————————————————————————"""


