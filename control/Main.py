from scipy.sparse.csgraph import dijkstra

from control.Menu import *
from clases.Grafo import *
import json

# menu = Menu()
# menu.menuInicio()



grafo = Grafo()


# carga de json
# leer json y crear vertices
with open(r'C:\Users\2003n\OneDrive\Escritorio\proyecto_librerias\data\librerias.json', 'r') as json_file:
    libreriasData = json.loads(json_file.read())
    for l in libreriasData:
        aux = Vertice(**l)
        grafo.ingresarVertice(aux.getNombre())


# leer json y crear aristas
with open(r'C:\Users\2003n\OneDrive\Escritorio\proyecto_librerias\data\rutas.json', 'r') as json_file:
    rutasData = json.loads(json_file.read())
    for r in rutasData:
        aux = Arista(**r)
        grafo.ingresarArista(aux.getOrigen(), aux.getDestino(), aux.getPeso())



a= grafo.dijkstra("Libreria Konisberg", "Libreria Celsius")

for i in a :
    print(i.getOrigen(), i.getDestino(), i.getPeso())


a= grafo.dijkstraBlock("Libreria Konisberg", "Libreria Celsius")
for i in a :
    print(i.getOrigen(), i.getDestino(), i.getPeso())

