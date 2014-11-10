
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
        if sorted(partition0) != sorted(partition1):
            partition0.extend(partition1)
            partitions.remove(partition1)
            minimum_spanning_tree.append(min_edge)
        copy.remove(min_edge)
    return minimum_spanning_tree


# ===============================================================
def read_graph_file(a_file):
    """ Lee un archivo en el formato a,b,c donde a y b son 
        los nombres del vertice y c es el costo de la arista 
        entre ellos.
        :param a_file: El nombre del archivo a leer
        :return: El grafo parseado
    """
    inf = open(a_file, 'r')
    graph = []
    for c, line in enumerate(inf):
        items = line.upper().strip().split(',')
        if len(items) != 3: raise Error('Error de formato en linea %i: %s' % (c , line))
        graph.append(Edge(nodes=sorted(items[:2]), cost=int(items[2])))
    return graph


# ===============================================================
if __name__ == '__main__':
    """ Punto de entrada de la consola
    """
    minimum_spanning_tree = kruskal(read_graph_file('graph.txt'))
    solution = read_graph_file('solution.txt')
    by_edges = lambda(e) : ''.join(e.nodes)
    minimum_spanning_tree.sort(key=by_edges)
    solution.sort(key=by_edges)
    if minimum_spanning_tree != solution:
        for g, s in zip(minimum_spanning_tree, solution):
            print 'g: %s, s:%s' % (g, s)
    else:
        print 'OK!'
