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




prim = grafo.boruvka()
for i in prim:
    for j in i:
        print(j.getOrigen(),"-->", j.getDestino(), "==", j.getPeso())
    print("xddxxd")
#     print("Funciono")
# a = [0]
# print(len(a))
# for i in range(len(a)):
#     print(i)











# Libreria Gadner ==> Libreria Voronoi == 170
# Libreria Voronoi ==> Casita == 190
# Casita ==> Libreria Gauss == 180
# Casita ==> Libreria Fahrenheit == 180
# Libreria Gauss ==> Libreria Richter == 198
# Libreria Richter ==> Libreria Konisberg == 225
# Libreria Gauss ==> Libreria Euler == 230
# Libreria Fahrenheit ==> Libreria Hilbert == 230
# Libreria Hilbert ==> Libreria Fibonacci == 250
# Libreria Fahrenheit ==> Libreria Celsius == 255













# grafo.recorridoAmplitud("Libreria Euler")
# for i in grafo.getAmplitud():
#     print(i)
#
# print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
# print("Funcionara pongamoslo a prueba")
# print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
#
# grafo.recorridoProfundidad("Libreria Euler")
# for i in grafo.getProfundidad():
#     print(i)

# for i in grafo.getListaVertices():
#     print(i.getNombre(), "Ad", i.getListaAdyacentes())
# for i in grafo.getListaVertices():
#         print(i.getNombre() == "Libreria Celsius")
# grafo.mostrarVertices()
# grafo.mostrarAristas()
# grafo.caminoMasCorto('Libreria Euler','Libreria Celsius')

# grafo.ingresarVertice("a", 10)
# grafo.ingresarVertice("b", 10)
# grafo.ingresarVertice("c", 10)
# grafo.ingresarVertice("d", 10)
# grafo.ingresarVertice("e", 10)
# #
# grafo.ingresarArista("a", "c", 3)

# grafo.ingresarArista("a", "b", 4)
# grafo.ingresarArista("b", "a", 1)
# grafo.ingresarArista("b", "c", 4)
# grafo.ingresarArista("c", "b", 2)
# grafo.ingresarArista("c", "d", 3)
# grafo.ingresarArista("d", "c", 3)
# grafo.ingresarArista("d", "e", 4)
# grafo.ingresarArista("e", "d", 4)
# grafo.ingresarArista("e", "a", 5)
# grafo.ingresarArista("a", "e", 5)


# prim = grafo.prim()
# for i in prim:
#     print(i.getOrigen(),"==>", i.getDestino(),"==", i.getPeso())
# grafo.caminoMasCorto("a","d")
# for i in grafo.getListaVertices():
#     print(i.getNombre(), "Ad", i.getListaAdyacentes())
#
# # grafo.mostrarVertices()
# grafo.mostrarAristas()
# grafo.dirigido()
# grafo.mostrarAristas()
#




