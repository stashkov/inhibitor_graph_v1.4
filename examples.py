import networkx as nx


def example30():
    G = nx.DiGraph()

    G.add_node(1, info='A')
    G.add_node(2, info='B')
    G.add_node(3, info='C')
    G.add_node(4, info='D')
    G.add_node(5, info='E')
    G.add_node(6, info='F')
    G.add_node(7, info='G')
    G.add_node(8, info='H')
    G.add_node(9, info='J')
    G.add_node(10, info='K')
    G.add_node(11, info='L')
    G.add_node(12, info='M')
    G.add_node(13, info='N')
    G.add_node(14, info='O')
    G.add_node(15, info='P')
    G.add_node(16, info='Q')
    G.add_node(17, info='R')
    G.add_node(18, info='S')
    G.add_node(19, info='T')
    G.add_node(20, info='U')
    G.add_node(21, info='V')

    G.add_edge(1, 17, weight=0)
    G.add_edge(1, 4, weight=0)
    G.add_edge(1, 2, weight=0)
    G.add_edge(1, 3, weight=0)

    G.add_edge(2, 5, weight=0)

    G.add_edge(3, 7, weight=0)

    G.add_edge(4, 19, weight=0)
    G.add_edge(4, 7, weight=0)

    G.add_edge(5, 17, weight=0)
    G.add_edge(5, 6, weight=0)
    G.add_edge(5, 10, weight=0)

    G.add_edge(6, 7, weight=0)

    G.add_edge(7, 5, weight=0)

    G.add_edge(8, 4, weight=0)
    G.add_edge(8, 8, weight=0)

    G.add_edge(9, 9, weight=0)
    G.add_edge(9, 19, weight=0)

    G.add_edge(10, 7, weight=0)

    G.add_edge(11, 15, weight=0)

    G.add_edge(12, 20, weight=0)
    G.add_edge(12, 21, weight=0)

    G.add_edge(13, 14, weight=0)
    G.add_edge(13, 16, weight=0)

    G.add_edge(14, 8, weight=0)
    G.add_edge(14, 9, weight=0)

    G.add_edge(15, 10, weight=0)
    G.add_edge(15, 17, weight=0)
    G.add_edge(15, 20, weight=0)
    G.add_edge(15, 16, weight=1)

    G.add_edge(16, 15, weight=1)
    G.add_edge(16, 5, weight=1)
    G.add_edge(16, 17, weight=0)
    G.add_edge(16, 21, weight=0)

    G.add_edge(17, 15, weight=0)
    G.add_edge(17, 16, weight=0)

    G.add_edge(18, 1, weight=1)

    G.add_edge(19, 3, weight=0)

    G.add_edge(20, 11, weight=0)

    G.add_edge(21, 13, weight=0)
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
    G = nx.barabasi_albert_graph(n, 2, seed=13)
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
