from typing import Tuple

import networkx as nx
from matplotlib import pyplot as plt

from src.ui.str_assembly import str_instructions, str_jump_condition


class CFGDrawer(object):
    def __init__(self, graph: nx.DiGraph, node_size: int = 300, node_shape: str = "o", arrows: bool = True, figize: Tuple[int, int] = None):
        self.graph = graph
        # pos = nx.spring_layout(graph)
        self.pos = nx.shell_layout(self.graph)
        # pos = nx.multipartite_layout(graph, subset_key="level", align="horizontal")
        self.figsize = figize
        self.node_shape = node_shape
        self.node_size = node_size
        self.general_draw_edge_options = {
            "G": self.graph,
            "pos": self.pos,
            "arrows": arrows,
            "node_size": node_size,
            "node_shape": node_shape
        }

    def draw(self, output_file: str):
        plt.figure(figsize=self.figsize)
        self.draw_nodes()
        self.draw_edges()
        if output_file:
            plt.savefig(output_file)
        plt.show()

    def draw_nodes(self):
        node_labels = nx.get_node_attributes(self.graph, "instructions")
        node_labels = {node: str_instructions(instructions) for node, instructions in node_labels.items()}
        nx.draw_networkx_nodes(self.graph, self.pos, node_shape=self.node_shape, node_size=self.node_size)
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
