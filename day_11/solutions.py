import networkx as nx
import matplotlib.pyplot as plt


def part_1(device_outputs: list[tuple[str, str]]) -> int:
    graph = nx.DiGraph()        
    graph.add_edges_from(device_outputs)
    
    #nx.draw(graph, with_labels=True)
    #plt.show()

    return len(list(nx.all_simple_paths(graph, source='you', target='out')))

def part_2(device_outputs: list[tuple[str, str]], filename: str) -> int:
    graph = nx.DiGraph()        
    graph.add_edges_from(device_outputs)

    svr_fft = count_paths(graph, 'svr', 'fft')
    fft_dac = count_paths(graph, 'fft', 'dac')
    dac_out = count_paths(graph, 'dac', 'out')

    save_graph(graph, filename)

    return svr_fft * fft_dac * dac_out

def count_paths(graph, source, target):
    topological_order = list(nx.topological_sort(graph))
    counts = {node: 0 for node in topological_order}
    counts[source] = 1

    for node in topological_order:
        if counts[node] > 0:
            for successor in graph.successors(node):
                counts[successor] += counts[node]
    
    return counts[target]

def save_graph(graph, filename: str) -> None:
    plt.figure(figsize=(30, 32))
    pos = nx.spring_layout(graph, k=2, iterations=100)
    nx.draw(graph, pos, with_labels=True, node_size=800, font_size=8, arrows=True)    
    plt.savefig(filename, dpi=300)
    plt.close()