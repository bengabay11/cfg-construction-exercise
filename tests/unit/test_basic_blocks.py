from src.cfg_construction import Assignment, Var, Call, Jump
from src.models.basic_block import BasicBlock
from tests.unit.utils import test_basic_blocks


def test_get_basic_blocks_unconditional_jump(var: Var, exit_instruction: Call):
    instructions = [
        Assignment(var, 1),
        Jump(3, None),
        Assignment(var, 2),
        exit_instruction
    ]
    expected_basic_blocks = [
        BasicBlock(0, [Assignment(var, 1), Jump(3, None)]),
        BasicBlock(1, [Assignment(var, 2)]),
        BasicBlock(2, [exit_instruction]),
    ]
    test_basic_blocks(instructions, expected_basic_blocks)


def test_get_basic_blocks_one_block(var: Var, exit_instruction: Call):
    instructions = [
        Assignment(var, 1),
        Call("print", [0]),
        exit_instruction
    ]
    expected_basic_blocks = [
        BasicBlock(0, [Assignment(var, 1), Call("print", [0]), exit_instruction])
    ]
    test_basic_blocks(instructions, expected_basic_blocks)


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
    test_basic_blocks(instructions, expected_basic_blocks, leader_indexes=leader_indexes)


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
    test_basic_blocks(instructions, expected_basic_blocks, leader_indexes=leader_indexes)


def test_get_basic_blocks_empty_code():
    test_basic_blocks([], [], [])
