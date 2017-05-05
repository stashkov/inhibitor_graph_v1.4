
# TODO probably should be in another file


# TODO probably should be in another file
def plot_graph(*argv):
    plt.figure(1)
    for i, arg in enumerate(argv):
        plt.subplot(2, 2, i + 1)
        my_draw_graph(arg)
    plt.show()
    return None


@staticmethod
def my_draw_graph(graph):
    pos = nx.spring_layout(graph, k=5 / math.sqrt(graph.order()))  # k - Optimal distance between nodes.
    labels = dict()
    white_nodes, red_nodes = [], []
    for n, d in graph.nodes(data=True):
        labels[n] = str(d.get('info')) + ' ' + str(d.get('label', n)) + '\n' + str(d.get('flag', ''))
        if 'flag' not in d.keys() or d['flag'] is True:
            white_nodes.append(n)
        else:
            red_nodes.append(n)

    nx.draw_networkx_edges(graph, pos, width=3)
    nx.draw_networkx_nodes(graph, pos, node_size=3 * 3000, node_color='white', nodelist=white_nodes)
    nx.draw_networkx_nodes(graph, pos, node_size=3 * 3000, node_color='red', nodelist=red_nodes)
    nx.draw_networkx_labels(graph, pos, labels, font_size=15)


# TODO do I even need the following 4 func ?
def contract_nodes_candidates(graph):
    d = dict()
    for u in graph.nodes():
        # print graph.predecessors(u), len(graph.predecessors(u))
        predecessors = graph.predecessors(u)
        if len(predecessors) > 1:
            d[u] = predecessors
    return d


def contract_nodes_candidates_in_modified_graph(graph):
    nodes = dict()
    for u, d in graph.nodes(data=True):
        # print graph.predecessors(u), len(graph.predecessors(u))
        print u, d, graph.node[u]['label']

        predecessors = graph.predecessors(u)
        node_negation = graph.node[u]['label']
        if node_negation in predecessors:
            predecessors.remove(node_negation)

        if len(predecessors) > 1:
            nodes[u] = predecessors
    return nodes


def remove_out_degree_zero_nodes(graph):
    for v, d in graph.nodes(data=True):
        if graph.in_degree(v) == graph.out_degree(v) == 1 and graph.predecessors(v) == graph.successors(v):
            graph.remove_node(v)


def replace_inhibited_edges_with_negation_of_node(input_graph, output_graph):
    added_negative_nodes = set()
    next_node = max(input_graph.nodes())
    for u, v, d in input_graph.edges(data=True):
        if d['weight'] == 0:
            output_graph.add_node(u, label=u, flag=True)
            output_graph.add_node(v, label=v, flag=True)
            output_graph.add_edge(u, v, weight=0)
        if d['weight'] == 1:
            output_graph.add_node(u, label=u, flag=True)
            output_graph.add_node(v, label=v, flag=True)
            if v not in added_negative_nodes:
                added_negative_nodes.add(v)
                next_node += 1
                w = next_node
                output_graph.add_node(w, label=v, flag=False)
                output_graph.add_edge(u, w, weight=0)
                output_graph.add_edge(v, w, weight=0)  # self loop
                output_graph.add_edge(w, v, weight=0)  # self loop
            else:
                output_graph.add_edge(u, v, weight=0)
    return output_graph
