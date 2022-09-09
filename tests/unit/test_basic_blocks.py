from typing import List

import pytest

from src.cfg_construction import Assignment, Var, Call
from src.logic.assembly_validtor import validate_assembly_code
from src.logic.cfg_builder import CFGBuilder
from src.models.basic_block import BasicBlock


@pytest.mark.skip
def test_basic_blocks(instructions: List, leader_indexes: List[int], expected_basic_blocks: List[BasicBlock]):
    cfg_builder = CFGBuilder("test_cfg", instructions, validate_assembly_code)
    cfg_builder.add_basic_blocks_to_cfg(leader_indexes)
    assert cfg_builder.cfg.basic_blocks == expected_basic_blocks
    assert len(cfg_builder.cfg.graph.nodes) == len(expected_basic_blocks)
    for i, node in enumerate(cfg_builder.cfg.graph.nodes):
        assert i == node
    for i, basic_block in enumerate(expected_basic_blocks):
        assert i == basic_block.index
        assert cfg_builder.cfg.graph.nodes[i]["instructions"] == basic_block.instructions


def test_get_basic_blocks_one_block(var: Var, exit_instruction: Call):
    leader_indexes = [0]
    instructions = [
        Assignment(var, 1),
        Call("print", [0]),
        exit_instruction
    ]
    expected_basic_blocks = [
        BasicBlock(0, [Assignment(var, 1), Call("print", [0]), exit_instruction])
    ]
    test_basic_blocks(instructions, leader_indexes, expected_basic_blocks)


def test_get_basic_blocks_two_blocks(var: Var, exit_instruction: Call):
    leader_indexes = [0, 1]
    instructions = [
        Assignment(var, 1),
        Call("print", [0]),
        exit_instruction
    ]
    expected_basic_blocks = [
        BasicBlock(0, [Assignment(var, 1)]),
        BasicBlock(1, [Call("print", [0]), exit_instruction])
    ]
    test_basic_blocks(instructions, leader_indexes, expected_basic_blocks)


def test_get_basic_blocks_three_blocks(var: Var, exit_instruction: Call):
    leader_indexes = [0, 1, 2]
    instructions = [
        Assignment(var, 1),
        Call("print", [0]),
        exit_instruction
    ]
    expected_basic_blocks = [
        BasicBlock(0, [Assignment(var, 1)]),
        BasicBlock(1, [Call("print", [0])]),
        BasicBlock(2, [exit_instruction])
    ]
    test_basic_blocks(instructions, leader_indexes, expected_basic_blocks)


def test_get_basic_blocks_empty_code():
    test_basic_blocks([], [], [])
