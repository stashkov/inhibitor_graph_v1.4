import networkx as nx
import matplotlib.pyplot as plt
import string
import math

# G = nx.barabasi_albert_graph(5, 1, seed=666)


def color_negative_and_positive_nodes(graph):
    red, white = [], []
    if any('mark' in d.keys() for u, d in graph.nodes(data=True)):
        for u, d in graph.nodes(data=True):
            if d['mark'] is True:
                white.append(u)
            else:
                red.append(u)
    else:
        white.extend(graph.nodes())
    return red, white


def assign_labels_to_nodes(graph):
    # labels = dict(zip(range(1, len(graph.nodes()) + 1), string.ascii_uppercase))
    labels = {i: str(i) for i in range(1, len(graph.nodes())+1)}
    if 'mark' in graph.nodes(data=True)[0][1].keys():
        for k, v in labels.iteritems():
            labels[k] += ' \n' + str(graph.node[k]['mark'])
    return labels


def my_draw_graph(G):
    pos = nx.spring_layout(G, k=5/math.sqrt(G.order()))  # k - Optimal distance between nodes.

    labels = assign_labels_to_nodes(G)
    red, white = color_negative_and_positive_nodes(G)
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='white', nodelist=white)
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='red', nodelist=red)
    # nx.draw_networkx_edges(G, pos)
    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] == 0]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] == 1]

    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=3)
    nx.draw_networkx_edges(G, pos,
                           edgelist=esmall,
                           width=3,
                           alpha=0.5,
                           edge_color='red',
                           style='dashed')
    nx.draw_networkx_labels(G, pos, labels, font_size=15)


# def is_negation_of_node_in_graph(graph, u, attr_dict):
#     return (u, {'mark': not (attr_dict[u])}) in graph.nodes(data=True)


def add_edge(graph, u, v, attr_dict):
    visited = set(graph.nodes())
    print u, v
    if u in visited and v not in visited:
        graph.add_node(v, mark=attr_dict[v])
        graph.add_edge(u, v, weight=0)
        if attr_dict[u] is False:
            graph.add_node(u, mark=attr_dict[u])
    elif v in visited and u not in visited:
        graph.add_node(u, mark=attr_dict[u])
        graph.add_edge(u, v, weight=0)
        if attr_dict[v] is False:
            graph.add_node(v, mark=attr_dict[v])
    else:
        graph.add_node(u, mark=attr_dict[u])
        graph.add_node(v, mark=attr_dict[v])
        graph.add_edge(u, v, weight=0)


def generate_graph():
    G = nx.DiGraph()
    G.add_edge(1, 2, weight=0)
    G.add_edge(3, 2, weight=1)
    G.add_edge(2, 4, weight=0)
    G.add_edge(4, 5, weight=0)
    return G

if __name__ == '__main__':
    G = generate_graph()

    G1 = nx.DiGraph()
    G2 = nx.DiGraph()
    for u, v, d in G.edges(data=True):
        if d['weight'] == 0:
            add_edge(G1, u, v, {u: True, v: True})
            add_edge(G2, u, v, {u: True, v: True})
        if d['weight'] == 1:
            add_edge(G1, u, v, {u: True, v: False})
            add_edge(G2, u, v, {u: False, v: True})



    plt.figure(1)
    plt.subplot(311)
    my_draw_graph(G)
    plt.subplot(312)
    my_draw_graph(G1)
    plt.subplot(313)
    my_draw_graph(G2)


plt.show()