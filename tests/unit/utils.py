from typing import List

import pytest

from src.logic.assembly_validtor import validate_assembly_code
from src.logic.cfg_builder import CFGBuilder
from src.models.basic_block import BasicBlock


@pytest.mark.skip
def test_basic_blocks(instructions: List, expected_basic_blocks: List[BasicBlock], leader_indexes: List[int] = None):
    cfg_builder = CFGBuilder("test_cfg", instructions, validate_assembly_code)
    if not leader_indexes:
        leader_indexes = cfg_builder.get_leader_indexes()
    cfg_builder.add_basic_blocks_to_cfg(leader_indexes)
    assert cfg_builder.cfg.basic_blocks == expected_basic_blocks
    assert len(cfg_builder.cfg.graph.nodes) == len(expected_basic_blocks)
    for i, node in enumerate(cfg_builder.cfg.graph.nodes):
        assert i == node
    for i, basic_block in enumerate(expected_basic_blocks):
        assert i == basic_block.index
        assert cfg_builder.cfg.graph.nodes[i]["instructions"] == basic_block.instructions


@pytest.mark.skip
def test_get_leader_indexes(code: List, expected_leader_indexes: List[int]) -> None:
    cfg_builder = CFGBuilder("test_graph", code, validate_assembly_code)
    leader_indexes = cfg_builder.get_leader_indexes()
    assert leader_indexes == expected_leader_indexes
