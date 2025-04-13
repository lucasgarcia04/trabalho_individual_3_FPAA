import matplotlib.pyplot as plt
import networkx as nx
from main import hamiltonian_path

def draw_graph(graph):
    G = nx.Graph()
    for v in graph:
        for u in graph[v]:
            G.add_edge(v, u)

    pos = nx.spring_layout(G)
    path = hamiltonian_path(graph)

    edge_colors = []
    for edge in G.edges():
        if path and (edge in zip(path, path[1:]) or (edge[1], edge[0]) in zip(path, path[1:])):
            edge_colors.append('red')
        else:
            edge_colors.append('black')

    nx.draw(G, pos, with_labels=True, edge_color=edge_colors, node_color='skyblue', node_size=600)
    plt.title('Grafo com Caminho Hamiltoniano' if path else 'Grafo sem Caminho Hamiltoniano')
    plt.show()

if __name__ == '__main__':
    graph = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [1, 2]
    }
    draw_graph(graph)
