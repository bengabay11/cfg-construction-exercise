from src.cfg_construction import Var, Assignment, Call, Jump
from tests.unit.utils import test_get_leader_indexes


def test_get_leader_indexes_no_jumps(var: Var, exit_instruction: Call) -> None:
    code = [
        Assignment(var, 1),
        exit_instruction
    ]
    test_get_leader_indexes(code, [0])


def test_get_leader_indexes_empty_code():
    test_get_leader_indexes([], [])


def test_get_leader_indexes_jump(var: Var, exit_instruction: Call):
    code = [
        Assignment(var, 1),
        Jump(4, var),
        Assignment(var, 0),
        Call("print", [var]),
        exit_instruction
    ]
    test_get_leader_indexes(code, [0, 2, 4])


def test_get_leader_indexes_first_line_target(var: Var, exit_instruction: Call) -> None:
    code = [
        Assignment(var, 1),
        Jump(0, var),
        exit_instruction
    ]
    test_get_leader_indexes(code, [0, 2])


def test_get_leader_indexes_jump_last_instruction(var: Var) -> None:
    code = [
        Assignment(var, 1),
        Call("print", [var]),
        Jump(1, var),
    ]
    test_get_leader_indexes(code, [0, 1])


def test_get_leader_indexes_unconditional_jump(var: Var, exit_instruction: Call) -> None:
    code = [
        Assignment(var, 1),
        Jump(3, None),
        Call("print", [var]),
        exit_instruction
    ]
    test_get_leader_indexes(code, [0, 2, 3])
