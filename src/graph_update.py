import networkx as nx
from typing import Tuple
from networkx import Graph

from src.cfg_construction import Assignment, Jump, Call
from src.str_assembly import str_assignment, str_jump_branch_taken, str_call


def add_assignment(graph: Graph, current_node: Tuple[int, str], assignment: Assignment):
    current_line = current_node[0] + 1
    instruction_node = (current_line, str_assignment(assignment))
    graph.add_node(instruction_node)
    graph.add_edge(current_node, instruction_node)
    return instruction_node


def add_jump(graph: Graph, current_node: Tuple[int, str], jump: Jump):
    destination_node = next(filter(lambda node: node[0] == jump.target, graph.nodes), None)
    edge = (current_node, destination_node)
    graph.add_edge(*edge)
    pos = nx.spring_layout(graph)
    edge_label = str_jump_branch_taken(jump)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels={edge: edge_label}, font_color='red')
    return current_node


def add_call(graph: Graph, current_node: Tuple[int, str], call: Call):
    current_line = current_node[0] + 1
    instruction_node = (current_line, str_call(call))
    graph.add_node(instruction_node)
    graph.add_edge(current_node, instruction_node)
    return instruction_node
