import networkx as nx
import matplotlib.pyplot as plt
import random
import string
import math

# G = nx.barabasi_albert_graph(5, 1, seed=666)


def my_draw_graph(G):
    pos = nx.spring_layout(G, k=5/math.sqrt(G.order()))  # k - Optimal distance between nodes.
    # labels = {i: i for i in range(1, len(G.nodes())+1)}
    labels = dict(zip(range(1, len(G.nodes())+1), string.ascii_uppercase))
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='white')
    # nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=3)
    nx.draw_networkx_edges(G, pos,
                           edgelist=esmall,
                           width=3,
                           alpha=0.5,
                           edge_color='red',
                           style='dashed')
    nx.draw_networkx_labels(G, pos, labels, font_size=30)


# G = nx.gn_graph(6, seed=6)

# for u, v, d in G.edges(data=True):
#     w = random.choice([0, 1])
#     d['weight'] = w


G = nx.DiGraph()
G.add_edge(1, 2, weight=0)
G.add_edge(2, 3, weight=1)
G.add_edge(4, 2, weight=0)
G.add_edge(3, 5, weight=0)

G.add_nodes_from([1, 2, 3])

for u, v, d in G.edges(data=True):
    print u, v, d

print G


elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] == 0]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] == 1]
#

my_draw_graph(G)

print vars(G)


for u, v, d in G.edges(data=True):
    print u, v, d
#
# print G.predecessors(1)
# print G.successors(1)
#
# print G.get_edge_data(4, 1)


print list(nx.edge_dfs(G, orientation='ignore'))


plt.show()