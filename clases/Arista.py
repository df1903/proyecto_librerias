"""————————————————
   Clase arista
———————————————————"""
class Arista:

    # constructor
    def __init__(self, origen, destino, peso):
        self.origen = origen
        self.destino = destino
        self.peso = peso

    @classmethod
    # constructor json
    def fromjson(cls, json_string):
        json_dict = json_string.loads(json_string)
        return Arista(**json_dict)

    """————————————————————————————————————————————GETS | SETS————————————————————————————————————————————————————"""

    # Set - Get | origen
    def getOrigen(self):
        return self.origen

    def setOrigen(self, origen):
        self.origen = origen

    # Set - Get | destino
    def getDestino(self):
        return self.destino

    def setDestino(self, destino):
        self.destino = destino

    # Set - Get | peso
    def getPeso(self):
        return self.peso

    def setPeso(self, peso):
        self.peso = peso

    """—————————————————————————————————————————————FUNCIONES—————————————————————————————————————————————————————"""

