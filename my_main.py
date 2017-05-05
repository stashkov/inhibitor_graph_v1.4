import examples
import pathway_graph as ig

# G = examples.generate_barabasi(7); graph_name = 'barabasi'
G = examples.generate_graph()
# G = examples.example30(); graph_name = 'example30'
# G = generate_graph_test_loops()


# [save_graphml(G3, z) for G3 in result ]
# save_graphml(G3, z)
# save_matrix(G3, z, file_prefix=graph_name)

a = ig.RemoveInhibitionFromMethabolicPathway(G)
for i, graph in enumerate(a.result):
    a.save_matrix(graph=graph, sequential_number=i, file_prefix='test')
    a.save_graphml(graph=graph, sequential_number=i, file_prefix='test')


# a.print_dict_of_actions(a.dict_of_actions)