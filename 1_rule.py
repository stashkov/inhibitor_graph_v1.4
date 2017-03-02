import networkx as nx
import matplotlib.pyplot as plt
import math
import examples

"""
if u -> v is inhibited, we duplicate v to bar{v} and redirect u to bar{v}
v and bar{v} will be connect via a directed loop
"""


def my_draw_graph(G):
    pos = nx.spring_layout(G, k=5/math.sqrt(G.order()))  # k - Optimal distance between nodes.
    labels = dict()
    white_nodes, red_nodes = [], []
    for n, d in G.nodes(data=True):
        labels[n] = str(d.get('label', n)) + '\n' + str(d.get('flag', ''))
        if 'flag' not in d.keys() or d['flag'] is True:
            white_nodes.append(n)
        else:
            red_nodes.append(n)

    nx.draw_networkx_edges(G, pos, width=3)
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='white', nodelist=white_nodes)
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='red', nodelist=red_nodes)
    nx.draw_networkx_labels(G, pos, labels, font_size=15)


def remove_out_degree_zero_nodes(graph):
    for v, d in graph.nodes(data=True):
        if graph.in_degree(v) == graph.out_degree(v) == 1 and graph.predecessors(v) == graph.successors(v):
            graph.remove_node(v)


def contract_nodes_candidates(graph):
    d = dict()
    for u in graph.nodes():
        # print graph.predecessors(u), len(graph.predecessors(u))
        predecessors = graph.predecessors(u)
        if len(predecessors) > 1:
            d[u] = predecessors
    return d


def contract_nodes_candidates_in_modified_graph(graph):
    nodes = dict()
    for u, d in graph.nodes(data=True):
        # print graph.predecessors(u), len(graph.predecessors(u))
        print u, d, graph.node[u]['label']

        predecessors = graph.predecessors(u)
        node_negation = graph.node[u]['label']
        if node_negation in predecessors:
            predecessors.remove(node_negation)

        if len(predecessors) > 1:
            nodes[u] = predecessors
    return nodes


def replace_inhibited_edges_with_negation_of_node(input_graph, output_graph):
    added_negative_nodes = set()
    next_node = max(input_graph.nodes())
    for u, v, d in input_graph.edges(data=True):
        if d['weight'] == 0:
            output_graph.add_node(u, label=u, flag=True)
            output_graph.add_node(v, label=v, flag=True)
            output_graph.add_edge(u, v, weight=0)
        if d['weight'] == 1:
            output_graph.add_node(u, label=u, flag=True)
            output_graph.add_node(v, label=v, flag=True)
            if v not in added_negative_nodes:
                added_negative_nodes.add(v)
                next_node += 1
                w = next_node
                output_graph.add_node(w, label=v, flag=False)
                output_graph.add_edge(u, w, weight=0)
                output_graph.add_edge(v, w, weight=0)  # self loop
                output_graph.add_edge(w, v, weight=0)  # self loop
            else:
                output_graph.add_edge(u, v, weight=0)
    return output_graph


if __name__ == '__main__':
    # G = generate_barabasi(100)
    G = examples.generate_graph()
    # G = generate_graph_test_loops()

    # G = examples.example30()
    # G = examples.generate_graph()

    G1 = nx.DiGraph()
    G1 = replace_inhibited_edges_with_negation_of_node(input_graph=G, output_graph=G1)

    remove_out_degree_zero_nodes(G1)

    contract_nodes_candidates = contract_nodes_candidates_in_modified_graph(G1)
    print contract_nodes_candidates
    #
    # G2 = copy.deepcopy(G1)
    #
    # for k, v in contract_nodes_candidates.iteritems():
    #     G2 = nx.contracted_nodes(G2, v[0], v[1])
    #
    # for node in G2.nodes():
    #     # print 'test', G2.node[node]['contraction']
    #     for attrib in G2.node[node]:
    #         print G2.node[node], 'before', node
    #         if type(G2.node[node][attrib]) == dict:
    #             print node, 'oO'
    #             print G2.node[node]
    #
    # print G2.nodes()

    plt.figure(1)
    plt.subplot(131)
    my_draw_graph(G1)
    plt.subplot(132)
    my_draw_graph(G)
    plt.subplot(133)
    # my_draw_graph(G2)

    plt.show()

    print nx.write_graphml(G1, "test.graphml")