import networkx as nx
import examples
import new_esampler as s
import os
import pathway_graph as ig
import copy

# G = examples.generate_barabasi(7); graph_name = 'barabasi'
G = examples.generate_graph()


# G = examples.example30(); graph_name = 'example30'
# G = generate_graph_test_loops()


# [save_graphml(G3, z) for G3 in result ]
# save_graphml(G3, z)
# save_stoichimetric_matrices(G3, z, file_prefix=graph_name)


stoichiometric_matrix = ig.InhibitionRemovalFromMethabolicPathway.stat_generate_stoichiometric_matrix(G)
ig.InhibitionRemovalFromMethabolicPathway.stat_save_stoichimetric_matrix(stoichiometric_matrix)

a = ig.InhibitionRemovalFromMethabolicPathway(G)
a.save_stoichimetric_matrices(file_prefix='Stoic')
a.save_graphml(file_prefix='graphML')

for node in G.nodes():
    temp_graph = copy.deepcopy(G)
    temp_graph.remove_node(node)
    a = ig.InhibitionRemovalFromMethabolicPathway(temp_graph)
    a.save_stoichimetric_matrices(file_prefix='Stoic_remove_node' + str(node))
    a.save_graphml(file_prefix='GraphML_remove_node' + str(node))


for dirpath, dirnames, filenames in os.walk('data/'):
    for filename in filenames:
        if filename.endswith('.txt'):
            matrix = ig.InhibitionRemovalFromMethabolicPathway.stat_read_stoic_matrix(dirpath + filename)
            rev_vector = [0 for i in range(len(matrix[0]))]
            sampler = s.Sampler(matrix, rev_vector)
            print '{:<50}{:<25}'.format(filename, len(sampler.result))
