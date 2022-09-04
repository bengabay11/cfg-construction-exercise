import networkx as nx

from src.cfg_builder import create_cfg_nodes
from src.cfg_construction import Assignment, Var, Call, Jump


def test_create_cfg_nodes_empty_basic_blocks(graph: nx.DiGraph) -> None:
    create_cfg_nodes(graph, [])
    assert list(graph.nodes) == []


def test_create_cfg_nodes(graph: nx.DiGraph, var: Var, exit_instruction: Call) -> None:
    basic_blocks = [
        [Assignment(var, 1), Jump(2, var)],
        [Call("print", [var])],
        exit_instruction
    ]
    create_cfg_nodes(graph, basic_blocks)
    assert len(graph.nodes) == len(basic_blocks)
    for i, node in enumerate(graph.nodes):
        assert i == node
    for i, basic_block in enumerate(basic_blocks):
        assert graph.nodes[i]["instructions"] == basic_block
        assert graph.nodes[i]["level"] == len(basic_blocks) - i - 1
