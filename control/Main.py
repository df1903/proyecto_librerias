from control.Menu import *
from clases.Grafo import *
import json

# menu = Menu()
# menu.menuInicio()



grafo = Grafo()

# leer json y crear vertices
with open(r'C:\Users\2003n\OneDrive\Escritorio\proyecto_librerias\data\librerias.json', 'r') as json_file:
    libreriasData = json.loads(json_file.read())
    for l in libreriasData:
        aux = Vertice(**l)
        grafo.ingresarVertice(aux.getNombre(), aux.getLibros())


# leer json y crear aristas
with open(r'C:\Users\2003n\OneDrive\Escritorio\proyecto_librerias\data\rutas.json', 'r') as json_file:
    rutasData = json.loads(json_file.read())
    for r in rutasData:
        aux = Arista(**r)
        grafo.ingresarArista(aux.getOrigen(), aux.getDestino(), aux.getPeso())

# for i in grafo.getListaVertices():
#     print(i.getNombre(), "Ad", i.getListaAdyacentes())
# for i in grafo.getListaVertices():
#         print(i.getNombre() == "Libreria Celsius")
# grafo.mostrarVertices()
# grafo.mostrarAristas()
# grafo.caminoMasCorto('Libreria Euler','Libreria Celsius')

# grafo.recorridoProfundidad("Libreria Euler")
# for i in grafo.getProfundidad():
#     print(i)



# grafo.ingresarVertice("a", 10)
# grafo.ingresarVertice("b", 10)
# grafo.ingresarVertice("c", 10)
# grafo.ingresarVertice("d", 10)
# grafo.ingresarVertice("e", 10)
#
#
# grafo.ingresarArista("a", "b", 1)
# grafo.ingresarArista("b", "a", 1)
# grafo.ingresarArista("b", "c", 2)
# grafo.ingresarArista("c", "b", 2)
# grafo.ingresarArista("c", "d", 3)
# grafo.ingresarArista("d", "c", 3)
# grafo.ingresarArista("d", "e", 4)
# grafo.ingresarArista("e", "d", 4)
# grafo.ingresarArista("e", "a", 5)
# grafo.ingresarArista("a", "e", 5)

# grafo.caminoMasCorto("a","d")
# for i in grafo.getListaVertices():
#     print(i.getNombre(), "Ad", i.getListaAdyacentes())
#
# # grafo.mostrarVertices()
# grafo.mostrarAristas()
# grafo.dirigido()
# grafo.mostrarAristas()
#




