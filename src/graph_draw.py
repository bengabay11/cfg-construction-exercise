import networkx as nx
from matplotlib import pyplot as plt
# from networkx.drawing.nx_agraph import graphviz_layout

from src.node_display import instructions_node_display, display_jump_branch_taken

NODE_SIZE = 1000
NODE_SHAPE = "s"
ARROW_SIZE = 20
FILE_PATH = "../path.png"


def draw_nodes(graph, pos):
    node_labels = nx.get_node_attributes(graph, "instructions")
    node_labels = {node: instructions_node_display(instructions) for node, instructions in node_labels.items()}
    nx.draw_networkx_nodes(graph, pos, node_shape=NODE_SHAPE, node_size=NODE_SIZE)
    nx.draw_networkx_labels(graph, pos, labels=node_labels)


def draw_edges(graph, pos):
    edge_labels = nx.get_edge_attributes(graph, "jump")
    edge_labels = {edge: display_jump_branch_taken(jump) for edge, jump in edge_labels.items()}
    nx.draw_networkx_edges(graph, pos, arrows=True, node_size=NODE_SIZE, node_shape=NODE_SHAPE)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)


def draw_graph(graph):
    pos = nx.spring_layout(graph)
    draw_nodes(graph, pos)
    draw_edges(graph, pos)
    plt.savefig(FILE_PATH)
    plt.show()
