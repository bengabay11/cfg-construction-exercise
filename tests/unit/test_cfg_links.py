from src.cfg_construction import Var, Assignment, Call, Jump
from src.logic.assembly_validtor import validate_assembly_code
from src.logic.cfg_builder import CFGBuilder
from src.models.basic_block import BasicBlock
from src.models.link import Link


def test_create_create_conditional_jump_link(var: Var) -> None:
    cfg_builder = CFGBuilder("test_cfg", [], validate_assembly_code)
    cfg_builder.cfg.basic_blocks = [BasicBlock(0, []), BasicBlock(1, []), BasicBlock(2, [])]
    cfg_builder.create_conditional_jump_links(var, 0, 2)
    sorted_cfg_links = sorted(cfg_builder.cfg.links, key=lambda link: link.target)
    assert sorted_cfg_links == [Link(0, 1, var, branch_taken=False), Link(0, 2, var, branch_taken=True)]


def test_create_create_unconditional_jump_link(var: Var) -> None:
    cfg_builder = CFGBuilder("test_cfg", [], validate_assembly_code)
    cfg_builder.create_unconditional_jump_link(1, 3)
    assert cfg_builder.cfg.links == [Link(1, 3)]


def test_create_create_conditional_jump_links_last_instruction(var: Var, exit_instruction: Call) -> None:
    instructions = [
        Assignment(var, 1),
        Jump(3, None),
        Assignment(var, 2),
        Jump(0, var),
    ]
    cfg_builder = CFGBuilder("test_cfg", instructions, validate_assembly_code)
    cfg_builder.cfg.basic_blocks = [
        BasicBlock(0, [Assignment(var, 1), Jump(3, None)]),
        BasicBlock(2, [Assignment(var, 2)]),
        BasicBlock(3, [Jump(0, var)])
    ]
    cfg_builder.create_conditional_jump_links(var, 2, 0)
    expected_links = [
        Link(2, 0, condition=var, branch_taken=True),
    ]
    assert cfg_builder.cfg.links == expected_links
