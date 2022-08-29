import networkx as nx
from typing import Tuple
from networkx import Graph

from src.cfg_construction import Assignment, Jump, Call
from src.node_display import display_assignment, display_jump_branch_taken, display_call


def add_assignment(graph: Graph, current_node: Tuple[int, str], assignment: Assignment):
    current_line = current_node[0] + 1
    instruction_node = (current_line, display_assignment(assignment))
    graph.add_node(instruction_node)
    graph.add_edge(current_node, instruction_node)
    return instruction_node


def add_jump(graph: Graph, current_node: Tuple[int, str], jump: Jump):
    destination_node = next(filter(lambda node: node[0] == jump.target, graph.nodes), None)
    edge = (current_node, destination_node)
    graph.add_edge(*edge)
    pos = nx.spring_layout(graph)
    edge_label = display_jump_branch_taken(jump)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels={edge: edge_label}, font_color='red')
    return current_node


def add_call(graph: Graph, current_node: Tuple[int, str], call: Call):
    current_line = current_node[0] + 1
    instruction_node = (current_line, display_call(call))
    graph.add_node(instruction_node)
    graph.add_edge(current_node, instruction_node)
    return instruction_node
