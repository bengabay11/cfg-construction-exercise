import pytest

from src.cfg_builder import get_basic_blocks
from src.cfg_construction import Assignment, Var, Call


def test_get_basic_blocks_no_jumps(var: Var, exit_instruction: Call):
    leader_indexes = [0]
    instructions = [
        Assignment(var, 1),
        exit_instruction
    ]
    basic_blocks = get_basic_blocks(instructions, leader_indexes)
    assert basic_blocks == [instructions]


def test_get_basic_blocks_two_blocks(var: Var, exit_instruction: Call):
    leader_indexes = [0, 1]
    instructions = [
        Assignment(var, 1),
        Call("print", [0]),
        exit_instruction
    ]
    basic_blocks = get_basic_blocks(instructions, leader_indexes)
    assert basic_blocks == [[Assignment(var, 1)], [Call("print", [0]), exit_instruction]]


def test_get_basic_blocks_three_blocks(var: Var, exit_instruction: Call):
    leader_indexes = [0, 1, 2]
    instructions = [
        Assignment(var, 1),
        Call("print", [0]),
        exit_instruction
    ]
    basic_blocks = get_basic_blocks(instructions, leader_indexes)
    assert basic_blocks == [[Assignment(var, 1)], [Call("print", [0])], [exit_instruction]]


def test_get_basic_blocks_empty_code():
    basic_blocks = get_basic_blocks([], [])
    assert basic_blocks == []
