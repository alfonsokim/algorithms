
from collections import namedtuple

Edge = namedtuple('Edge', 'nodes, cost')

graph = [Edge(nodes=['A', 'B'], cost=10),
         Edge(nodes=['A', 'C'], cost=15),
         Edge(nodes=['A', 'D'], cost=8),
         Edge(nodes=['B', 'D'], cost=20),
         Edge(nodes=['C', 'D'], cost=3)]

print graph

def get_minimum_edge(graph):
    graph.sort(key=lambda(g): g.cost)
    return graph[0]

def get_nodes(graph):
    nodes = set()
    for edge in graph:
        [nodes.add(v) for v in edge.nodes]
    return nodes

def find_partition(partitions, node):
    for partition in partitions:
        if node in partition:
            return partition

def kruskal(graph):
    copy = list(graph)
    partitions = [[v for v in get_nodes(graph)]]
    while len(partitions[0]) != 0:
        min_edge = get_minimum_edge(graph)
        partition = find_partition(partitions, min_edge)
        

nodes = get_nodes(graph)

print nodes

#print 'sorted:', get_minimum_edge(graph)

kruskal(graph)

