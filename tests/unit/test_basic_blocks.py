from src.cfg_builder import get_basic_blocks, get_leader_indexes
from src.cfg_construction import Var, Assignment, Call

var1 = Var("var1")
one_block_code = [
    Assignment(var1, 1),
    Call("test", [var1])
]


def test_get_basic_blocks():
    leader_indexes = get_leader_indexes(one_block_code)
    basic_blocks = get_basic_blocks(one_block_code, leader_indexes)
    assert basic_blocks == [one_block_code]


def test_get_basic_blocks_empty_code():
    leader_indexes = get_leader_indexes([])
    basic_blocks = get_basic_blocks(one_block_code, leader_indexes)
    assert basic_blocks == []
