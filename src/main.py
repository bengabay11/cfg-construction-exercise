from typing import List

import networkx as nx

from src.cfg_construction import Assignment, Var, Expression, Operation, Jump, Call
from src.graph_draw import draw_graph


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


def create_cfg(instructions: List) -> nx.Graph:
    graph = nx.DiGraph()
    leader_indexes = get_leader_indexes(instructions)
    basic_blocks = get_basic_blocks(instructions, leader_indexes)
    graph.add_node(0, instructions=basic_blocks[0])
    for i in range(1, len(basic_blocks)):
        graph.add_node(i, instructions=basic_blocks[i])
        graph.add_edge(i - 1, i)
        if isinstance(basic_blocks[i][-1], Jump):
            create_jump_edge(graph, leader_indexes, i, basic_blocks[i][-1])
    return graph
