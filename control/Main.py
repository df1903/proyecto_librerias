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


grafo.boruvka()
# # uniones = [[0,1],[1,7],[2,3],[3,4], [7,4]]
# uniones = [[0,1],[2,1],[3,4],[4,7], [7,1],[5,6],[6,1]]
#
# for i in uniones:
#     print(i)
#
# repetir = True
# while repetir:
#     unir = []
#     unir.append(uniones.pop(0))
#
#     repetir = False
#     while len(uniones) != 0:
#         count = 0
#         i = 0
#         Crear = True
#         while i != len(unir):
#             x = False
#             for u in unir[i]:
#                 for j in uniones[0]:
#                     if j == u:
#                         x = True
#             if x:
#                 count += 1
#                 for j in uniones[0]:
#                     unir[i].append(j)
#                 Crear = False
#             i += 1
#         if Crear:
#             unir.append([uniones[0][0],uniones[0][1]])
#         uniones.pop(0)
#         if count > 1:
#             repetir = True
#
#     for conjunto in unir:
#         uniones.append([])
#         for element in conjunto:
#             if element not in uniones[len(uniones)-1]:
#                 uniones[len(uniones) - 1].append(element)
#
#
# print(uniones)