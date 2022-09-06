from typing import List

import networkx as nx
import pytest

from src.cfg_construction import Call, Var
from src.logic.cfg import CFG
from src.logic.cfg_builder import CFGBuilder
from src.models.basic_block import BasicBlock


@pytest.fixture(scope="module")
def exit_instruction():
    return Call("exit", [0])


@pytest.fixture(scope="module")
def var():
    return Var("var")


@pytest.fixture(scope="function")
def graph():
    return nx.DiGraph()
