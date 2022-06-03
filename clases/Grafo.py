"""————————————————
   Clase grafo
———————————————————"""
from copy import copy #para realizar copias de objetos
from clases.Arista import *
from clases.Vertice import *


class Grafo:

    # constructor
    def __init__(self):
        self.listaVertices = []
        self.listaAristas = []
        self.profundidad = []
        self.amplitud = []
        self.caminoBloqueado = []
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

    # Set - Get | camino bloqueado
    def getCaminoBloqueado(self):
        return self.caminoBloqueado

    def setCaminoBloqueado(self, caminoBloqueado):
        self.caminoBloqueado = caminoBloqueado

    """—————————————————————————————————————————FUNCIONES VERTICE————————————————————————————————————————————————"""

    # ingresar vertice
    def ingresarVertice(self, nombre):
        if not self.existeVertice(nombre, self.listaVertices):
            self.listaVertices.append(Vertice(nombre))

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
            print(i.getNombre())

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
        conjuntoVertices = [] # conjunto con conjunto de vertices
        conjuntoAristas = [] # conjunto solucion
        copiaAristas = copy(self.listaAristas) # conjunto de donde se extraeran aristas

        # inicializacion de listas
        for i in self.listaVertices:
            conjuntoVertices.append([])
            conjuntoAristas.append([])
            conjuntoVertices[len(conjuntoVertices)-1].append(i)

        # for i in conjuntoVertices:
        #     print(i)
        #
        # for i in conjuntoAristas:
        #     print(i)
        #
        # for i in copiaAristas:
        #     print(i.getOrigen(),i.getDestino(),i.getPeso())

        aristas = self.ordenarBoruvka(conjuntoVertices, copiaAristas, conjuntoAristas)
        print("solucion")
        for j in aristas:
            for i in j:
                print(i.getOrigen(),"----", i.getDestino(),"--->", i.getPeso())

    def ordenarBoruvka(self, conjuntoVertices, copiaAristas, conjuntoAristas):
        if len(conjuntoVertices) == 1:
            return conjuntoAristas
        aristasTemp = []
        uniones = []
        print("tamaño copiaAristas", len(copiaAristas))
        # encontrar menor
        for listaVeritices in conjuntoVertices:
            menor = (Arista("x", "x", float("inf")))
            for vertice in listaVeritices:
                for arista in copiaAristas:
                    if arista.getOrigen() == vertice.getNombre():
                        if arista.getPeso() < menor.getPeso():
                            menor = arista
            # aristasTemp.append([])
            # aristasTemp[len(aristasTemp)-1]
            copiaAristas.pop(copiaAristas.index(menor))
            conjuntoAristas[conjuntoVertices.index(listaVeritices)].append(menor)
            aristasTemp.append(menor)
            print("menor")
            print(menor.getOrigen(),"----", menor.getDestino(),"--->", menor.getPeso())
        print("tamaño copiaAristas", len(copiaAristas))

        # print("menor")
        # for i in aristasTemp:
        #     print(i.getOrigen(),"---",i.getDestino(),"---->", i.getPeso())


        # verificar uniones
        for listaVeritices in conjuntoVertices:
            for vertice in listaVeritices:
                for arista in aristasTemp:
                    if aristasTemp.index(arista) != conjuntoVertices.index(listaVeritices):
                         if vertice.getNombre() == arista.getDestino():
                            uniones.append([conjuntoVertices.index(listaVeritices), aristasTemp.index(arista)])

        # print("verificar uniones")
        # for i in uniones:
        #     print(i)

        repetir = True
        while repetir:
            unir = []
            unir.append(uniones.pop(0))

            repetir = False
            while len(uniones) != 0:
                count = 0
                i = 0
                Crear = True
                while i != len(unir):
                    x = False
                    for u in unir[i]:
                        for j in uniones[0]:
                            if j == u:
                                x = True
                    if x:
                        count += 1
                        for j in uniones[0]:
                            unir[i].append(j)
                        Crear = False
                    i += 1
                if Crear:
                    unir.append([uniones[0][0], uniones[0][1]])
                uniones.pop(0)
                if count > 1:
                    repetir = True

            for conjunto in unir:
                uniones.append([])
                for element in conjunto:
                    if element not in uniones[len(uniones) - 1]:
                        uniones[len(uniones) - 1].append(element)

        print(uniones)
        verticeTemp = []
        conjuntoAristasTemp = []
        for i in uniones:
            verticeTemp.append([])
            conjuntoAristasTemp.append([])
            for j in i:
                for x in conjuntoVertices[j]:
                    verticeTemp[len(verticeTemp) - 1].append(x)
                for y in conjuntoAristas[j]:
                    conjuntoAristasTemp[len(conjuntoAristasTemp) - 1].append(y)

        for i in conjuntoAristasTemp:
            for j in i:
                print(j.getOrigen(),"---",j.getDestino(),"---->", j.getPeso())
            print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")

        conjuntoAristas = []
        # eliminar aristas repetidas

        for i in range(len(conjuntoAristasTemp)):
            for j in conjuntoAristasTemp[i]:
                arista = False
                for x in conjuntoAristasTemp[i]:
                    if j.getOrigen() == x.getDestino() and j.getDestino() == x.getOrigen():
                        arista = x
                        break
                if arista:
                    conjuntoAristasTemp[i].pop(conjuntoAristasTemp[i].index(arista))
        print("tamaño copiaAristas", len(copiaAristas))

        for i in verticeTemp:
            for j in i:
                for x in copiaAristas:
                    if x.getOrigen() == j.getNombre():
                        for y in i:
                            if x.getDestino() == y.getNombre():
                                copiaAristas.pop(copiaAristas.index(x))
        print("tamaño copiaAristas", len(copiaAristas))

        for i in copiaAristas:
            print(i.getOrigen(), i.getDestino(), i.getPeso())

        return self.ordenarBoruvka(verticeTemp, copiaAristas, conjuntoAristasTemp)

        # eliminar aristas que formen ciclos

        # for i in verticeTemp:
        #     for j in i:
        #         print(j.getNombre())
        #     print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        # for i in conjuntoAristas:
        #     for j in i:
        #         print(j.getOrigen(),"---",j.getDestino(),"---->", j.getPeso())
        #     print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")

        #  for i in uniones:

    # def boruvka(self):
    #     copiaVertices = copy(self.listaVertices)
    #     copiaAristas = copy(self.listaAristas)
    #     aristasBoruvka = []
    #     listaConjuntos = []
    #     bandera = True
    #     cantidad = 0
    #     while(cantidad > 1 or bandera):
    #         for vertice in copiaVertices:
    #             self.operacinesCunjuntosB(vertice, listaConjuntos, aristasBoruvka, copiaAristas)
    #         bandera = False
    #         cantidad = self.cantidadConjuntos(listaConjuntos)
    #     return aristasBoruvka
    #
    # def cantidadConjuntos(self,listaConjuntos):
    #     cantidad = 0
    #     for conjunto in listaConjuntos:
    #         if len(conjunto) > 0:
    #             cantidad = cantidad + 1
    #     return cantidad
    #
    # def ordenar(self, aristas):
    #     for i in range(len(aristas)):
    #         for j in range(len(aristas)):
    #                 if aristas[i].getPeso() < aristas[j].getPeso():
    #                     temp = aristas[i]
    #                     aristas[i] = aristas [j]
    #                     aristas[j] = temp
    # def buscarMenor(self, vertice, copiaAristas):
    #     temp = []
    #     for adyacencia in vertice.getListaAdyacentes():
    #         for arista in copiaAristas:
    #             if arista.getOrigen() == vertice.getNombre() and arista.getDestino() == adyacencia:
    #                 temp.append(arista)
    #     if temp:
    #         self.ordenar(temp)
    #
    #         vertice.getListaAdyacentes().remove(temp[0].getDestino())
    #         return temp[0]
    #     return None
    #
    #
    # def operacinesCunjuntosB(self, vertice, listaConjuntos, aristasBoruvka, copiaAristas):
    #     encontrado1 = -1
    #     encontrado2 = -1
    #     menor = self.buscarMenor(vertice, copiaAristas)
    #
    #     if not menor == None:
    #         if not listaConjuntos:
    #             listaConjuntos.append({menor.getOrigen(), menor.getDestino()})
    #             aristasBoruvka.append(menor)
    #         else:
    #             for i in range(len(listaConjuntos)):
    #                 if (menor.getOrigen() in listaConjuntos[i]) and (menor.getDestino() in listaConjuntos[i]):
    #                     return False
    #
    #             for i in range(len(listaConjuntos)):
    #                 if menor.getOrigen() in listaConjuntos[i]:
    #                     encontrado1 = i
    #                 if menor.getDestino() in listaConjuntos[i]:
    #                     encontrado2= i
    #
    #             if encontrado1 != -1 and encontrado2 != -1:
    #                 if encontrado1 != encontrado2:
    #                     listaConjuntos[encontrado1].update(listaConjuntos[encontrado2])
    #                     listaConjuntos[encontrado2].clear()
    #                     aristasBoruvka.append(menor)
    #
    #             if encontrado1 != -1  and encontrado2 == -1:
    #                 listaConjuntos[encontrado1].update(menor.getOrigen())
    #                 listaConjuntos[encontrado1].update(menor.getDestino())
    #                 aristasBoruvka.append(menor)
    #
    #             if encontrado1 == -1 and encontrado2 != -1:
    #                 listaConjuntos[encontrado2].update(menor.getOrigen())
    #                 listaConjuntos[encontrado2].update(menor.getDestino())
    #                 aristasBoruvka.append(menor)
    #
    #             if encontrado1 == -1 and encontrado2 == -1:
    #                 listaConjuntos.append({menor.getOrigen(), menor.getDestino()})
    #                 aristasBoruvka.append(menor)


    # dijkstra
    def dijkstra(self, origen, destino):
        verticesAux = []
        verticesD = []
        caminos = self.ordenarDijkstra(origen, verticesAux)
        cont = 0

        # for i in caminos:
        #     print("La distancia mínima a " + self.listaVertices[cont].getNombre() + " es " + str(i))
        #     cont += 1
        #
        self.rutas(verticesD, verticesAux, destino, origen)
        # print("El camino más corto de " + origen + " a " + destino + " es: ")
        # print(verticesD)
        aristas = []
        for i in range(len(verticesD)-1):
            aristas.append(self.obtenerArista(verticesD[i],verticesD[i+1], self.listaAristas))
        return aristas

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

    # dijkstraBlock
    def dijkstraBlock(self, origen, destino):
        self.setCaminoBloqueado(self.dijkstra(origen, destino))
        verticesAux = []
        verticesD = []
        caminos = self.ordenarDijkstraBlock(origen, verticesAux)
        cont = 0
        self.rutas(verticesD, verticesAux, destino, origen)
        aristas = []
        for i in range(len(verticesD) - 1):
            aristas.append(self.obtenerArista(verticesD[i], verticesD[i + 1], self.listaAristas))
        return aristas

    def ordenarDijkstraBlock(self, origen, verticesAux):
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
                if self.viaBloqueada(self.obtenerArista(menorAux.getNombre(), adyacencia, self.listaAristas)):
                    indiceNuevo = self.listaVertices.index(self.obtenerVertice(adyacencia, self.listaVertices))
                    arista = self.verificarAristaBlock(menorAux.getNombre(), adyacencia)
                    if caminos[indiceNuevo] > valorActual + arista.getPeso():
                        caminos[indiceNuevo] = valorActual + arista.getPeso()
                        verticesAux[indiceNuevo] = self.listaVertices[indice].getNombre()

        return caminos

    def verificarAristaBlock(self, origen, destino):
        for i in range(len(self.listaAristas)):
            if self.viaBloqueada(self.listaAristas[i]):
                if origen == self.listaAristas[i].getOrigen() and destino == self.listaAristas[i].getDestino():
                    return self.listaAristas[i]

        return None

    def viaBloqueada(self, arista):
        for i in self.caminoBloqueado:
            arista == i
            return False
        return True