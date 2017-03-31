import networkx as nx
import matplotlib.pyplot as plt
import math
import examples
import copy
import collections
import itertools
import time

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


def nodes_more_1_parent(graph):
    """
    :param graph: object of type networkx.classes.digraph.DiGraph
    :return: a list of tuples [(2, [1,3]),...]

    if node has > 1 parent we add it to a list
    for possible contraction later
    """
    assert isinstance(graph, nx.classes.digraph.DiGraph)
    nodes = list()
    for u, d in graph.nodes(data=True):
        predecessors = graph.predecessors(u)
        if len(predecessors) > 1:
            nodes.append((u, predecessors))
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
        child, parents = k
        print '---'
        print 'edges to remove from G2: ', v.edges_to_remove_from_G2
        print 'node to add to G3', v.node_to_add
        print 'edges to add to G3', v.edges_to_add
        print '---'


def add_combinations(edges, length=2):
    """
        input: a list of tuples (int, list())
        output: append combinations of list() to a list
        example:
            list: [(1, [2, 3]),
                    (2, [3, 4, 5])]
            result: [(1, [2, 3]),
                       (2, [3, 4, 5]),
                       (2, [3, 4]),
                       (2, [3, 5]),
                       (2, [4, 5])]
        because we took r-length combination of a list [3,4,5]
    """
    assert type(edges) == list
    assert all(isinstance(u, int) for u, v in edges)
    assert all(isinstance(v, list) for u, v in edges)
    for child, parents in edges:
        if len(parents) > length:
            for c in list(itertools.combinations(parents, length)):
                edges.append((child, list(c)))
    return edges


def missing_sequential_nodes(graph):
    """given a graph with nodes [1,2,3,6,7] return [4,5]"""
    assert isinstance(graph, nx.classes.digraph.DiGraph)
    return list(set(range(1, max(graph.nodes()) + 1)) - set(graph.nodes()))


def delete_rows_from_matrix(list_of_rows, matrix):
    """we have nodes [1,2,7,11] this means nodes 3,4,5,6,8,9,10 do not exist, so we have to delete them"""
    assert type(matrix) == list
    assert all(isinstance(row, list) for row in matrix)
    # TODO need to check that matrix in the output file has correct dimensions
    matrix = [row for i, row in enumerate(matrix) if i + 1 not in list_of_rows]
    return matrix


def save_matrix(graph, sequential_number, file_prefix='empty_prefix'):
    """    create and save to file stoichiometric matrix    """
    # TODO write test case
    n_of_rows = max(graph.nodes())
    n_of_columns = len(graph.edges())
    matrix = [[0 for x in range(n_of_columns)] for y in range(n_of_rows)]

    column = 0
    for u, v in graph.edges():
        matrix[u - 1][column] = -1
        matrix[v - 1][column] = 1
        column += 1

    delete_rows_from_matrix(missing_sequential_nodes(G3), matrix)



    # save to file
    f = open('data/matrix/%s_matrix_%s.txt' % (file_prefix, sequential_number), 'w')
    f.write('matrix dimensions: %s %s' % (len(matrix), n_of_columns))
    f.write('\n')
    f.write('nodes: %s' % ' '.join(str(n) for n in graph.nodes()))
    f.write('\n')
    f.write('edges: %s' % ' '.join(str(u) + ' ' + str(v) for u, v in graph.edges()))
    f.write('\n')

    for i in matrix:
        f.write('  '.join(str(e) for e in i))
        f.write('\n')
    f.close()
    return None


def save_graphml(graph, sequential_number):
    """
    :param graph:
    :param sequential_number:
    :return:
     graphML format doesn't like anything except strings
     so we need to convert additional information to string
    """
    for node in graph.nodes():
        # print 'test', graph.node[node]['contraction']
        for attrib in graph.node[node]:
            # print graph.node[node], 'before', node
            if type(graph.node[node][attrib]) == list:
                graph.node[node]['label'] = str(graph.node[node]['label'])
                # print node, 'oO'
                # print graph.node[node]

    nx.write_graphml(graph, "data/graphML/_barabasi_stoichiometric_" + str(sequential_number) + ".graphml")
    return None


def plot_graph(*argv):
    plt.figure(1)
    for i, arg in enumerate(argv):
        plt.subplot(2, 2, i + 1)
        my_draw_graph(arg)
    plt.show()
    return None


if __name__ == '__main__':
    G = examples.generate_barabasi(7); graph_name = 'barabasi'
    # G = examples.generate_graph()
    # G = examples.example30(); graph_name = 'example30'
    # G = generate_graph_test_loops()
    start = time.time()

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



    # dict_test = {(2, (1, 3)): Combi_graph(edges_to_remove_from_G2=[[1, 2], [3, 8]],
    #                                       node_to_add=(13, [1, True, 3, False], 'AB0'),
    #                                       edges_to_add=[[13, 2], [1, 13], [9, 13]])}
    #
    #
    dict_test = {}

    z = max(G1.nodes())

    contract_nodes_candidates = nodes_more_1_parent(G)
    contract_nodes_candidates = add_combinations(contract_nodes_candidates)

    Combi_graph = collections.namedtuple('Combi_graph', 'edges_to_remove_from_G2 node_to_add edges_to_add')
    for child, parents in contract_nodes_candidates:
        edges_to_remove_from_G2 = list()  # gonna be list of tuples
        node_to_add = tuple()  # 3-tuple
        edges_to_add = list()  # list of tuples
        new_node_label = list()
        new_node_info = str()
        z += 1  # new node
        # print child, parents
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

    # merge G1 and G3
    for k, v in dict_test.iteritems():
        G3_1 = copy.deepcopy(G2)
        edges_to_remove_from_G2, node_to_add, edges_to_add = v
        for u, v in edges_to_remove_from_G2:
            G3_1.remove_edge(u, v)
        z, label, info = node_to_add
        # print z, label, info
        G3_1.add_node(z, label=label, info=info)

        for u, v in edges_to_add:
            G3_1.add_edge(u, v)

        G3 = nx.compose(G3_1, G1)  # apparently order matters

        save_graphml(G3, z)
        save_matrix(G3, z, file_prefix=graph_name)

    print "Process time: %s " % (time.time() - start)

    plot_graph(G1, G2, G3_1, G3)




