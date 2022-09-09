from typing import Tuple

import networkx as nx
from matplotlib import pyplot as plt

from src.ui.str_assembly import str_instructions, str_jump_condition


class CFGDrawer(object):
    def __init__(self, graph: nx.DiGraph, node_size: int = 300, node_shape: str = "o", arrows: bool = True,
                 figize: Tuple[int, int] = None):
        self.graph = graph
        # self.pos = nx.spring_layout(self.graph)
        self.pos = nx.shell_layout(self.graph)
        # self.pos = nx.multipartite_layout(graph, subset_key="level", align="horizontal")
        self.figsize = figize
        self.node_shape = node_shape
        self.node_size = node_size
        self.general_draw_edge_options = {"G": self.graph, "pos": self.pos, "arrows": arrows, "node_size": node_size,
                                          "node_shape": node_shape}

    def draw(self, output_file: str = None):
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
        nx.draw_networkx_labels(self.graph, self.pos, labels=node_labels, font_size=10)

    def draw_edges(self, branch_taken_color: str = "k"):
        graph_edges = list(self.graph.edges(data=True))
        regular_edges = []
        branch_taken_edge_labels = {}
        branch_not_taken_edge_labels = {}
        self_loops_edge_labels = {}
        for source, target, data in graph_edges:
            if data["branch_taken"] is None:
                regular_edges.append((source, target))
            else:
                if data["branch_taken"]:
                    if source != target:
                        branch_taken_edge_labels[(source, target)] = str_jump_condition(**data)
                    else:
                        self_loops_edge_labels[(source, target)] = str_jump_condition(**data)
                else:
                    branch_not_taken_edge_labels[(source, target)] = str_jump_condition(**data)
        if self_loops_edge_labels:
            self.draw_edge_group(self_loops_edge_labels.keys(), "g", self_loops_edge_labels)
        if branch_taken_edge_labels:
            self.draw_edge_group(branch_taken_edge_labels.keys(), "g", branch_taken_edge_labels)
        if branch_not_taken_edge_labels:
            self.draw_edge_group(branch_not_taken_edge_labels.keys(), "r", branch_not_taken_edge_labels)
        self.draw_edge_group(regular_edges)

    def draw_edge_group(self, edge_list, color="k", edge_labels=None, node_size=None):
        edge_options = self.general_draw_edge_options
        edge_options["edgelist"] = edge_list
        edge_options["edge_color"] = color
        if node_size:
            edge_options["node_size"] = node_size
        nx.draw_networkx_edges(**edge_options)
        if edge_labels:
            nx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels=edge_labels, label_pos=0.75)

    # def _get_node_size(self, node_data):
    #     longest_line = max(node_data, key=len)
    #     lines_count = len(node_data.split("\n"))
    #     max_chars = max(longest_line, lines_count)

