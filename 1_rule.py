import networkx as nx
import matplotlib.pyplot as plt
import string
import math
import random

"""
if u -> v is inhibited, we duplicate v to bar{v} and redirect u to bar{v}
v and bar{v} will be connect via a directed loop
"""


def my_draw_graph(G):
    pos = nx.spring_layout(G, k=5/math.sqrt(G.order()))  # k - Optimal distance between nodes.
    labels = dict()
    white_nodes, red_nodes = [], []
    for n, d in G.nodes(data=True):
        labels[n] = str(d['label']) + '\n' + str(d['flag'])
        if d['flag'] is True:
            white_nodes.append(n)
        else:
            red_nodes.append(n)

    nx.draw_networkx_edges(G, pos, width=3)
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='white', nodelist=white_nodes)
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='red', nodelist=red_nodes)
    nx.draw_networkx_labels(G, pos, labels, font_size=15)




def generate_graph():
    G = nx.DiGraph()
    G.add_edge(1, 2, weight=0)
    G.add_edge(3, 2, weight=1)
    G.add_edge(2, 4, weight=0)
    # G.add_edge(4, 5, weight=0)
    return G


def generate_barabasi(n):
    G = nx.barabasi_albert_graph(n, 2)
    percent_chance_of_inhibited_edge = 10
    for u, v, d in G.edges(data=True):
        d['weight'] = random.choice([0]*(100-percent_chance_of_inhibited_edge) + [1]*percent_chance_of_inhibited_edge)
    return G

if __name__ == '__main__':
    # G = generate_graph()
    G = generate_barabasi(20)

    G1 = nx.DiGraph()
    for u, v, d in G.edges(data=True):
        if d['weight'] == 0:
            G1.add_node(u, label=u, flag=True)
            G1.add_node(v, label=v, flag=True)
            G1.add_edge(u, v, weight=0)
        if d['weight'] == 1:
            G1.add_node(u, label=u, flag=True)
            G1.add_node(v, label=v, flag=True)
            w = max(G.nodes()) + 1
            G1.add_node(w, label=v, flag=False)
            G1.add_edge(u, w, weight=0)
            G1.add_edge(v, w, weight=0)  # self loop
            G1.add_edge(w, v, weight=0)  # self loop

    plt.figure(1)
    plt.subplot(111)
    my_draw_graph(G1)

    plt.show()

    print nx.write_graphml(G1, "test.graphml")