import networkx as nx
import pytest

from src.cfg_builder import create_jump_edges
from src.cfg_construction import Jump, Var


def test_create_jump_edges(graph: nx.DiGraph, var: Var) -> None:
    pass


def test_create_jump_edges_unconditional_jump() -> None:
    pass


def test_create_jump_edges_target_not_leader() -> None:
    pass


def test_create_jump_edges_jump_last_instruction() -> None:
    pass
