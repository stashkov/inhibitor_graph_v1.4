import networkx as nx
import examples
import new_esampler as s
import os
import pathway_graph as ig
import copy
import efm_summary as efms
import time

# G = examples.generate_barabasi(7); graph_name = 'barabasi'
# G = examples.generate_graph()


# G = examples.example30()
G = examples.example31S2()
# G = generate_graph_test_loops()


nx.write_graphml(G, 'data/input_graph.graphml')

# [save_graphml(G3, z) for G3 in result ]
# save_graphml(G3, z)
# save_stoichimetric_matrices(G3, z, file_prefix=graph_name)


start = time.time()

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

print('Stoichiometric Matrices generated in %s' % str(time.time() - start))
start = time.time()

# ----summary

dirpath = 'data/'
print('Processing files in {}'.format(dirpath))
summary = efms.EFMSummary(dirpath)

print('\nNumber of EFMs in expanded graph: {}'.format(summary.EFM_in_expanded_graph))
summary.print_EFM_by_node()

print('#EFM calculated in %s' % str(time.time() - start))
