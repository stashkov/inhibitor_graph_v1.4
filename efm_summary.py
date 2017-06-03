import os
import new_esampler as s
import re


class EFMSummary(object):
    """
    EFM - Elementary flux modes
    Given a directory 
        calculate #EFM in expanded graph
        calculate #EFM in a graph minus node v
    
    """
    def __init__(self, dirpath):
        self.dirpath = dirpath
        self.EFM_by_nodes = self.calculate_EFM_by_node()
        self.EFM_in_expanded_graph = self.calculate_EFM_in_expanded_graph()

    def filenames(self):
        for dirpath, dirnames, filenames in os.walk(self.dirpath):
            for filename in filenames:
                if filename.endswith('.txt'):
                    yield filename

    def calculate_EFM_in_expanded_graph(self):
        number_of_efm_in_expanded_graph = 0
        for filename in self.filenames():
            if filename.startswith('Stoic_matrix'):
                efms = EFMSummary.calculate_efm(self.dirpath + filename)
                number_of_efm_in_expanded_graph += efms
        return number_of_efm_in_expanded_graph

    def calculate_EFM_by_node(self):
        number_of_efm_by_node = dict()
        for filename in self.filenames():
            if filename.startswith('Stoic_remove_node'):
                efms = EFMSummary.calculate_efm(self.dirpath + filename)
                node = EFMSummary.get_node_number_from_filename(filename)
                number_of_efm_by_node[node] = number_of_efm_by_node.get(node, 0) + efms
        return number_of_efm_by_node

    def print_EFM_by_node(self):
        assert isinstance(self.EFM_by_nodes, dict)
        print '{:<25}{:<25}{:<25}'.format("Node", "#EFM-v", "Ratio")
        for k, v in sorted(self.EFM_by_nodes.items()):
            print('{:<25}{:<25}{:<25}'.format(k, v, EFMSummary.calculate_ratio(v, self.EFM_in_expanded_graph)))

    @staticmethod
    def read_stoic_matrix(filename):
        assert os.path.exists(filename)

        def skip_first_3_lines():
            for line in range(3):
                f.next()

        def read_matrix_line_by_line():
            for line in f:
                stoic_matrix.append([int(i) for i in line.strip().split('  ')])

        stoic_matrix = []
        with open(filename, 'r') as f:
            skip_first_3_lines()
            read_matrix_line_by_line()
        return stoic_matrix

    @staticmethod
    def calculate_ratio(EFM_minus_v, EFM_total):
        assert isinstance(EFM_total, int)
        assert isinstance(EFM_minus_v, int)
        return float(EFM_total - EFM_minus_v) / EFM_total

    @staticmethod
    def calculate_efm(filename):
        assert os.path.exists(filename)

        def print_for_each_file_number_of_EFMs():
            print '{:<50}{:<25}'.format(filename, len(sampler.result))
        matrix = EFMSummary.read_stoic_matrix(filename)
        rev_vector = [0 for i in range(len(matrix[0]))]
        sampler = s.Sampler(matrix, rev_vector)
        print_for_each_file_number_of_EFMs()
        return len(sampler.result)

    @staticmethod
    def get_node_number_from_filename(filename):
        return int(re.match(r'^.*node(\d+).*$', filename).group(1))
