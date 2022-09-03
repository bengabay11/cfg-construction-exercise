from src.cfg_builder import get_leader_indexes
from src.cfg_construction import Var, Assignment, Call, Jump

var1 = Var("var1")
one_block_code = [
    Assignment(var1, 1),
    Call("test", [var1])
]


def test_get_leader_indexes():
    leader_indexes = get_leader_indexes(one_block_code)
    assert leader_indexes == [0]


def test_get_leader_indexes_empty_code():
    leader_indexes = get_leader_indexes([])
    assert leader_indexes == []


def test_get_leader_indexes_jump():
    code = [
        Assignment(var1, 1),
        Jump(4, var1),
        Assignment(var1, 0),
        Call("print", [var1]),
        Call("exit", [0])
    ]
    leader_indexes = get_leader_indexes(code)
    assert leader_indexes == [0, 2, 4]


def test_get_leader_indexes_first_line_target():
    code = [
        Assignment(var1, 1),
        Jump(0, var1),
    ]
    leader_indexes = get_leader_indexes(code)
    assert leader_indexes == [0]


def test_get_leader_indexes_unconditional_jump():
    code = [
        Assignment(var1, 1),
        Jump(3, None),
        Call("print", [var1]),
        Call("exit", [0])
    ]
    leader_indexes = get_leader_indexes(code)
    assert leader_indexes == [0, 3]
