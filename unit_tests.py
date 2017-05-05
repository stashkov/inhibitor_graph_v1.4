import collections
from unittest import TestCase
import pathway_graph as p
import examples


class TestAdd_combinations(TestCase):
    def setUp(self):
        self.edges = [(1, [2, 3]),
                      (2, [3, 4, 5])]
        self.result = [(1, [2, 3]),
                       (2, [3, 4, 5]),
                       (2, [3, 4]),
                       (2, [3, 5]),
                       (2, [4, 5])]

    def test_add_combinations(self):
        self.assertEqual(p.add_combinations(self.edges), self.result)


class TestDelete_rows_from_matrix(TestCase):
    def test_delete_rows_from_matrix(self):
        list_of_rows = [2, 3]
        matrix = [[-1, -1, -1],
                  [0, 0, 0],
                  [0, 0, 0],
                  [1, 1, 1]]
        result = [[-1, -1, -1],
                  [1, 1, 1]]
        self.assertEqual(p.delete_rows_from_matrix(list_of_rows, matrix), result)


class Testgenerate_self_loop_graph(TestCase):
    def setUp(self):
        self.input = examples.generate_graph()
        self.gold_edges = [(1, 7, {}), (2, 8, {}), (3, 9, {}), (4, 10, {}), (5, 11, {}), (6, 12, {}), (7, 1, {}),
                           (8, 2, {}), (9, 3, {}), (10, 4, {}), (11, 5, {}), (12, 6, {})]
        self.gold_nodes = [(1, {'info': 'A1', 'label': [1, True]}), (2, {'info': 'C1', 'label': [2, True]}),
                           (3, {'info': 'B1', 'label': [3, True]}), (4, {'info': 'E1', 'label': [4, True]}),
                           (5, {'info': 'D1', 'label': [5, True]}), (6, {'info': 'F1', 'label': [6, True]}),
                           (7, {'info': 'A0', 'label': [1, False]}), (8, {'info': 'C0', 'label': [2, False]}),
                           (9, {'info': 'B0', 'label': [3, False]}), (10, {'info': 'E0', 'label': [4, False]}),
                           (11, {'info': 'D0', 'label': [5, False]}), (12, {'info': 'F0', 'label': [6, False]})]
        self.gold_selfloop = {1: 7, 2: 8, 3: 9, 4: 10, 5: 11, 6: 12}
        self.lead_graph, self.lead_selfloop = p.generate_self_loop_graph(self.input)

    def test_graph_edges(self):
        self.assertEqual(self.lead_graph.edges(data=True), self.gold_edges)

    def test_graph_nodes(self):
        self.assertEqual(self.lead_graph.nodes(data=True), self.gold_nodes)

    def test_self_loop(self):
        self.assertEqual(self.lead_selfloop, self.gold_selfloop)


class TestDictionaryOfActions(TestCase):
    def setUp(self):
        self.input = examples.generate_graph()
        self.gold_G1_nodes = [(1, {'info': 'A1', 'label': [1, True]}), (2, {'info': 'C1', 'label': [2, True]}),
                              (3, {'info': 'B1', 'label': [3, True]}), (4, {'info': 'E1', 'label': [4, True]}),
                              (5, {'info': 'D1', 'label': [5, True]}), (6, {'info': 'F1', 'label': [6, True]}),
                              (7, {'info': 'A0', 'label': [1, False]}), (8, {'info': 'C0', 'label': [2, False]}),
                              (9, {'info': 'B0', 'label': [3, False]}), (10, {'info': 'E0', 'label': [4, False]}),
                              (11, {'info': 'D0', 'label': [5, False]}), (12, {'info': 'F0', 'label': [6, False]})]
        self.gold_G1_edges = [(1, 7, {}), (2, 8, {}), (3, 9, {}), (4, 10, {}), (5, 11, {}), (6, 12, {}), (7, 1, {}),
                              (8, 2, {}), (9, 3, {}), (10, 4, {}), (11, 5, {}), (12, 6, {})]
        self.gold_G2_nodes = [(1, {'info': 'A1', 'label': [1, True]}), (2, {'info': 'C', 'label': [2, True]}),
                              (3, {'info': 'B1', 'label': [3, True]}), (4, {'info': 'E1', 'label': [4, True]}),
                              (5, {'info': 'D1', 'label': [5, True]}), (6, {'info': 'F1', 'label': [6, True]}),
                              (8, {'info': 'C0', 'label': [2, False]}), (10, {'info': 'E0', 'label': [4, False]})]
        self.gold_G2_edges = [(1, 2, {}), (2, 10, {}), (3, 8, {}), (3, 6, {}), (5, 4, {})]

        Combi_graph = collections.namedtuple('Combi_graph', 'edges_to_remove_from_G2 node_to_add edges_to_add')
        self.gold_dict_test = {(4, (2, 5)): Combi_graph(edges_to_remove_from_G2=[(2, 10), (5, 4)],
                                                        node_to_add=(14, [2, False, 5, True], 'C0D'),
                                                        edges_to_add=[(14, 4), (8, 14), (5, 14)]),
                               (2, (1, 3)): Combi_graph(edges_to_remove_from_G2=[(1, 2), (3, 8)],
                                                        node_to_add=(13, [1, True, 3, False], 'AB0'),
                                                        edges_to_add=[(13, 2), (1, 13), (9, 13)])}
        self.lead_G1, self.lead_G2, self.lead_dict_test = p.dictionary_of_actions(self.input)

    def test_dictionary_of_actions_G1_nodes(self):
        self.assertEqual(self.lead_G1.nodes(data=True), self.gold_G1_nodes)

    def test_dictionary_of_actions_G1_edges(self):
        self.assertEqual(self.lead_G1.edges(data=True), self.gold_G1_edges)

    def test_dictionary_of_actions_G2_nodes(self):
        self.assertEqual(self.lead_G2.nodes(data=True), self.gold_G2_nodes)

    def test_dictionary_of_actions_G2_edges(self):
        self.assertEqual(self.lead_G2.edges(data=True), self.gold_G2_edges)

    def test_dictionary_of_actions_dict(self):
        self.assertEqual(self.lead_dict_test, self.gold_dict_test)


class TestMergeG1AndG3(TestCase):
    def setUp(self):
        self.input = examples.generate_graph()
        self.G1, self.G2, self.dict_test = p.dictionary_of_actions(self.input)
        self.lead_result = p.merge_G1_and_G3(self.G1, self.G2, self.dict_test)
        self.lead_first_G3_nodes = self.lead_result[0].edges(data=True)
        self.lead_first_G3_edges = self.lead_result[0].nodes(data=True)
        self.lead_second_G3_nodes = self.lead_result[1].edges(data=True)
        self.lead_second_G3_edges = self.lead_result[1].nodes(data=True)

        self.gold_first_G3_nodes = [(1, 2, {}), (1, 7, {}), (2, 8, {}), (3, 8, {}), (3, 9, {}), (3, 6, {}), (4, 10, {}),
                                    (5, 11, {}), (5, 14, {}), (6, 12, {}), (7, 1, {}), (8, 2, {}), (8, 14, {}),
                                    (9, 3, {}), (10, 4, {}), (11, 5, {}), (12, 6, {}), (14, 4, {})]
        self.gold_first_G3_edges = [(1, 2, {}), (1, 7, {}), (2, 8, {}), (3, 8, {}), (3, 9, {}), (3, 6, {}), (4, 10, {}),
                                    (5, 11, {}), (5, 14, {}), (6, 12, {}), (7, 1, {}), (8, 2, {}), (8, 14, {}),
                                    (9, 3, {}), (10, 4, {}), (11, 5, {}), (12, 6, {}), (14, 4, {})]
        self.gold_second_G3_nodes = [(1, 13, {}), (1, 7, {}), (2, 8, {}), (2, 10, {}), (3, 9, {}), (3, 6, {}),
                                     (4, 10, {}), (5, 11, {}), (5, 4, {}), (6, 12, {}), (7, 1, {}), (8, 2, {}),
                                     (9, 3, {}), (9, 13, {}), (10, 4, {}), (11, 5, {}), (12, 6, {}), (13, 2, {})]
        self.gold_second_G3_edges = [(1, {'info': 'A1', 'label': [1, True]}), (2, {'info': 'C1', 'label': [2, True]}),
                                     (3, {'info': 'B1', 'label': [3, True]}), (4, {'info': 'E1', 'label': [4, True]}),
                                     (5, {'info': 'D1', 'label': [5, True]}), (6, {'info': 'F1', 'label': [6, True]}),
                                     (7, {'info': 'A0', 'label': [1, False]}), (8, {'info': 'C0', 'label': [2, False]}),
                                     (9, {'info': 'B0', 'label': [3, False]}),
                                     (10, {'info': 'E0', 'label': [4, False]}),
                                     (11, {'info': 'D0', 'label': [5, False]}),
                                     (12, {'info': 'F0', 'label': [6, False]}),
                                     (13, {'info': 'AB0', 'label': [1, True, 3, False]})]

    def test_merge_result_first_G3_nodes(self):
        self.assertEqual(self.lead_first_G3_nodes, self.gold_first_G3_nodes)

    def test_merge_result_first_G3_edges(self):
        self.assertEqual(self.lead_first_G3_nodes, self.gold_first_G3_nodes)

    def test_merge_result_second_G3_nodes(self):
        self.assertEqual(self.lead_second_G3_nodes, self.gold_second_G3_nodes)

    def test_merge_result_second_G3_edges(self):
        self.assertEqual(self.lead_second_G3_edges, self.gold_second_G3_edges)