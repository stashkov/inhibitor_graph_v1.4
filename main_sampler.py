import os
import new_esampler as s
import re


def stat_read_stoic_matrix(path='data/Stoic_matrix_0.txt'):
    stoic_matrix = []
    with open(path, 'r') as f:
        for line in xrange(3):
            f.next()
        for line in f:
            stoic_matrix.append([int(i) for i in line.strip().split('  ')])
    return stoic_matrix


def calculate_efm(path_to_file):
    matrix = stat_read_stoic_matrix(path_to_file)
    rev_vector = [0 for i in range(len(matrix[0]))]
    sampler = s.Sampler(matrix, rev_vector)
    print '{:<50}{:<25}'.format(filename, len(sampler.result))
    return len(sampler.result)


number_of_efm_by_node = dict()
number_of_efm_in_expanded_graph = 0
for dirpath, dirnames, filenames in os.walk('data/'):
    for filename in filenames:
        if filename.endswith('.txt'):
            efms = calculate_efm(dirpath + filename)
            if filename.startswith('Stoic_matrix'):
                number_of_efm_in_expanded_graph += efms
            if filename.startswith('Stoic_remove_'):
                node = re.match(r'^.*node(\d+).*$', filename).group(1)
                number_of_efm_by_node[node] = number_of_efm_by_node.get(node, 0) + efms

print number_of_efm_in_expanded_graph
print number_of_efm_by_node

for k, v in number_of_efm_by_node.items():
    print k, v

