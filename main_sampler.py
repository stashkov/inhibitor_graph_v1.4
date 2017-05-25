import os
import new_esampler as s


def stat_read_stoic_matrix(path='data/Stoic_matrix_0.txt'):
    stoic_matrix = []
    with open(path, 'r') as f:
        for i in xrange(3):
            f.next()
        for line in f:
            stoic_matrix.append([int(i) for i in line.strip().split('  ')])
    return stoic_matrix


for dirpath, dirnames, filenames in os.walk('data/'):
    for filename in filenames:
        if filename.endswith('.txt'):
            matrix = stat_read_stoic_matrix(dirpath + filename)
            rev_vector = [0 for i in range(len(matrix[0]))]
            sampler = s.Sampler(matrix, rev_vector)
            print '{:<50}{:<25}'.format(filename, len(sampler.result))