import examples
import pathway_graph as ig

# G = examples.generate_barabasi(7); graph_name = 'barabasi'
G = examples.generate_graph()
# G = examples.example30(); graph_name = 'example30'
# G = generate_graph_test_loops()

G1, G2, dict_test = ig.dictionary_of_actions(G)
result = ig.merge_G1_and_G3(G1, G2, dict_test)

# [save_graphml(G3, z) for G3 in result ]
# save_graphml(G3, z)
# save_matrix(G3, z, file_prefix=graph_name)

