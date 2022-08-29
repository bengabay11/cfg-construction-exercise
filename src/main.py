from typing import List

import networkx as nx
import matplotlib.pyplot as plt

from src.cfg_construction import Assignment, Var, Expression, Operation, Jump, Call
from src.graph_draw import draw_graph
from src.graph_update import add_assignment, add_jump, add_call

graph_update_functions = {
    Assignment: lambda graph, current_node, assignment: add_assignment(graph, current_node, assignment),
    Jump: lambda graph, current_node, jump: add_jump(graph, current_node, jump),
    Call: lambda graph, current_node, call: add_call(graph, current_node, call)
}


def get_leader_indexes(instructions):
    leader_indexes = [0]
    for index, instruction in enumerate(instructions):
        if isinstance(instruction, Jump):
            leader_indexes.append(index + 1)
            leader_indexes.append(instruction.target-1)
    leader_indexes.sort()
    return leader_indexes


def get_basic_blocks(instructions: List, leader_indexes: List):
    basic_blocks = []
    i = 1
    for i in range(1, len(leader_indexes)):
        start_index = leader_indexes[i-1]
        end_index = leader_indexes[i]
        basic_blocks.append(instructions[start_index:end_index])
    start_index = leader_indexes[i]
    basic_blocks.append(instructions[start_index:])
    return basic_blocks


def create_jump_edge(graph: nx.Graph, leader_indexes: List[int], current_basic_block_index: int, jump: Jump):
    if jump.target - 1 in leader_indexes:
        target_basic_block_index = leader_indexes.index(jump.target - 1)
        graph.add_edge(current_basic_block_index, target_basic_block_index, jump=jump)


def build_cfg(instructions):
    graph = nx.DiGraph()
    leader_indexes = get_leader_indexes(instructions)
    basic_blocks = get_basic_blocks(instructions, leader_indexes)
    graph.add_node(0, instructions=basic_blocks[0])
    for i in range(1, len(basic_blocks)):
        graph.add_node(i, instructions=basic_blocks[i])
        graph.add_edge(i-1, i)
        if isinstance(basic_blocks[i][-1], Jump):
            create_jump_edge(graph, leader_indexes, i, basic_blocks[i][-1])
    draw_graph(graph)


def build_cfg_old(instructions):
    graph = nx.Graph()
    pos = nx.spring_layout(graph)
    current_node = (1, "Start")
    graph.add_node(current_node)
    for line, instruction in enumerate(instructions, start=1):
        current_node = graph_update_functions[type(instruction)](graph, current_node, instruction)
    nx.draw(graph, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels={}, font_color="red")
    plt.savefig("../path.png")


base = Var("base")
counter = Var("counter")
output = Var("output")
code = [
    Assignment(base, 2),  # 0
    Assignment(counter, 5),  # 1
    Assignment(output, 1),  # 2
    # Loop start
    Assignment(output, Expression(output, base, Operation.MUL)),  # 3
    Assignment(counter, Expression(counter, 1, Operation.SUB)),  # 4
    Jump(3, counter),  # 5
    Call("print", [output])  # 6
]
build_cfg(code)
