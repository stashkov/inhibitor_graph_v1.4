import networkx as nx
import matplotlib.pyplot as plt
import math
import examples
import copy

"""
if u -> v is inhibited, we duplicate v to bar{v} and redirect u to bar{v}
v and bar{v} will be connect via a directed loop
"""


def my_draw_graph(G):
    pos = nx.spring_layout(G, k=5/math.sqrt(G.order()))  # k - Optimal distance between nodes.
    labels = dict()
    white_nodes, red_nodes = [], []
    for n, d in G.nodes(data=True):
        labels[n] = str(d.get('info')) + ' ' + str(d.get('label', n)) + '\n' + str(d.get('flag', ''))
        if 'flag' not in d.keys() or d['flag'] is True:
            white_nodes.append(n)
        else:
            red_nodes.append(n)

    nx.draw_networkx_edges(G, pos, width=3)
    nx.draw_networkx_nodes(G, pos, node_size=3*3000, node_color='white', nodelist=white_nodes)
    nx.draw_networkx_nodes(G, pos, node_size=3*3000, node_color='red', nodelist=red_nodes)
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


def contract_nodes_candidates_in_original_graph(graph):
    nodes = dict()
    for u, d in graph.nodes(data=True):
        # print graph.predecessors(u), len(graph.predecessors(u))
        predecessors = graph.predecessors(u)
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


def generate_self_loop_graph(G):
    G1_selfloop = dict()
    G1 = nx.DiGraph()
    z = max(G.nodes())
    for v in G.nodes():
        # add labels True to all starting nodes
        G1.add_node(v, label=[v, True], info=G.node[v]['info'] + '1')
        # add mirror negated nodes
        z += 1
        G1.add_node(z, label=[v, False], info=G.node[v]['info'] + '0')
        # add edges between them
        G1.add_edge(v, z)
        G1.add_edge(z, v)
        # create dictionary of self loops
        G1_selfloop[v] = z
    return G1, G1_selfloop


def generate_inhibited_edges_graph(G, G1_selfloop):
    G2 = nx.DiGraph()
    for u, v in G.edges():
        if G[u][v]['weight'] == 0:
            G2.add_node(u, label=[u, True], info=G.node[u]['info'] + '1')
            G2.add_node(v, label=[v, True], info=G.node[v]['info'] + '1')
            G2.add_edge(u, v)
        else:  # G[u][v]['weight'] == 1
            G2.add_node(u, label=[u, True], info=G.node[u]['info'])
            G2.add_node(G1_selfloop[v], label=[v, False], info=G.node[v]['info'] + '0')
            G2.add_edge(u, G1_selfloop[v])
    return G2


def print_my_insane_dict(d):
    for k, v in d.iteritems():
        print k
        child, parents = k
        print '---'
        print v.edges_to_remove_from_G2

        node_to_add, label, info = v.node_to_add
        print v.node_to_add

        print v.edges_to_add
        print '---'



if __name__ == '__main__':
    # G = generate_barabasi(100)
    G = examples.generate_graph()
    # G = generate_graph_test_loops()

    G1, G1_selfloop = generate_self_loop_graph(G)

    G2 = generate_inhibited_edges_graph(G, G1_selfloop)

    # {
    #     (2, [1,3]) : ([
    #                       [1,2], [3,8]
    #                   ],
    #                   [
    #                       [z, label=[parent1, True, parent2, False], info='AB0']
    #                   ],
    #                   [
    #                       [z, 2], [1, z], [9, z]
    #                   ])
    # }
    #
    from collections import namedtuple
    Combi_graph = namedtuple('Combi_graph', 'edges_to_remove_from_G2 node_to_add edges_to_add')

    # dict_test = {(2, (1, 3)): Combi_graph(edges_to_remove_from_G2=[[1, 2], [3, 8]],
    #                                       node_to_add=(13, [1, True, 3, False], 'AB0'),
    #                                       edges_to_add=[[13, 2], [1, 13], [9, 13]])}
    #
    #
    dict_test = {}

    z = max(G1.nodes())
    contract_nodes_candidates = contract_nodes_candidates_in_original_graph(G)
    contract_nodes_candidates = {2: [1, 3]}


    for child, parents in contract_nodes_candidates.iteritems():
        edges_to_remove_from_G2 = list()  # gonna be list of tuples
        node_to_add = tuple()  # 3-tuple
        edges_to_add = list()  # list of tuples
        new_node_label = list()
        new_node_info = str()
        z += 1  # new node
        print child, parents
        edges_to_add.append((z, child))
        for p in parents:
            if G[p][child]['weight'] == 0:
                new_node_label.extend([p, True])
                new_node_info += G.node[p]['info']
                edges_to_remove_from_G2.append((p, child))
                edges_to_add.append((p, z))
            if G[p][child]['weight'] == 1:
                new_node_label.extend([p, False])
                new_node_info += G.node[p]['info'] + '0'
                edges_to_remove_from_G2.append((p, G1_selfloop[child]))
                edges_to_add.append((G1_selfloop[p], z))
        node_to_add = (z, new_node_label, new_node_info)

        dict_test[(child, tuple(parents))] = Combi_graph(edges_to_remove_from_G2=edges_to_remove_from_G2,
                                                         node_to_add=node_to_add,
                                                         edges_to_add=edges_to_add)


    print_my_insane_dict(dict_test)

    G_3_1 = copy.deepcopy(G2)
    for k, v in dict_test.iteritems():
        edges_to_remove_from_G2, node_to_add, edges_to_add = v
        for u, v in edges_to_remove_from_G2:
            G_3_1.remove_edge(u, v)

        z, label, info = node_to_add
        G_3_1.add_node(z, label=label, info=info)

        for u, v in edges_to_add:
            G_3_1.add_edge(u, v)

    G3 = nx.compose(G_3_1, G1)  # apparently order matters


    print '\n'
    print G2.edges()

    print G1.edges()
    print G1.nodes(data=True)

    # G = examples.example30()
    # G = examples.generate_graph()

    # G1 = nx.DiGraph()
    # G1 = replace_inhibited_edges_with_negation_of_node(input_graph=G, output_graph=G1)

    # remove_out_degree_zero_nodes(G1)

    # contract_nodes_candidates = contract_nodes_candidates_in_original_graph(G)
    # TODO remove this line, because it was used for tests
    # contract_nodes_candidates = {2: [1, 3]}
    # print contract_nodes_candidates

    # G2 = copy.deepcopy(G1)

    # edges_pool = dict()
    # z = max(G2.nodes())

    # for k, nodes_going_to_k in contract_nodes_candidates.iteritems():
    #     # print 'oO', G[1][2]
    #     # print G2.node[2]['label'], G2.node[2]['flag']
    #     z += 1
    #     label = str()
    #     for n in nodes_going_to_k:
    #         # TODO A and B can have predecessors, in this case we need to redirect all of them to a new node z
    #         # G.predecessors(n)
    #         # print G2.node[n]['label'], G2.node[n]['flag'], k,  G[n][k]
    #         if G[n][k]['weight'] == 0:
    #             label += str(n) + 'T'
    #         else:
    #             label += str(n) + 'F'
    #         G2.remove_node(n)
    #     G2.add_node(z, label=label)
    #     G2.add_edge(z, k, weight=0)












    for node in G3.nodes():
        # print 'test', G3.node[node]['contraction']
        for attrib in G3.node[node]:
            # print G3.node[node], 'before', node
            if type(G3.node[node][attrib]) == list:
                G3.node[node]['label'] = str(G3.node[node]['label'])
                # print node, 'oO'
                # print G3.node[node]
    #
    #
    plt.figure(1)
    plt.subplot(221)
    my_draw_graph(G)
    plt.subplot(222)
    my_draw_graph(G1)
    plt.subplot(223)
    my_draw_graph(G2)
    plt.subplot(224)
    my_draw_graph(nx.compose(G1,G2))

    plt.figure(2)
    plt.subplot(111)
    my_draw_graph(G3)


    plt.show()
    #
    print nx.write_graphml(G3, "test_G3.graphml")




    # G2 = nx.contracted_nodes(G2, v[0], v[1])