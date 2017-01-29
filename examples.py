import networkx as nx


def example30():
    G = nx.DiGraph()

    G.add_node(1, comment='Bacteria')
    G.add_node(2, comment='')
    G.add_node(3, comment='')
    G.add_node(4, comment='')
    G.add_node(5, comment='')
    G.add_node(6, comment='')
    G.add_node(7, comment='')
    G.add_node(8, comment='')
    G.add_node(9, comment='')
    G.add_node(10, comment='')
    G.add_node(11, comment='')
    G.add_node(12, comment='')
    G.add_node(13, comment='')
    G.add_node(14, comment='')
    G.add_node(15, comment='')
    G.add_node(16, comment='')
    G.add_node(17, comment='')
    G.add_node(18, comment='')

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