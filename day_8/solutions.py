from .parser import Coordinate
from itertools import combinations
from math import prod
import networkx as nx
import matplotlib.pyplot as plt

def part_1(boxes: set[Coordinate], connections: int) -> int:
    possible_edges = sorted([(first, second, square_distance(first, second)) for first, second in combinations(boxes, 2)], key=lambda x: x[2])
    graph = nx.Graph()

    for i in range(connections):
        current_edge = possible_edges[i]

        graph.add_edge(current_edge[0], current_edge[1])

    #plt.subplot(111)
    #nx.draw(graph, with_labels=True)
    #plt.show()

    return prod([len(c) for c in sorted(nx.connected_components(graph), key=len, reverse=True)[:3]])
    
def part_2(boxes: set[Coordinate]) -> int:
    possible_edges = sorted([(first, second, square_distance(first, second)) for first, second in combinations(boxes, 2)], key=lambda x: x[2])
    graph = nx.Graph()
    graph.add_nodes_from(boxes)

    for i in range(len(possible_edges)):
        current_edge = possible_edges[i]
        graph.add_edge(current_edge[0], current_edge[1])
        if(nx.is_connected(graph)):
            return current_edge[0].x * current_edge[1].x

def square_distance(first: Coordinate, second: Coordinate) -> int:
    return (first.x - second.x) ** 2 + (first.y - second.y) ** 2 + (first.z - second.z) ** 2