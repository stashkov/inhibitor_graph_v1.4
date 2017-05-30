import networkx as nx


def example30():
    G = nx.DiGraph()

    G.add_node(1, info='Bacteria')
    G.add_node(2, info='Epithelial cells')
    G.add_node(3, info='Complement')
    G.add_node(4, info='Ag-Ab complex')
    G.add_node(5, info='Pro-inflamatory cytokines (IL-1,6,TNF-alpha, beta)')
    G.add_node(6, info='Recruited PMNs')
    G.add_node(7, info='Activated Phagocytic Cells')
    G.add_node(8, info='Other antibodies')
    G.add_node(9, info='Complement fixing antibodies IgG, IgM')
    G.add_node(10, info='Macrophages')
    G.add_node(11, info='Th1 cells')
    G.add_node(12, info='T0 cells')
    G.add_node(13, info='Th2 cells')
    G.add_node(14, info='B cells')
    G.add_node(15, info='Th1 related cytokines (IFN- Gamma, TNF-beta, IL-2)')
    G.add_node(16, info='Th2 related cytokines (IL-4, 10,13)')
    G.add_node(17, info='Dendritic cells')
    G.add_node(18, info='Phagocytosis')

    G.add_edge(1, 17, weight=0)
    G.add_edge(1, 4, weight=0)
    G.add_edge(1, 2, weight=0)
    G.add_edge(1, 3, weight=0)

    G.add_edge(2, 5, weight=0)

    G.add_edge(3, 7, weight=0)

    G.add_edge(4, 3, weight=0)
    G.add_edge(4, 7, weight=0)

    G.add_edge(5, 17, weight=0)
    G.add_edge(5, 6, weight=0)
    G.add_edge(5, 10, weight=0)

    G.add_edge(6, 7, weight=0)

    G.add_edge(7, 5, weight=0)

    G.add_edge(8, 4, weight=0)
    G.add_edge(8, 8, weight=0)

    G.add_edge(9, 9, weight=0)
    G.add_edge(9, 3, weight=0)

    G.add_edge(10, 7, weight=0)

    G.add_edge(11, 15, weight=0)

    G.add_edge(12, 11, weight=0)
    G.add_edge(12, 13, weight=0)

    G.add_edge(13, 14, weight=0)
    G.add_edge(13, 16, weight=0)

    G.add_edge(14, 8, weight=0)
    G.add_edge(14, 9, weight=0)

    G.add_edge(15, 10, weight=0)
    G.add_edge(15, 17, weight=0)
    G.add_edge(15, 11, weight=0)
    G.add_edge(15, 16, weight=1)

    G.add_edge(16, 15, weight=1)
    G.add_edge(16, 5, weight=1)
    G.add_edge(16, 17, weight=0)
    G.add_edge(16, 13, weight=0)

    G.add_edge(17, 15, weight=0)
    G.add_edge(17, 16, weight=0)

    G.add_edge(18, 1, weight=1)
    return G


def generate_graph_test_loops():
    G = nx.DiGraph()
    G.add_edge(1, 2, weight=0)
    G.add_edge(2, 3, weight=0)
    G.add_edge(3, 4, weight=0)
    G.add_edge(3, 2, weight=1)
    return G


def composite_graph_1():
    G = nx.DiGraph()
    G.add_edge(1, 4, weight=0)
    G.add_edge(2, 4, weight=0)
    G.add_edge(3, 4, weight=0)
    G.add_edge(4, 5, weight=0)
    G.add_edge(4, 6, weight=0)
    G.add_edge(7, 6, weight=0)
    G.add_edge(6, 8, weight=0)
    return G


def composite_graph_1():
    G = nx.DiGraph()
    G.add_edge(1, 3, weight=0)
    G.add_edge(1, 4, weight=0)
    G.add_edge(2, 4, weight=0)
    return G


def generate_barabasi(n):
    import random
    G = nx.barabasi_albert_graph(n, 2, seed=14)
    # set info ( information about a node )
    for i in range(len(G.nodes())):
        G.node[i]['info'] = '_%s_' % i

    percent_chance_of_inhibited_edge = 25
    for u, v, d in G.edges(data=True):
        d['weight'] = random.choice([0]*(100-percent_chance_of_inhibited_edge) + [1]*percent_chance_of_inhibited_edge)

    diff = list(set(G.edges()) - set(G.to_directed()))
    G = G.to_directed()
    for u, v in diff:
        G.remove_edge(u, v)
    return G


def generate_graph():
    G = nx.DiGraph()
    G.add_edge(1, 2, weight=0)
    G.add_edge(3, 2, weight=1)
    G.add_edge(3, 6, weight=0)
    G.add_edge(2, 4, weight=1)
    G.add_edge(5, 4, weight=0)

    G.node[1]['info'] = 'A'
    G.node[3]['info'] = 'B'
    G.node[2]['info'] = 'C'
    G.node[4]['info'] = 'E'
    G.node[5]['info'] = 'D'
    G.node[6]['info'] = 'F'
    return G


def generate_graph_test_combine():
    G = nx.DiGraph()
    G.add_edge(1, 2, weight=0)
    G.add_edge(3, 2, weight=1)
    G.add_edge(2, 4, weight=1)
    G.add_edge(5, 4, weight=0)
    return G

def generate_graph_test_combine1():
    G = nx.DiGraph()
    G.add_edge(3, 2, weight=1)
