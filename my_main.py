import examples
import pathway_graph as ig
import copy

# G = examples.generate_barabasi(7); graph_name = 'barabasi'
G = examples.generate_graph()
# G = examples.example30(); graph_name = 'example30'
# G = generate_graph_test_loops()


# [save_graphml(G3, z) for G3 in result ]
# save_graphml(G3, z)
# save_stoichimetric_matrices(G3, z, file_prefix=graph_name)

a = ig.RemoveInhibitionFromMethabolicPathway(G)
a.save_stoichimetric_matrices(file_prefix='test')

for node in G.nodes():
    print node
    temp_graph = copy.deepcopy(G)
    temp_graph.remove_node(node)
    a = ig.RemoveInhibitionFromMethabolicPathway(temp_graph)
    a.save_stoichimetric_matrices(file_prefix='node' + str(node))

# TODO for each of generated stoichimetric matrices

# a.print_dict_of_actions(a.dict_of_actions)