import networkx as nx
import examples
import new_esampler as s
import os
import pathway_graph as ig
import copy
import efm_summary as efms
import time
import csv


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


def write_results_to_a_file(filename):
    with open('data/' + filename + '.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        spamwriter.writerow(
            ['Node',
             'Name',
             'Degree Centrality',
             'Betweenness Centrality',
             'PageRank',
             'IsSignificant',
             '#EFM minus node',
             '#EFM Total',
             '#EFM-v / #EFM Total'])
        for i in G.nodes():
            if G.node[i].get('isEssential', 'no data').isdigit():
                spamwriter.writerow(
                    [
                        i,
                        G.node[i]['info'],
                        nx.degree_centrality(G)[i],
                        nx.betweenness_centrality(G)[i],
                        nx.pagerank_scipy(G)[i],
                        G.node[i].get('isEssential', 'no data'),
                        efm_summary.EFM_by_nodes[i],
                        efm_summary.EFM_in_expanded_graph,
                        efms.EFMSummary.calculate_ratio(efm_summary.EFM_by_nodes[i], efm_summary.EFM_in_expanded_graph)
                    ])


if __name__ == '__main__':
    # G = generate_graph_test_loops()
    # G = examples.generate_barabasi(7)
    # G = examples.generate_graph()
    G = examples.example30()
    # G = examples.example31S2()
    # G = examples.example32S3()
    # G = examples.example32S4()

    dirpath = 'data/'

    start = time.time()
    nx.write_graphml(G, 'data/input_graph.graphml')

    print('Start generating stoichiometric matrices')
    write_stoichimetric_matrices_to_files()
    print('Stoichiometric Matrices generated in {} seconds'.format(int(time.time() - start)))

    start = time.time()
    print('Processing files in {}'.format(dirpath))
    efm_summary = efms.EFMSummary(dirpath)
    print('\n#EFM calculated in {} seconds'.format(int(time.time() - start)))

    write_results_to_a_file('S1')

