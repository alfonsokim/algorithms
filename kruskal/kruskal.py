
from collections import namedtuple

""" Graph structure
"""
Edge = namedtuple('Edge', 'nodes, cost')

""" Just in case
"""
test_graph = [Edge(nodes=['A', 'B'], cost=10),
              Edge(nodes=['A', 'C'], cost=15),
              Edge(nodes=['A', 'D'], cost=8),
              Edge(nodes=['B', 'C'], cost=1),
              Edge(nodes=['B', 'D'], cost=20),
              Edge(nodes=['C', 'D'], cost=3)]


# ===============================================================
def get_nodes(graph):
    """ Returns the name of all the vertices in the graph.
        Could be inlined in the code, was added for clarity.
        :param graph: The graph to read
        :return: The name of the vertices
    """
    return set([v for edge in graph for v in edge.nodes])


# ===============================================================
def find_partition(partitions, node):
    """ Finds the partition of the graph where node is.
        Could be inlined in the code, was added for clarity.
        :param partitions: The list of partitions 
        :param node: The node to look for
        :return: The partition where the node is
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
        minimum_edge = sorted(copy, key=lambda g: g.cost)[0]
        nodes = minimum_edge.nodes
        partition0 = find_partition(partitions, nodes[0])
        partition1 = find_partition(partitions, nodes[1])
        if sorted(partition0) != sorted(partition1):
            partition0.extend(partition1)
            partitions.remove(partition1)
            minimum_spanning_tree.append(minimum_edge)
        copy.remove(minimum_edge)
    return minimum_spanning_tree


# ===============================================================
def read_graph_file(file_name):
    """ Utilitary method. This is not part of the algorithm.
        Reads a file where each line has the format a,b,c. 
        a and b are the vertex names, c is the cost of the edge between them.
        :param file_name: The name of the file to read
        :return: The list of the edges of the graph
    """
    def _line_to_edge(index, line):
        """ Parse each line """
        items = line.upper().strip().split(',')
        if len(items) != 3: 
            raise Exception('Invalid line %i: %s' % (index, line))
        return Edge(nodes=items[:2], cost=int(items[2]))
    # -----------------------------------------------------------
    graph_data = open(file_name, 'r')
    graph = [_line_to_edge(c, line) for c, line in enumerate(graph_data)]
    graph_data.close()
    return graph


# ===============================================================
if __name__ == '__main__':
    """ Main entry point
        Reads the test file and check the result of the algorithm
    """
    minimum_spanning_tree = kruskal(read_graph_file('graph.txt'))
    path = '->'.join(['%s%s' % tuple(n.nodes) for n in minimum_spanning_tree])
    assert path == 'BC->KL->OR->EF->KP->OP->OS->RV->IM->AC->LM->WX->DE->CF->DG->FH->QT->JO->KQ->GJ->TY->NU->SX->UY->YZ'
    print 'OK!'
