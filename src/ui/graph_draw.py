from typing import Dict, Callable

import networkx as nx
from matplotlib import pyplot as plt

from src.config import NODE_SIZE, NODE_SHAPE, FILE_PATH
from src.ui.str_assembly import str_instructions, str_jump_condition


class CFGDrawer(object):
    def __init__(self, graph: nx.DiGraph):
        self.graph = graph
        # pos = nx.spring_layout(graph)
        self.pos = nx.shell_layout(self.graph)
        # pos = nx.multipartite_layout(graph, subset_key="level", align="horizontal")
        self.general_draw_edge_options = {
            "G": self.graph,
            "pos": self.pos,
            "arrows": True,
            "node_size": NODE_SIZE,
            "node_shape": NODE_SHAPE
        }

    def draw(self):
        plt.figure(figsize=(20, 20))
        self.draw_nodes()
        self.draw_edges()
        plt.savefig(FILE_PATH)
        plt.show()

    def draw_nodes(self):
        node_labels = nx.get_node_attributes(self.graph, "instructions")
        node_labels = {node: str_instructions(instructions) for node, instructions in node_labels.items()}
        nx.draw_networkx_nodes(self.graph, self.pos, node_shape=NODE_SHAPE, node_size=NODE_SIZE)
        nx.draw_networkx_labels(self.graph, self.pos, labels=node_labels, font_size=6)

    def draw_edges(self):
        graph_edges = list(self.graph.edges(data=True))
        unconditional_edges = []
        conditional_edge_labels = {}
        for source, target, data in graph_edges:
            if data["condition"] is None:
                unconditional_edges.append((source, target))
            else:
                conditional_edge_labels[(source, target)] = str_jump_condition(**data)
        unconditional_edges_options = self.general_draw_edge_options
        unconditional_edges_options["edgelist"] = unconditional_edges
        nx.draw_networkx_edges(**unconditional_edges_options)
        conditional_edges_options = self.general_draw_edge_options
        conditional_edges_options["edgelist"] = conditional_edge_labels.keys()
        nx.draw_networkx_edges(**conditional_edges_options)
        nx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels=conditional_edge_labels)
