from typing import Tuple

import networkx as nx
from matplotlib import pyplot as plt

from src.ui.str_assembly import str_instructions, str_jump_condition


class CFGDrawer(object):
    def __init__(self, graph, **kwargs):
        self.graph = graph
        self.pos = nx.shell_layout(self.graph)
        self.node_shape = kwargs["node_shape"]
        self.node_size = kwargs["node_size"]
        self.font_size = kwargs["font_size"]
        self.general_draw_edge_options = {
            "G": self.graph,
            "pos": self.pos,
            "arrows": kwargs["arrows"],
            "node_size": self.node_size,
            "node_shape": self.node_shape
        }

    def draw(self, plt_title: str = None, output_file: str = None, figzie: Tuple[int, int] = (10, 10)):
        plt.figure(figsize=figzie)
        self.draw_nodes()
        self.draw_edges()
        if output_file:
            plt.savefig(output_file)
        if plt_title:
            plt.title(plt_title)
        plt.show()

    def draw_nodes(self):
        node_labels = nx.get_node_attributes(self.graph, "instructions")
        node_labels = {node: str_instructions(instructions) for node, instructions in node_labels.items()}
        nx.draw_networkx_nodes(self.graph, self.pos, node_shape=self.node_shape, node_size=self.node_size)
        nx.draw_networkx_labels(self.graph, self.pos, labels=node_labels, font_size=10)

    def draw_edges(self):
        graph_edges = list(self.graph.edges(data=True))
        regular_edges = []
        branch_taken_edge_labels = {}
        branch_not_taken_edge_labels = {}
        for source, target, data in graph_edges:
            if data["branch_taken"] is None:
                regular_edges.append((source, target))
            else:
                if data["branch_taken"]:
                    branch_taken_edge_labels[(source, target)] = str_jump_condition(**data)
                else:
                    branch_not_taken_edge_labels[(source, target)] = str_jump_condition(**data)
        self.draw_edge_group(branch_taken_edge_labels.keys(), "g", branch_taken_edge_labels)
        self.draw_edge_group(branch_not_taken_edge_labels.keys(), "r", branch_not_taken_edge_labels)
        self.draw_edge_group(regular_edges)

    def draw_edge_group(self, edge_list, color="k", edge_labels=None):
        edge_options = self.general_draw_edge_options
        edge_options["edgelist"] = edge_list
        edge_options["edge_color"] = color
        nx.draw_networkx_edges(**edge_options)
        if edge_labels:
            nx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels=edge_labels)
