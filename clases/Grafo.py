"""————————————————
   Clase grafo
———————————————————"""
from copy import copy #para realizar copias de objetos
import sys
from clases.Arista import *
from clases.Vertice import *
import json
from typing import List
from collections import deque

class Grafo:

    # constructor
    def __init__(self):
        self.listaVertices = []
        self.listaAristas = []
        self.profundidad = []
        self.amplitud = []
    """————————————————————————————————————————————GETS | SETS————————————————————————————————————————————————————"""

    # Set - Get | lista de vertices
    def getListaVertices(self):
        return self.listaVertices

    def setListaVertices(self, listaVertices):
        self.listaVertices = listaVertices

    # Set - Get | lista de aristas
    def getListaAristas(self):
        return self.listaAristas

    def setListaAristas(self, listaAristas):
        self.listaAristas = listaAristas

    # Set - Get | recorrido profundidad
    def getProfundidad(self):
        return self.profundidad

    def setProfundidad(self, profundidad):
        self.profundidad = profundidad

    # Set - Get | recorrido profundidad
    def getAmplitud(self):
        return self.amplitud

    def setAmplitud(self,amplitud):
        self.amplitud = amplitud



    """—————————————————————————————————————————FUNCIONES VERTICE————————————————————————————————————————————————"""

    # ingresar vertice
    def ingresarVertice(self, nombre, libros):
        if not self.existeVertice(nombre, self.listaVertices):
            self.listaVertices.append(Vertice(nombre, libros))

    # existe vertice
    def existeVertice(self, nombre, listaVertices):
        for i in listaVertices:
            if nombre == i.getNombre():
                return True
        return False

    # mostrar vertices
    def mostrarVertices(self):
        print("                                    VERTICES")
        for i in self.listaVertices:
            # print(i+1, "- {0}".format(i.getNombre()))
            print(i.getNombre())
        # return False

    # obtener vertice
    def obtenerVertice(self, origen, lista):
        for i in lista:
            if origen == i.getNombre():
                return i

    """—————————————————————————————————————————FUNCIONES ARISTA—————————————————————————————————————————————————"""

    # ingresar arista
    def ingresarArista(self, origen, destino, peso):
        if not self.existeArista(origen, destino, self.listaAristas):
            if self.existeVertice(origen, self.listaVertices) and self.existeVertice(destino, self.listaVertices):
                self.listaAristas.append(Arista(origen, destino, peso))
                self.obtenerVertice(origen, self.listaVertices).getListaAdyacentes().append(destino)
                # return True
        # return False

    # existe arista
    def existeArista(self, origen, destino, lista):
        for i in lista:
            if origen == i.getOrigen() and destino == i.getDestino():
                return True
        return False

    # mostrar aristas
    def mostrarAristas(self):
        print("                                    ARISTAS")
        for i in self.listaAristas:
            print("| Origen: {0}  →  Destino: {1}  |  Peso: {2} |"
                  .format(i.getOrigen(),
                          i.getDestino(),
                          i.getPeso()))

    # obtener Arista
    def obtenerArista(self, origen, destino, lista):
        for i in lista:
            if origen == i.getOrigen() and destino == i.getDestino():
                return i

    # mostrar adyacencias
    def mostrarAdyacencias(self):
        print("                                    ADYACENCIAS")
        for i in self.listaVertices:
            print("| vértice: {0} |  Adyacencias: {1} |"
                  .format(i.getNombre(),
                          i.getListaAdyacentes()))

    """—————————————————————————————————————————————FUNCTIONS————————————————————————————————————————————————————————"""

    # convertir dirigido a no dirigido
    def nodirigido(self):
        lista = copy(self.listaAristas)
        for i in lista:
            crear = True
            for j in lista:
                if i.getOrigen() == j.getDestino() and i.getDestino() == j.getOrigen():
                    crear = False
                    break
            if crear:
                self.ingresarArista(i.getDestino(), i.getOrigen(), i.getPeso())

    # convertir no dirigido a dirigido
    def dirigido(self):
        lista = copy(self.listaAristas)
        for i in lista:
            arista = False
            for j in lista:
                if i.getOrigen() == j.getDestino() and i.getDestino() == j.getOrigen():
                    arista = j
                    break
            if arista:
                lista.pop(lista.index(arista))
                vertice = self.obtenerVertice(arista.getOrigen(), self.listaVertices)
                vertice.getListaAdyacentes().pop(vertice.getListaAdyacentes().index(arista.getDestino()))
        self.listaAristas = lista

    # recorrido en profundidad
    def recorridoProfundidad(self, nombre):
        if nombre in self.profundidad:
            return
        vertice = self.obtenerVertice(nombre, self.listaVertices)
        if vertice != None:
            self.profundidad.append(vertice.getNombre())
            for dato in vertice.getListaAdyacentes():
                self.recorridoProfundidad(dato)

    # recorrido en amplitud
    def recorridoAmplitud(self, nombre):
        visitados = []
        cola =  []
        cola.append(nombre)
        for i in self.listaVertices:
            visitados.append(False)
        self.ra(cola, visitados)

    def ra(self, cola, visitados):
        if len(cola) == 0:
            return
        vertice = self.obtenerVertice(cola.pop(0), self.listaVertices)
        self.amplitud.append(vertice.getNombre())
        visitados[self.listaVertices.index(vertice)] = True
        for a in vertice.getListaAdyacentes():
            if not (a in cola) and not (visitados[self.listaVertices.index(self.obtenerVertice(a, self.listaVertices))]):
                cola.append(a)
        self.ra(cola, visitados)

    # algoritmo de kruskal
    def kruskal(self):
        aristas = copy(self.listaAristas)
        visitados = []  # para vetices visitados

        for v in self.listaVertices:# inicializar con el tamaño de los vertice con false
            visitados.append(False)
        return self.ordenarKruskal(visitados, aristas, [])

    def ordenarKruskal(self, visitados, aristas, recorrido):
        if len(recorrido) == len(self.listaVertices)-1:# retornar cuando el arbol de expacion minima este formado
            return recorrido
        for vis in aristas:  # eliminar aristas que formen ciclos
            if visitados[self.listaVertices.index(self.obtenerVertice(vis.getDestino(), self.listaVertices))] == True:
                aristas.pop(aristas.index(vis))
        menor = aristas[0]
        for a in aristas:  # obtener arista de menor peso
            if a.getPeso() < menor.getPeso():
                menor = a
        recorrido.append(aristas.pop(aristas.index(menor)))
        return self.ordenarKruskal(visitados, aristas, recorrido)


    # algoritmo de prim
    def prim(self):
        # inicializar listas
        visitados = []# para vetices visitados
        recorrido = []# agregar recorrido final
        aristas = []# posibles aristas

        for v in self.listaVertices:# inicializar con el tamaño de los vertice con false
            visitados.append(False)

        menor = self.listaAristas[0]# tomar una arista base para comparar

        for a in self.listaAristas:# obtener arista con menor peso
            if a.getPeso() < menor.getPeso():
                menor = a

        recorrido.append(menor) # agregar arista al recorrido final

       # obtener los vertices de las aristas
        origen = self.obtenerVertice(menor.getOrigen(), self.listaVertices)
        destino = self.obtenerVertice(menor.getDestino(), self.listaVertices)

        # cambiar el valor de visitado de los vertices de la arista
        visitados[self.listaVertices.index(origen)] = True
        visitados[self.listaVertices.index(destino)] = True

        for ad in origen.getListaAdyacentes():# añadir adyacencias de los vertices
            if visitados[self.listaVertices.index(self.obtenerVertice(ad,self.listaVertices))] == False:
                aristas.append(self.obtenerArista(origen.getNombre(), ad, self.listaAristas))

        for ada in destino.getListaAdyacentes():# añadir adyacencias de los vertices
            if visitados[self.listaVertices.index(self.obtenerVertice(ada,self.listaVertices))] == False:
                aristas.append(self.obtenerArista(destino.getNombre(), ada, self.listaAristas))
        return self.ordenarPrim(visitados, aristas, recorrido)


    def ordenarPrim(self, visitados, aristas, recorrido):

        if len(recorrido) == len(self.listaVertices)-1:# retornar cuando el arbol de expacion minima este formado
            return recorrido

        for vis in aristas:# eliminar aristas que formen ciclos
            if  visitados[self.listaVertices.index(self.obtenerVertice(vis.getDestino(), self.listaVertices))] == True:
                aristas.pop(aristas.index(vis))

        menor = aristas[0]
        for a in aristas:#obtener arista de menor peso
            if a.getPeso() < menor.getPeso():
                menor = a
        menor = aristas.pop(aristas.index(menor))

        destino = self.obtenerVertice(menor.getDestino(), self.listaVertices)
        visitados[self.listaVertices.index(destino)] = True
        recorrido.append(menor)

        for ad in destino.getListaAdyacentes():# añadir adyacencias de los vertices
            if visitados[self.listaVertices.index(self.obtenerVertice(ad, self.listaVertices))] == False:
                aristas.append(self.obtenerArista(menor.getDestino(), ad, self.listaAristas))
        return self.ordenarPrim(visitados, aristas, recorrido)

    # boruvka

    def boruvka(self):

        # listaAdyacencias = []# crear la lista de adyacencias

        # crear los 3 conjuntos
        listaVertices = []# lista para conjuntos de vertices
        listaAristas = []# lista para conjuntos de aristas de todos los vertices
        conjuntos = []# lista para conjuntos definitivos

        # inicializar conjuntos
        for vertice in self.listaVertices:
            listaVertices.append([])
            listaVertices[len(listaVertices) - 1].append(vertice.getNombre())
            conjuntos.append([])
            # listaAdyacencias.append([])
            listaAristas.append([])
            for adyacencia in vertice.getListaAdyacentes():
                # listaAdyacencias[len(listaAdyacencias)-1].append(adyacencia)
                listaAristas[len(listaAristas) - 1].append(self.obtenerArista(vertice.getNombre(), adyacencia, self.listaAristas))

        return self.ordenarBoruvka(listaVertices, listaAristas, conjuntos)

    def ordenarBoruvka(self, listaVertices, listaAristas, conjuntos):
        if len(conjuntos) == 1:
            return conjuntos
        for indice in range(len(listaVertices)):# encontrar la menor arista de un conjunto de vertice
            menor = listaAristas[indice][0]
            for i in listaVertices[indice]:
                for arista in listaAristas[indice]:
                    if menor.getPeso() > arista.getPeso():
                        menor = arista
            conjuntos[indice].append(listaAristas[indice].pop(listaAristas[indice].index(menor)))

        # for indice in range(len(listaVertices)):# verfico las otras listas por el tamaño de la lista de el conjunto de vertices
        #     for vertice in listaVertices[indice]:# obtengo un vertice de cada lista de vertices
        #         # for i in range(len(conjuntos)- indice):# obtengo el indice paraa obtener un conjunto
        #         i = 1
        #         while indice + i  < len(conjuntos):
        #             enlace = False
        #             for arista in conjuntos[i + indice]:# obtengo las aristas de un conjunto
        #                 if vertice == arista.getDestino():
        #                     enlace = True
        #                     break
        #             if enlace:
        #                 for arista in conjuntos[i + indice]:
        #                     conjuntos[indice].append(arista)
        #                 conjuntos.pop(1 + indice)
        #             i +=1
        indice = 0
        while indice < len(conjuntos):
            for vertice in listaVertices[indice]:# obtengo un vertice de cada lista de vertices
                # for i in range(len(conjuntos)- indice):# obtengo el indice paraa obtener un conjunto
                i = 1
                while indice + i  < len(conjuntos):
                    enlace = False
                    for arista in conjuntos[i + indice]:# obtengo las aristas de un conjunto
                        if vertice == arista.getDestino():
                            enlace = True
                            break
                    if enlace:
                        for arista in conjuntos[i + indice]:
                            conjuntos[indice].append(arista)
                        conjuntos.pop(1 + indice)
                        for v in listaVertices[i + indice]:
                            listaVertices[indice].append(v)
                        listaVertices.pop(1 + indice)
                        for a in listaAristas[i + indice]:
                            listaAristas[indice].append(a)
                        listaAristas.pop(1 + indice)

                    i +=1
            indice += 1

        for lista in listaAristas:
            i = 0
            while i < len(lista):
                j = 0
                while j < len(lista):
                    if lista[i].getOrigen() == lista[j].getDestino() and lista[i].getDestino() == lista[j].getOrigen():
                        lista.pop(j)
                    j += 1
                i += 1

        for lista in conjuntos:
            i = 0
            while i < len(lista):
                j = 0
                while j < len(lista):
                    if lista[i].getOrigen() == lista[j].getDestino() and lista[i].getDestino() == lista[j].getOrigen():
                        lista.pop(j)
                    j += 1
                i += 1





        print(len(listaAristas))
        print(len(listaVertices))
        print(len(conjuntos))
        return self.ordenarBoruvka(listaVertices, listaAristas, conjuntos)





    #
    #     aristasBoruvka = []
    #     listaConjuntos = []
    #     bandera = True
    #     cantidad = 0
    #     while(cantidad >1 or bandera):
    #         for vertice in copiaVertices:
    #             self.operacinesCunjuntosB(listaConjuntos, aristasBoruvka, copiaAristas)
    #         bandera = False
    #         cantidad = self.cantidadConjuntos(listaConjuntos)
    #     return aristasBoruvka
    #
    # def cantidadConjuntos(self,listaConjuntos):
    #     cantida = 0
    #     for conjunto in listaConjuntos:
    #         if len(conjunto) > 0:
    #             cantidad = cantidad + 1
    #     return cantidad
    #
    # operacinesCunjuntosB(listaConjuntos, aristasBoruvka, copiaAristas)



    # dijkstra
    def dijkstra(self, origen, destino):
        verticesAux = []
        verticesD = []
        caminos = self.ordenarDijkstra(origen, verticesAux)
        cont = 0
        for i in caminos:
            print("La distancia mínima a " + self.listaVertices[cont].getNombre() + " es " + str(i))
            cont += 1

        self.rutas(verticesD, verticesAux, destino, origen)
        print("El camino más corto de " + origen + " a " + destino + " es: ")
        print(verticesD)

    def ordenarDijkstra(self, origen, verticesAux):
        visitados = []  # lista de visitados
        caminos = []  # recorrido final

        for v in self.listaVertices:  # iniciar los valores en infinito
            caminos.append(float("inf"))
            visitados.append(False)
            verticesAux.append(None)
            if v.getNombre() == origen:
                caminos[self.listaVertices.index(v)] = 0
                verticesAux[self.listaVertices.index(v)] = v.getNombre()

        while not self.todosVisitados(visitados):
            menorAux = self.menorNoVisitado(caminos, visitados)  # obtiene el menor no visitado
            if menorAux == None:
                break
            indice = self.listaVertices.index(menorAux)  # indice del menor no marcado
            visitados[indice] = True
            valorActual = caminos[indice]

            for adyacencia in menorAux.getListaAdyacentes():
                indiceNuevo = self.listaVertices.index(self.obtenerVertice(adyacencia, self.listaVertices))
                arista = self.verificarArista(menorAux.getNombre(), adyacencia)
                if caminos[indiceNuevo] > valorActual + arista.getPeso():
                    caminos[indiceNuevo] = valorActual + arista.getPeso()
                    verticesAux[indiceNuevo] = self.listaVertices[indice].getNombre()

        return caminos

    def verificarArista(self, origen, destino):
        for i in range(len(self.listaAristas)):
            if origen == self.listaAristas[i].getOrigen() and destino == self.listaAristas[i].getDestino():
                return self.listaAristas[i]

        return None

    def todosVisitados(self, visitados):
        for vertice in visitados:
            if vertice == False:
                return False

        return True

    def menorNoVisitado(self, caminos, visitados):
        verticeMenor = None
        caminosAux = sorted(caminos)  # de menor a mayor

        copiaCaminos = copy(caminos)
        bandera = True
        cont = 0

        while bandera:
            menor = caminosAux[cont]

            if visitados[copiaCaminos.index(menor)] == False:
                verticeMenor = self.listaVertices[copiaCaminos.index(menor)]
                bandera = False

            else:
                copiaCaminos[copiaCaminos.index(menor)] = "x"
                cont += 1

        return verticeMenor

    def rutas(self, verticesD, verticesAux, destino, origen):
        verticeDestino = self.obtenerVertice(destino, self.listaVertices)
        indice = self.listaVertices.index(verticeDestino)

        if verticesAux[indice] == None:
            print("No hay camino entre: ", (origen, destino))
            return
        aux = destino

        while aux != origen:
            verticeDestino = self.obtenerVertice(aux, self.listaVertices)
            indice = self.listaVertices.index(verticeDestino)
            verticesD.insert(0, aux)
            aux = verticesAux[indice]
        verticesD.insert(0, aux)

    # # are there wells?
    # def existenPozos(self):
    #     for i in range(len(self.listaVertices)):
    #         if not self.listaVertices[i].getListaAdyacentes():
    #             return print("Pozo --> {0}".format(self.listaVertices[i].getNombre()))
    #     return print("El grafo no tiene Pozos")
    #
    # # are there sources?
    # def existenFuentes(self):
    #     for i in range(len(self.listaVertices)):
    #         if self.listaVertices[i].getListaAdyacentes():
    #             return print("Fuente --> {0}".format(self.listaVertices[i].getNombre()))
    #     return print("El grafo no tiene Fuentes")
    #
    # # 1)smallest to largest edges
    # def minMaxAristas(self, entorno):
    #     if entorno == (len(self.listaAristas)):
    #         return
    #     self.ordenarMinMax(entorno, entorno + 1)
    #     return self.minMaxAristas(entorno + 1)
    #
    # def ordenarMinMax(self, entorno, iter):
    #     if iter == (len(self.listaAristas)):
    #         return
    #     if self.listaAristas[entorno].getPeso() > self.listaAristas[iter].getPeso():
    #         aux = self.listaAristas[entorno]
    #         self.listaAristas[entorno] = self.listaAristas[iter]
    #         self.listaAristas[iter] = aux
    #     return self.ordenarMinMax(entorno, iter + 1)
    #
    # # 1.1)largest to smallest edges
    # def maxMinAristas(self, entorno):
    #     if entorno == (len(self.listaAristas)):
    #         return
    #     self.ordenarMaxMin(entorno, entorno + 1)
    #     return self.maxMinAristas(entorno + 1)
    #
    # def ordenarMaxMin(self, entorno, iter):
    #     if iter == (len(self.listaAristas)):
    #         return
    #     if self.listaAristas[entorno].getPeso() < self.listaAristas[iter].getPeso():
    #         aux = self.listaAristas[entorno]
    #         self.listaAristas[entorno] = self.listaAristas[iter]
    #         self.listaAristas[iter] = aux
    #     return self.ordenarMaxMin(entorno, iter + 1)
    #
    #
    # # 2)degree of the vertices
    # # def gradoVertices(self, entorno):
    # #     if entorno == (len(self.listaVertices)):
    # #         return True
    # #     self.gradoVertice(self.listaVertices[entorno], 0, 0)
    # #     return self.gradoVertices01(entorno+1)
    # #
    # # def gradoVertice(self, vertice, entorno, gradoVertice):
    # #     if entorno == (len(self.listaAristas)):
    # #         print("El grado del vertice {} es {}".format(vertice.getNombre(), gradoVertice))
    # #         return
    # #     if vertice.getNombre() == self.listaAristas[entorno].getOrigen() or vertice.getNombre() == self.listaAristas[entorno].getDestino():
    # #         gradoVertice += 1
    # #     self.gradoVertice(vertice, entorno+1, gradoVertice)
    #
    # def gradoVertices(self, entorno, listaGrados):
    #     if entorno == 0:
    #         for i in range(len(self.listaVertices)):
    #             listaGrados.append(0)
    #     if entorno == (len(self.listaAristas)):
    #         return listaGrados
    #     for i in range(len(self.listaVertices)):
    #         if self.listaVertices[i].getNombre() == self.listaAristas[entorno].getOrigen() or self.listaVertices[i].getNombre() == self.listaAristas[entorno].getDestino():
    #             listaGrados[i] += 1
    #     return self.gradoVertices(entorno+1,listaGrados)
    #
    # def mostrarGradoVertices(self):
    #     print("                                 GRADOS DE LOS VERTICES")
    #     listaGrados = self.gradoVertices(0,[])
    #     for i in range(len(self.listaVertices)):
    #         print("{} Grado({})".format(self.listaVertices[i].getNombre(), listaGrados[i]))
    #
    # # 3)vertex highest degree
    # def verticeMayorGrado(self):
    #     listaGrados = self.gradoVertices(0,[])
    #     vertice = [0,0]
    #     for i in range(len(self.listaVertices)):
    #         if listaGrados[i] > vertice[1]:
    #             vertice[0] = i
    #             vertice[1] = listaGrados[i]
    #     print("{} con grado de {} es el vertice con mayor grado".format(self.listaVertices[vertice[0]].getNombre(),vertice[1]))
    #
    # # 4)average adjacencies list
    # def promedioListaAdyacencias(self):
    #     adyacencias = 0
    #     for i in range(len(self.listaVertices)):
    #         adyacencias += len(self.listaVertices[i].getListaAdyacentes())
    #     adyacencias = adyacencias/len(self.listaVertices)
    #     print("El promedio de la lista de adyacencias es: ",adyacencias)
    #
    # # 5)Show the wells
    # def pozos(self,entorno,listaPozos):
    #     if entorno == 0:
    #         for i in range(len(self.listaVertices)):
    #             listaPozos.append(True)
    #     if entorno == (len(self.listaAristas)):
    #         return listaPozos
    #     for i in range(len(self.listaVertices)):
    #         if self.listaVertices[i].getNombre() == self.listaAristas[entorno].getOrigen():
    #             listaPozos[i] = False
    #     return self.pozos(entorno+1, listaPozos)
    #
    # def mostrarPozos(self):
    #     print("                                    POZOS")
    #     listaPozos = self.pozos(0,[])
    #     for i in range(len(self.listaVertices)):
    #         if listaPozos[i]:
    #             print(self.listaVertices[i].getNombre())
    #
    # # 6)Show the sources
    # def fuentes(self,entorno,listaFuentes):
    #     if entorno == 0:
    #         for i in range(len(self.listaVertices)):
    #             listaFuentes.append(True)
    #     if entorno == (len(self.listaAristas)):
    #         return listaFuentes
    #     for i in range(len(self.listaVertices)):
    #         if self.listaVertices[i].getNombre() == self.listaAristas[entorno].getDestino():
    #             listaFuentes[i] = False
    #     return self.fuentes(entorno+1, listaFuentes)
    #
    # def mostrarFuentes(self):
    #     print("                                   FUENTES")
    #     listaFuentes = self.fuentes(0,[])
    #     for i in range(len(self.listaVertices)):
    #         if listaFuentes[i]:
    #             print(self.listaVertices[i].getNombre())
    #
    # # 7)average edge weight
    # def promedioPesoAristas(self):
    #     promedio = 0
    #     for i in range(len(self.listaAristas)):
    #         promedio += self.listaAristas[i].getPeso()
    #     promedio = promedio / len(self.listaAristas)
    #     print("El promedio del peso de las aristas es: ",promedio)
    #
    # # 8)top artist
    # def aristaMayorPeso(self):
    #     aristaMayor= [Arista(0,0,0)]
    #     for i in range(len(self.listaAristas)):
    #         if aristaMayor[len(aristaMayor)-1].getPeso() < self.listaAristas[i].getPeso():
    #            aristaMayor = [self.listaAristas[i]]
    #         elif aristaMayor[len(aristaMayor)-1].getPeso() == self.listaAristas[i].getPeso():
    #             aristaMayor.append(self.listaAristas[i])
    #
    #     if len(aristaMayor) == 1:
    #         print("Arista mayor peso: {}--> {} peso {}".format(aristaMayor[0].getOrigen(), aristaMayor[0].getDestino(), aristaMayor[0].getPeso()))
    #
    #     else:
    #         print("Las aristas de mayor peso son:")
    #         for i in range(len(aristaMayor)):
    #             print ("{}--> {} peso {}".format(aristaMayor[i].getOrigen(), aristaMayor[i].getDestino() , aristaMayor[i].getPeso()))
    #
    # # 9)
    # def aristaMenorPeso(self):
    #     aristaMenor= [Arista(0,0,sys.maxsize)]
    #     for i in range(len(self.listaAristas)):
    #         if aristaMenor[len(aristaMenor)-1].getPeso() > self.listaAristas[i].getPeso():
    #            aristaMenor = [self.listaAristas[i]]
    #         elif aristaMenor[len(aristaMenor)-1].getPeso() == self.listaAristas[i].getPeso():
    #             aristaMenor.append(self.listaAristas[i])
    #
    #     if len(aristaMenor) == 1:
    #         print("Arista menor peso: {}--> {} peso {}".format(aristaMenor[0].getOrigen(), aristaMenor[0].getDestino(), aristaMenor[0].getPeso()))
    #
    #     else:
    #         print("Las aristas de menor peso son:")
    #         for i in range(len(aristaMenor)):
    #             print ("{}--> {} peso {}".format(aristaMenor[i].getOrigen(), aristaMenor[i].getDestino() , aristaMenor[i].getPeso()))
    #
    # # 10)
    # def verticeAdyacente(self):
    #     print("Ahora")
    #
    # # 11)
    # def listaAdyacencias(self):
    #     lista=[]
    #     for i in range(len(self.listaVertices)):
    #         for j in range(len(self.listaVertices[i].getListaAdyacentes())):
    #             lista.append(self.listaVertices[i].getListaAdyacentes()[j])
    #     return lista
    #
    # def mostrarListaAdyacentes(self):
    #     print("                                  LISTA ADYACENTES")
    #     lista = self.listaAdyacencias()
    #     for i in range(len(lista)):
    #         print(lista[i])
    # # a)
    # def verticesNoContemplados(self, entorno, listaVertices, listaAdyacencias):
    #     if entorno == 0:
    #         listaAdyacencias = self.listaAdyacencias()
    #         for i in range(len(self.listaVertices)):
    #             listaVertices.append(True)
    #     if entorno == (len(self.listaVertices)):
    #         return listaVertices
    #     for i in range(len(listaAdyacencias)):
    #         if self.listaVertices[entorno].getNombre() == listaAdyacencias[i]:
    #             listaVertices[entorno] = False
    #     return self.verticesNoContemplados(entorno+1, listaVertices, listaAdyacencias)
    #
    # def mostrarVerticesNoContemplados(self):
    #     print("                                  VERTICES NO CONTEMPLADOS")
    #     listaVertices =self.verticesNoContemplados(0, [], [])
    #     for i in range(len(listaVertices)):
    #         if listaVertices[i]:
    #             print(self.listaVertices[i].getNombre())
    #
    # # b)
    # def adyacenciaMasComun(self, entorno, listaVertices, listaAdyacencias):
    #     if entorno == 0:
    #         listaAdyacencias = self.listaAdyacencias()
    #         for i in range(len(self.listaVertices)):
    #             listaVertices.append(0)
    #     if entorno == (len(self.listaVertices)):
    #         return listaVertices
    #     for i in range(len(listaAdyacencias)):
    #         if self.listaVertices[entorno].getNombre() == listaAdyacencias[i]:
    #             listaVertices[entorno] += 1
    #     return self.adyacenciaMasComun(entorno+1, listaVertices, listaAdyacencias)
    #
    # def mostarAdyacenciaMasComun(self):
    #     listaVertices = self.adyacenciaMasComun(0, [], [])
    #     comun = 0
    #     for i in range(len(listaVertices)):
    #         if listaVertices[i] > comun:
    #             comun = i
    #     print("La adyacencia mas comun es {} con {} ".format(self.listaVertices[comun].getNombre(), listaVertices[comun]))
    #
    #
    #
    # def prim(self,origen):
    #     visitados = []
    #     for i in self.listaVertices:
    #         visitados.append(False)
    #     caminos= self.obtenerCaminos(origen,[], visitados, [])
    #     for c in caminos:
    #         print("{} ---> {}".format(c.getOrigen(), c.getDestino()))
    #
    #
    # def obtenerCaminos(self, origen, listaAdyacencias, visitados, caminosFinal):
    #     if self.visitadosTodos(visitados):
    #         return caminosFinal
    #     vertice = self.obtenerVertice(origen, self.listaVertices)
    #     visitados[self.listaVertices.index(vertice)] = True
    #     aristaActual = Arista("X", "X", float("inf"))
    #
    #     for i in range (len(vertice.getListaAdyacentes())):#Obtine las adyacencias del vertice
    #         listaAdyacencias.append(vertice.getListaAdyacentes()[i])
    #
    #     for v in self.listaVertices:
    #         if visitados[self.listaVertices.index(v)]:
    #             nuevolistaAdyacencias = []
    #             for l in listaAdyacencias:
    #                 if l.getDestino() != v.getNombre():
    #                     nuevolistaAdyacencias.append(l)
    #             listaAdyacencias = nuevolistaAdyacencias
    #
    #     for arista in listaAdyacencias:#obtener arista de menor peso
    #         if arista < aristaActual.getPeso():
    #             aristaActual = arista
    #     caminosFinal.append(aristaActual)
    #     return self.obtenerVertice(aristaActual.getDestino(),listaAdyacencias, visitados, caminosFinal)
    #
    #
    # def visitadosTodos(self, visitados):
    #     for i in visitados:
    #         if not i:
    #             return False
    #     return True
    #
    #
    #     caminos = self.caminosOrdenados(origen,[])
    #
