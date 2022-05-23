"""——————————————————————————————————————————————
    console method menu
——————————————————————————————————————————————"""

from helpers.Keyboard import *
from clases.Grafo import *


class Menu:

    """—————————————————————————————————————————————CONSTRUCTOR——————————————————————————————————————————————————————"""

    def __init__(self):
        self.name = ''
        self.grafo = Grafo()

    """—————————————————————————————————————————————SALIDA-PANTALLA——————————————————————————————————————————————————"""

    def menuInicio(self):

        self.inicializarGrafo()
        # self.grafo_nociclos_conexo_nodirigido()
        self.grafo_ciclos_conexo_dirigido()
        self.grafo.prim("Manizales")

        # self.grafo.caminoMasCorto("Cali", "Barranquilla")

        print('▛▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▜\n' \
              '▌▓▒░     01. Iniciar     ░▒▓█▓▒░     02. Opciones     ░▒▓█▓▒░     03. Salir     ░▒▓▐\n' \
              '▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟')

        opcion = {
            1: self.ejecutar, 2: self.menuOpciones, 3: self.salir
        }
        i = Keyboard.readIntRangeDefaultErrorMessage("Ingrese una opcion: ", 1, 3)
        opcion[i]()



    def menuOpciones(self):
        while True:
            print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")

            print(
                "\nOPCIONES"
                "\n01 — Ejecutar todos              02 — Elejir grafo                   03 — Ver vértices           04 — Ver aristas"
                "\n05 — Ver adyacencias             06 — Ver vértices de < a >          07 — Ver vértices de > a <  08 — Ver grados vertices"
                "\n09 — Vértice mayor grado         10 — Ver promedio lista adyacencias 11 — Ver pozos              12 — Ver fuentes"
                "\n13 — Ver promedio peso aristas   14 — Ver arista mayor peso          15 — Ver arista menor peso  16 — Ver vértice adyacente"
                "\n17 — Ver lista adyacentes        18 — Ver vértices no contemplados   19 — Ver adyacia más comun  20 — Salir"
                "\n00 — Volver"
            )
            opcion = {
                1: self.ejecutar,                   2: self.tipoGrafo,                           3: self.grafo.mostrarVertices,          4: self.grafo.mostrarAristas,
                5: self.grafo.mostrarAdyacencias,       6: self.minMaxAristas,                       7: self.maxMinAristas,                  8: self.grafo.mostrarGradoVertices,
                9: self.grafo.verticeMayorGrado,        10: self.grafo.promedioListaAdyacencias,     11: self.grafo.mostrarPozos,            12: self.grafo.mostrarFuentes,
                13: self.grafo.promedioPesoAristas,     14: self.grafo.aristaMayorPeso,              15: self.grafo.aristaMenorPeso,         16: self.grafo.verticeAdyacente,
                17: self.grafo.mostrarListaAdyacentes,  18: self.grafo.mostrarVerticesNoContemplados,19: self.grafo.mostarAdyacenciaMasComun,20:self.salir
            }
            i = Keyboard.readIntRangeDefaultErrorMessage("Ingrese una opcion: ", 1, 20)
            if i != 1:
                print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
            opcion[i]()

    def salir(self):
        s = '▛▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▜\n' \
            '▌▓▓▒▒▒░                       ¡GRACIAS POR USAR EL PROGRAMA!                      ░▒▒▒▓▓▐\n' \
            '▌▓▓▒▒▒░                                                                           ░▒▒▒▓▓▐\n' \
            '▌▓▓▒▒▒░                             Desarrollado por:                             ░▒▒▒▓▓▐\n' \
            '▌▓▓▒▒▒░                                                                           ░▒▒▒▓▓▐\n' \
            '▌▓▓▒▒▒░                      Daniel Felipe Franco Rincon                          ░▒▒▒▓▓▐\n' \
            '▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟'
        print(s)
        sys.exit()




    """——————————————————————01——————————————————————EJECUCIÓN———————————————————————————————————————————————————————"""

    def ejecutar(self):
        self.todosMetodos()
        self.salir()


    def todosMetodos(self):
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print("                                TODAS LAS FUNCIONES")
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        self.tipoGrafo()
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        self.grafo.mostrarVertices()
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        self.grafo.mostrarAristas()
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        self.grafo.mostrarAdyacencias()
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        self.minMaxAristas()
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        self.maxMinAristas()
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        self.grafo.mostrarGradoVertices()
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        self.grafo.verticeMayorGrado()
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        self.grafo.promedioListaAdyacencias()
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        self.grafo.mostrarPozos()
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        self.grafo.mostrarFuentes()
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        self.grafo.promedioPesoAristas()
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        self.grafo.aristaMayorPeso()
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        self.grafo.aristaMenorPeso()
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        self.grafo.verticeAdyacente()
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        self.grafo.mostrarListaAdyacentes()
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        self.grafo.mostrarVerticesNoContemplados()
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        self.grafo.mostarAdyacenciaMasComun()

    # graph type
    def tipoGrafo(self):
        print("                                    GRAFOS"
             "\n1) Grafo dirigido/sin ciclos/conexo     5) Grafo no dirigido/sin ciclos/conexo" 
             "\n2) Grafo dirigido/sin ciclos/no conexo  6) Grafo no dirigido/sin ciclos/no conexo" 
             "\n3) Grafo dirigido/con ciclos/conexo     7) Grafo no dirigido/con ciclos/conexo" 
             "\n4) Grafo dirigido/con ciclos/no conexo  8) Grafo nodirigido/con ciclos/no conexo "
             )
        opcion = {
            1: self.grafo_nociclos_conexo_dirigido, 5: self.grafo_nociclos_conexo_nodirigido,
            2: self.grafo_nociclos_noconexo_dirigido, 6: self.grafo_nociclos_noconexo_nodirigido,
            3: self.grafo_ciclos_conexo_dirigido, 7: self.grafo_ciclos_conexo_nodirigido,
            4: self.grafos_ciclos_noconexo_dirigido, 8: self.grafos_ciclos_noconexo_nodirigido
        }
        i = Keyboard.readIntRangeDefaultErrorMessage("Ingrese del tipo de grafo que desea crear: ", 1, 8)
        opcion[i]()

    def minMaxAristas(self):
        self.grafo.minMaxAristas(0)
        print("                                  MENOR A MAYOR")
        self.grafo.mostrarAristas()

    def maxMinAristas(self):
        self.grafo.maxMinAristas(0)
        print("                                  MAYOR A MENOR")
        self.grafo.mostrarAristas()

    """—————————————————————————————————————————————Grafos/Vertices——————————————————————————————————————————————————"""

    def inicializarGrafo(self):
        # creation of vertices
        self.grafo.ingresarVertice('Pereira')
        self.grafo.ingresarVertice('Armenia')
        self.grafo.ingresarVertice('Manizales')
        self.grafo.ingresarVertice('Cali')
        self.grafo.ingresarVertice('Bogota')
        self.grafo.ingresarVertice('Cututa')
        self.grafo.ingresarVertice('Barranquilla')
        self.grafo.ingresarVertice('Cartagena')
        self.grafo.ingresarVertice('Medellin')

    """———————————————————————————————————————————————Grafos/Aristas—————————————————————————————————————————————————"""

    # graph_nocycles_connected_directed
    def grafo_nociclos_conexo_dirigido(self):
        self.grafo.setListaAristas([])
        self.name = "grafo/dirigido/conexo/sin ciclos"
        self.grafo.ingresarArista('Manizales','Pereira',1)
        self.grafo.ingresarArista('Manizales', 'Bogota', 8)
        self.grafo.ingresarArista('Manizales', 'Medellin', 4)
        self.grafo.ingresarArista('Pereira','Armenia',3)
        self.grafo.ingresarArista('Armenia','Cali',4)
        self.grafo.ingresarArista('Armenia','Bogota',3)
        self.grafo.ingresarArista('Medellin','Bogota',4)
        self.grafo.ingresarArista('Bogota','Cututa',7)
        self.grafo.ingresarArista('Bogota','Cartagena',6)
        self.grafo.ingresarArista('Cartagena','Barranquilla',1)
        self.grafo.ingresarArista('Barranquilla','Cututa',12)

    # graph_no cycles_no connected_directed
    def grafo_nociclos_noconexo_dirigido(self):
        self.grafo.setListaAristas([])
        self.name = "grafo/dirigido/no conexo/sin ciclos"
        self.grafo.ingresarArista('Manizales', 'Pereira', 1)
        self.grafo.ingresarArista('Manizales', 'Bogota', 8)
        self.grafo.ingresarArista('Manizales', 'Medellin', 4)
        self.grafo.ingresarArista('Pereira', 'Armenia', 3)
        self.grafo.ingresarArista('Armenia', 'Cali', 4)
        self.grafo.ingresarArista('Armenia', 'Bogota', 3)
        self.grafo.ingresarArista('Medellin', 'Bogota', 4)
        self.grafo.ingresarArista('Cartagena', 'Barranquilla', 1)
        self.grafo.ingresarArista('Barranquilla', 'Cututa', 12)

    # graph_cycles_connected_directed
    def grafo_ciclos_conexo_dirigido(self):
        self.grafo.setListaAristas([])
        self.name = "grafo/dirigido/conexo/ciclos"
        self.grafo.ingresarArista('Manizales','Pereira',1)
        self.grafo.ingresarArista('Bogota','Manizales', 8)
        self.grafo.ingresarArista('Manizales','Medellin',4)
        self.grafo.ingresarArista('Pereira','Armenia',3)
        self.grafo.ingresarArista('Armenia','Cali',4)
        self.grafo.ingresarArista('Armenia','Bogota',3)
        self.grafo.ingresarArista('Medellin','Bogota',4)
        self.grafo.ingresarArista('Bogota','Cututa',7)
        self.grafo.ingresarArista('Bogota','Cartagena',6)
        self.grafo.ingresarArista('Cartagena','Barranquilla',1)
        self.grafo.ingresarArista('Barranquilla','Cututa',12)

    # graph_cycles_no connected_directed
    def grafos_ciclos_noconexo_dirigido(self):
        self.grafo.setListaAristas([])
        self.name = "grafo/dirigido/no conexo/ciclos"
        self.grafo.ingresarArista('Manizales','Pereira',1)
        self.grafo.ingresarArista('Bogota','Manizales',8)
        self.grafo.ingresarArista('Manizales','Medellin',4)
        self.grafo.ingresarArista('Pereira','Armenia',3)
        self.grafo.ingresarArista('Armenia','Cali',4)
        self.grafo.ingresarArista('Armenia','Bogota',3)
        self.grafo.ingresarArista('Medellin','Bogota',4)
        self.grafo.ingresarArista('Cututa','Cartagena',13)
        self.grafo.ingresarArista('Cartagena','Barranquilla',1)
        self.grafo.ingresarArista('Barranquilla','Cututa',12)

    # graph_cycles_connected_no directed
    def grafo_ciclos_conexo_nodirigido(self):
        self.grafo.setListaAristas([])
        self.name = "grafo/no dirigido/conexo/ciclos"
        self.grafo.ingresarArista('Manizales','Pereira',1)
        self.grafo.ingresarArista('Pereira','Manizales',1)
        self.grafo.ingresarArista('Manizales','Bogota',8)
        self.grafo.ingresarArista('Bogota','Manizales',8)
        self.grafo.ingresarArista('Manizales','Medellin',4)
        self.grafo.ingresarArista('Medellin','Manizales',4)
        self.grafo.ingresarArista('Pereira','Armenia',3)
        self.grafo.ingresarArista('Armenia', 'Pereira',3)
        self.grafo.ingresarArista('Armenia','Cali',4)
        self.grafo.ingresarArista('Cali','Armenia',4)
        self.grafo.ingresarArista('Armenia','Bogota',3)
        self.grafo.ingresarArista('Bogota','Armenia',3)
        self.grafo.ingresarArista('Medellin','Bogota',4)
        self.grafo.ingresarArista('Bogota','Medellin',4)
        self.grafo.ingresarArista('Bogota','Cututa',7)
        self.grafo.ingresarArista('Cututa','Bogota',7)
        self.grafo.ingresarArista('Bogota','Cartagena',6)
        self.grafo.ingresarArista('Cartagena','Bogota',6)
        self.grafo.ingresarArista('Cartagena','Barranquilla',1)
        self.grafo.ingresarArista('Barranquilla','Cartagena',1)
        self.grafo.ingresarArista('Barranquilla','Cututa',12)
        self.grafo.ingresarArista('Cututa','Barranquilla',12)

    # graph_cycles_no connected_no directed
    def grafos_ciclos_noconexo_nodirigido(self):
        self.grafo.setListaAristas([])
        self.name = "grafo/no dirigido/no conexo/ciclos"
        self.grafo.ingresarArista('Manizales','Pereira',1)
        self.grafo.ingresarArista('Pereira','Manizales',1)
        self.grafo.ingresarArista('Manizales','Bogota',8)
        self.grafo.ingresarArista('Bogota','Manizales',8)
        self.grafo.ingresarArista('Manizales','Medellin',4)
        self.grafo.ingresarArista('Medellin','Manizales',4)
        self.grafo.ingresarArista('Pereira','Armenia',3)
        self.grafo.ingresarArista('Armenia', 'Pereira',3)
        self.grafo.ingresarArista('Armenia','Cali',4)
        self.grafo.ingresarArista('Cali','Armenia',4)
        self.grafo.ingresarArista('Armenia','Bogota',3)
        self.grafo.ingresarArista('Bogota','Armenia',3)
        self.grafo.ingresarArista('Medellin','Bogota',4)
        self.grafo.ingresarArista('Bogota','Medellin',4)
        self.grafo.ingresarArista('Cartagena','Barranquilla',1)
        self.grafo.ingresarArista('Barranquilla','Cartagena',1)
        self.grafo.ingresarArista('Barranquilla','Cututa',12)
        self.grafo.ingresarArista('Cututa','Barranquilla',12)

    # graph_no cycles_connected_no directed
    def grafo_nociclos_conexo_nodirigido(self):
        self.grafo.setListaAristas([])
        self.name = "grafo/no dirigido/conexo/sin ciclos"
        self.grafo.ingresarArista('Manizales','Pereira',1)
        self.grafo.ingresarArista('Pereira','Manizales',1)
        self.grafo.ingresarArista('Manizales','Bogota',8)
        self.grafo.ingresarArista('Bogota','Manizales',8)
        self.grafo.ingresarArista('Manizales','Medellin',4)
        self.grafo.ingresarArista('Medellin','Manizales',4)
        self.grafo.ingresarArista('Pereira','Armenia',3)
        self.grafo.ingresarArista('Armenia', 'Pereira',3)
        self.grafo.ingresarArista('Armenia','Cali',4)
        self.grafo.ingresarArista('Cali','Armenia',4)
        self.grafo.ingresarArista('Bogota','Cartagena',4)
        self.grafo.ingresarArista('Cartagena','Bogota',6)
        self.grafo.ingresarArista('Cartagena','Barranquilla',1)
        self.grafo.ingresarArista('Barranquilla','Cartagena',1)
        self.grafo.ingresarArista('Barranquilla','Cututa',12)
        self.grafo.ingresarArista('Cututa','Barranquilla',12)

    # graph_no cycles_no connected_no directed
    def grafo_nociclos_noconexo_nodirigido(self):
        self.grafo.setListaAristas([])
        self.name = "grafo/no dirigido/no conexo/sin ciclos"
        self.grafo.ingresarArista('Manizales','Pereira',1)
        self.grafo.ingresarArista('Pereira','Manizales',1)
        self.grafo.ingresarArista('Manizales','Bogota',8)
        self.grafo.ingresarArista('Bogota','Manizales',8)
        self.grafo.ingresarArista('Manizales','Medellin',4)
        self.grafo.ingresarArista('Medellin','Manizales',4)
        self.grafo.ingresarArista('Pereira','Armenia',3)
        self.grafo.ingresarArista('Armenia', 'Pereira',3)
        self.grafo.ingresarArista('Armenia','Cali',4)
        self.grafo.ingresarArista('Cali','Armenia',4)
        self.grafo.ingresarArista('Cartagena','Barranquilla',1)
        self.grafo.ingresarArista('Barranquilla','Cartagena',1)
        self.grafo.ingresarArista('Barranquilla','Cututa',12)
        self.grafo.ingresarArista('Cututa','Barranquilla',12)