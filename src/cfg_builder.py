from typing import List

import networkx as nx

from src.assembly_validtor import validate_assembly_code
from src.cfg_construction import Jump


def get_leader_indexes(instructions):
    leader_indexes = {0}
    for index, instruction in enumerate(instructions):
        if isinstance(instruction, Jump):
            leader_indexes.add(index + 1)
            leader_indexes.add(instruction.target)
    return sorted(leader_indexes)


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
    if jump.target in leader_indexes:
        target_basic_block_index = leader_indexes.index(jump.target)
        graph.add_edge(current_basic_block_index, target_basic_block_index, jump=jump)
        graph.add_edge(current_basic_block_index, current_basic_block_index + 1, no_jump=jump)


def create_cfg_nodes(graph: nx.Graph, basic_blocks: List):
    for i in range(0, len(basic_blocks)):
        graph.add_node(i, instructions=basic_blocks[i], level=len(basic_blocks)-1-i)


def create_cfg_edges(graph: nx.Graph, basic_blocks: List, leader_indexes: List[int]):
    for index, basic_block in enumerate(basic_blocks):
        if isinstance(basic_block[-1], Jump):
            create_jump_edge(graph, leader_indexes, index, basic_block[-1])
        elif index < len(basic_blocks) - 1:
            graph.add_edge(index, index + 1)


def create_cfg(instructions: List) -> nx.Graph:
    validate_assembly_code(instructions)
    graph = nx.DiGraph()
    leader_indexes = get_leader_indexes(instructions)
    basic_blocks = get_basic_blocks(instructions, leader_indexes)
    create_cfg_nodes(graph, basic_blocks)
    create_cfg_edges(graph, basic_blocks, leader_indexes)
    return graph
