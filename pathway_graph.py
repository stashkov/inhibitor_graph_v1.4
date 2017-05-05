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


class RemoveInhibitionFromMethabolicPathway(object):
    def __init__(self, G):
        self.G = G
        self.G1, self.G1_selfloop = self.generate_self_loop_graph()
        self.G2 = self.generate_inhibited_edges_graph()
        self.dict_of_actions = self.dictionary_of_actions()
        self.result = self.merge_G1_and_G3()

    @staticmethod
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

    def generate_self_loop_graph(self):
        G1_selfloop = dict()
        G1 = nx.DiGraph()
        z = max(self.G.nodes())
        for v in self.G.nodes():
            # add labels True to all starting nodes
            G1.add_node(v, label=[v, True], info=self.G.node[v]['info'] + '1')
            # add mirror negated nodes
            z += 1
            G1.add_node(z, label=[v, False], info=self.G.node[v]['info'] + '0')
            # add edges between them
            G1.add_edge(v, z)
            G1.add_edge(z, v)
            # create dictionary of self loops
            G1_selfloop[v] = z
        return G1, G1_selfloop

    def generate_inhibited_edges_graph(self):
        G2 = nx.DiGraph()
        for u, v in self.G.edges():
            if self.G[u][v]['weight'] == 0:
                G2.add_node(u, label=[u, True], info=self.G.node[u]['info'] + '1')
                G2.add_node(v, label=[v, True], info=self.G.node[v]['info'] + '1')
                G2.add_edge(u, v)
            else:  # self.G[u][v]['weight'] == 1
                G2.add_node(u, label=[u, True], info=self.G.node[u]['info'])
                G2.add_node(self.G1_selfloop[v], label=[v, False], info=self.G.node[v]['info'] + '0')
                G2.add_edge(u, self.G1_selfloop[v])
        return G2

    @staticmethod
    def print_dict_of_actions(d):
        for k, v in d.iteritems():
            child, parents = k
            print '---'
            print 'edges to remove from G2: ', v.edges_to_remove_from_G2
            print 'node to add to G3', v.node_to_add
            print 'edges to add to G3', v.edges_to_add
            print '---'

    @staticmethod
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

    def dictionary_of_actions(self):
        """
        {
            (2, [1,3]) : ([
                              [1,2], [3,8]
                          ],
                          [
                              [z, label=[parent1, True, parent2, False], info='AB0']
                          ],
                          [
                              [z, 2], [1, z], [9, z]
                          ])
        }

    
    
    
        dict_of_actions = {(2, (1, 3)): Combi_graph(edges_to_remove_from_G2=[[1, 2], [3, 8]],
                                              node_to_add=(13, [1, True, 3, False], 'AB0'),
                                              edges_to_add=[[13, 2], [1, 13], [9, 13]])}


        """
        dict_test = {}

        z = max(self.G1.nodes())

        contract_nodes_candidates = self.nodes_more_1_parent(self.G)
        contract_nodes_candidates = self.add_combinations(contract_nodes_candidates)

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
                if self.G[p][child]['weight'] == 0:
                    new_node_label.extend([p, True])
                    new_node_info += self.G.node[p]['info']
                    edges_to_remove_from_G2.append((p, child))
                    edges_to_add.append((p, z))
                if self.G[p][child]['weight'] == 1:
                    new_node_label.extend([p, False])
                    new_node_info += self.G.node[p]['info'] + '0'
                    edges_to_remove_from_G2.append((p, self.G1_selfloop[child]))
                    edges_to_add.append((self.G1_selfloop[p], z))
            node_to_add = (z, new_node_label, new_node_info)

            dict_test[(child, tuple(parents))] = Combi_graph(edges_to_remove_from_G2=edges_to_remove_from_G2,
                                                             node_to_add=node_to_add,
                                                             edges_to_add=edges_to_add)
        return dict_test

    def merge_G1_and_G3(self):
        # merge G1 and G3
        result = []
        for k, v in self.dict_of_actions.iteritems():
            G3_1 = copy.deepcopy(self.G2)
            edges_to_remove_from_G2, node_to_add, edges_to_add = v
            for u, v in edges_to_remove_from_G2:
                G3_1.remove_edge(u, v)
            z, label, info = node_to_add
            G3_1.add_node(z, label=label, info=info)
            for u, v in edges_to_add:
                G3_1.add_edge(u, v)

            G3 = nx.compose(G3_1, self.G1)  # apparently order matters
            result.append(G3)
        return result

    @staticmethod
    def save_matrix(graph, sequential_number, file_prefix='empty_prefix'):
        # TODO write test case
        """given a networkx DiGraph generate stoichiometric matrix and save it"""

        def missing_sequential_nodes(graph):
            """given a graph with nodes [1,2,3,6,7] return [4,5]"""
            assert isinstance(graph, nx.classes.digraph.DiGraph)
            return list(set(range(1, max(graph.nodes()) + 1)) - set(graph.nodes()))

        def delete_rows_from_matrix(list_of_rows, matrix):
            """we have nodes [1,2,7,11] this means nodes 3,4,5,6,8,9,10 do not exist, so we have to delete them"""
            assert type(matrix) == list
            assert all(isinstance(row, list) for row in matrix)
            matrix = [row for i, row in enumerate(matrix) if i + 1 not in list_of_rows]
            return matrix

        n_of_rows = max(graph.nodes())
        n_of_columns = len(graph.edges())
        matrix = [[0 for _ in range(n_of_columns)] for _ in range(n_of_rows)]

        column = 0
        for u, v in graph.edges():
            matrix[u - 1][column] = -1
            matrix[v - 1][column] = 1
            column += 1

        # here was G3 and I switched to graph (may be error)
        delete_rows_from_matrix(missing_sequential_nodes(graph), matrix)

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

    @staticmethod
    def save_graphml(graph, sequential_number, file_prefix='empty_prefix'):
        """save networkx DiGraph as GraphML file"""
        # graphML format doesn't like anything except strings
        # so we need to convert additional information to string
        for node in graph.nodes():
            # print 'test', graph.node[node]['contraction']
            for attrib in graph.node[node]:
                # print graph.node[node], 'before', node
                if type(graph.node[node][attrib]) == list:
                    graph.node[node]['label'] = str(graph.node[node]['label'])
                    # print node, 'oO'
                    # print graph.node[node]

        nx.write_graphml(graph, "data/graphML/" + file_prefix + "_" + str(sequential_number) + ".graphml")
        return None
