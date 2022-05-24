
from control.Menu import *
from clases.Grafo import *
import json

from helpers.Keyboard import *

# gido()
# ruta = 'data/nodos.json'
# def cargarDatos(ruta):
#     with open(ruta) as file:
#         aristas = json.load(grafo.getListaAristas())
# menu = Menu()
# menu.menuInicio()

grafo = Grafo()

# Ingresar vertices
grafo.ingresarVertice("a",3)
grafo.ingresarVertice("b",3)
grafo.ingresarVertice("b",4)
grafo.ingresarVertice("c",3)
grafo.ingresarVertice("d",3)
grafo.ingresarVertice("e",3)
grafo.ingresarVertice("f",3)
grafo.ingresarVertice("g",3)
grafo.ingresarVertice("h",3)
grafo.ingresarVertice("i",3)

# Ingresar aristas
grafo.ingresarArista("a","b",1)
grafo.ingresarArista("b","a",1)
grafo.ingresarArista("b","c",1)
grafo.ingresarArista("c","d",1)
grafo.ingresarArista("d","e",1)
grafo.ingresarArista("e","f",1)
grafo.ingresarArista("f","g",1)
grafo.ingresarArista("g","h",1)
grafo.ingresarArista("h","i",1)
grafo.ingresarArista("i","j",1)
grafo.ingresarArista("j","b",1)



# cargarDatos(ruta)

grafo.mostrarVertices()
grafo.mostrarAristas()
grafo.dirigido()
grafo.mostrarAristas()
grafo.nodirigido()
grafo.mostrarAristas()





