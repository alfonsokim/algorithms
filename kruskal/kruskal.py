
from collections import namedtuple

""" Estructura del grafo, representa una arista
"""
Edge = namedtuple('Edge', 'nodes, cost')

""" Grafo de pruebas
"""
test_graph = [Edge(nodes=['A', 'B'], cost=10),
              Edge(nodes=['A', 'C'], cost=15),
              Edge(nodes=['A', 'D'], cost=8),
              Edge(nodes=['B', 'C'], cost=1),
              Edge(nodes=['B', 'D'], cost=20),
              Edge(nodes=['C', 'D'], cost=3)]

stations = [Edge(nodes=['B', 'C'], cost=13),
            Edge(nodes=['C', 'A'], cost=23),
            Edge(nodes=['E', 'D'], cost=24),
            Edge(nodes=['E', 'F'], cost=20),
            Edge(nodes=['F', 'C'], cost=25),
            Edge(nodes=['G', 'D'], cost=25),
            Edge(nodes=['H', 'F'], cost=25),
            Edge(nodes=['J', 'G'], cost=29),
            Edge(nodes=['L', 'K'], cost=19),
            Edge(nodes=['M', 'I'], cost=22),
            Edge(nodes=['M', 'L'], cost=23),
            Edge(nodes=['O', 'J'], cost=27),
            Edge(nodes=['P', 'K'], cost=20),
            Edge(nodes=['P', 'O'], cost=20),
            Edge(nodes=['Q', 'K'], cost=27),
            Edge(nodes=['R', 'O'], cost=19),
            Edge(nodes=['S', 'O'], cost=20),
            Edge(nodes=['T', 'Q'], cost=25),
            Edge(nodes=['U', 'N'], cost=31),
            Edge(nodes=['V', 'R'], cost=20),
            Edge(nodes=['X', 'S'], cost=33),
            Edge(nodes=['X', 'W'], cost=23),
            Edge(nodes=['Y', 'T'], cost=29),
            Edge(nodes=['Y', 'U'], cost=34),
            Edge(nodes=['Z', 'Y'], cost=38)]


# ===============================================================
def get_minimum_edge(graph):
    """ Encuentra la arista minima en un grafo
        :param graph: El grafo a econtorar la arista con costo minimo
        :return: El vertice con costo mas bajo
    """
    graph.sort(key=lambda(g): g.cost)
    return graph[0]


# ===============================================================
def get_nodes(graph):
    """ Encuentra todos los nombres de los vertices en un grafo
        :param graph: El grafo a encontrar sus vertices
        :return: El nombre de los nodos en el grafo
    """
    nodes = set()
    for edge in graph:
        [nodes.add(v) for v in edge.nodes]
    return nodes


# ===============================================================
def find_partition(partitions, node):
    """ Encuentra la particion donde se encuentra un nodo
        :param partitions:  La lista de particiones a buscar
        :param node:    El nodo a buscar en la lista
        :return:        La particion en la que se encuentra el nodo
    """
    for partition in partitions:
        if node in partition:
            return partition


# ===============================================================
def kruskal(graph):
    """ Ejecuta el algoritmo de kruskal para encontrar el arbol
        de cobertura minima de un grafo
        :param graph: El grafo a analizar
        :return: El arbol de cobertura minima del grafo
    """
    copy = list(graph)
    partitions = [[v] for v in get_nodes(graph)]
    minimum_spanning_tree = []
    while copy and partitions:
        min_edge = get_minimum_edge(copy)
        nodes = min_edge.nodes
        partition0 = find_partition(partitions, nodes[0])
        partition1 = find_partition(partitions, nodes[1])
        partition0.extend(partition1)
        partitions.remove(partition1)
        copy.remove(min_edge)
        minimum_spanning_tree.append(min_edge)
    return minimum_spanning_tree


# ===============================================================
def read_graph_file(a_file):
    """ Lee un archivo en el formato a,b,c donde a y b son 
        los nombres del vertice y c es el costo de la arista 
        entre ellos.
        :param a_file: El nombre del archivo a leer
        :return: El grafo parseado
    """
    pass


# ===============================================================
if __name__ == '__main__':
    print kruskal(stations)

