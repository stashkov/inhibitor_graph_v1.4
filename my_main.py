import networkx as nx
import examples
import new_esampler as s
import os
import pathway_graph as ig
import copy
import efm_summary as efms
import time


def calculate_EFM():
    dirpath = 'data/'
    print('Processing files in {}'.format(dirpath))
    summary = efms.EFMSummary(dirpath)
    print('\nNumber of EFMs in expanded graph: {}'.format(summary.EFM_in_expanded_graph))
    summary.print_EFM_by_node()


def write_stoichimetric_matrices_to_files():
    stoichiometric_matrix = ig.InhibitionRemovalFromMethabolicPathway.stat_generate_stoichiometric_matrix(G)
    ig.InhibitionRemovalFromMethabolicPathway.stat_save_stoichimetric_matrix(stoichiometric_matrix)
    a = ig.InhibitionRemovalFromMethabolicPathway(G)
    a.save_stoichimetric_matrices(file_prefix='Stoic')
    a.save_graphml(file_prefix='graphML')
    for node in G.nodes():
        print('Working with node %s out of %s' % (node, len(G.nodes())))
        temp_graph = copy.deepcopy(G)
        temp_graph.remove_node(node)
        a = ig.InhibitionRemovalFromMethabolicPathway(temp_graph)
        a.save_stoichimetric_matrices(file_prefix='Stoic_remove_node' + str(node))
        a.save_graphml(file_prefix='GraphML_remove_node' + str(node))


if __name__ == '__main__':
    # G = generate_graph_test_loops()
    # G = examples.generate_barabasi(7)
    # G = examples.generate_graph()
    # G = examples.example30()
    G = examples.example31S2()

    nx.write_graphml(G, 'data/input_graph.graphml')

    print('Start generating stoichiometric matrices')
    start = time.time()
    write_stoichimetric_matrices_to_files()
    print('Stoichiometric Matrices generated in {} seconds'.format(int(time.time() - start)))
    start = time.time()
    calculate_EFM()
    print('\n#EFM calculated in {} seconds'.format(int(time.time() - start)))
