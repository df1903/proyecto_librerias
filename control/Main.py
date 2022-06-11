from scipy.sparse.csgraph import dijkstra

from clases.Grafo import *
import json

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

grafo.dirigido()
grafo.nodirigido()
grafo.recorridoAmplitud("Libreria Celsius")
grafo.recorridoProfundidad("Libreria Celsius")
solucion_boruvka = grafo.boruvka()
solucion_prim = grafo.prim()
solucion_kruskal = grafo.kruskal()
solucion_caminoBloqueado = grafo.caminoBloqueado("Libreria Celsius","Libreria Gadner")
solucion_dijkstra = grafo.dijkstra("Libreria Celsius","Libreria Gadner")

print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
print("Solucion boruvka")
for i in solucion_boruvka:
    print(i.getOrigen(),"----", i.getDestino(),"--->", i.getPeso())

print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
print("Solucion kruskal")
for i in solucion_kruskal:
    print(i.getOrigen(),"----", i.getDestino(),"--->", i.getPeso())
#
print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
print("Solucion dijkstra")
for i in solucion_dijkstra:
    print(i.getOrigen(),"----", i.getDestino(),"--->", i.getPeso())

print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
print("Solucion camino bloqueado")
for i in solucion_caminoBloqueado:
    print(i.getOrigen(),"----", i.getDestino(),"--->", i.getPeso())


print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
print("Solucion prim")
for i in solucion_prim:
    print(i.getOrigen(),"----", i.getDestino(),"--->", i.getPeso())


# print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
# print("Solucion amplitud")
# for i in grafo.getAmplitud():
#     print(i)
#     # print(i.getOrigen(), "----", i.getDestino(), "--->", i.getPeso())

# print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
# print("Solucion profundidad")
# for i in grafo.getProfundidad()     :
#     print(i)
#     # print(i.getOrigen(), "----", i.getDestino(), "--->", i.getPeso())

