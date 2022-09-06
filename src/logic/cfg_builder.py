from typing import List

from src.logic.assembly_validtor import AssemblyValidator
from src.models.basic_block import BasicBlock
from src.logic.cfg import CFG
from src.cfg_construction import Jump
from src.models.link import Link


class CFGBuilder(object):
    def __init__(self, graph_name: str, code: List[any], assembly_validator: AssemblyValidator) -> None:
        self.code = code
        self.cfg = CFG(graph_name)
        self.assembly_validator = assembly_validator

    def build(self) -> CFG:
        self.assembly_validator.validate()
        leader_indexes = self.get_leader_indexes()
        self.add_basic_blocks_to_cfg(leader_indexes)
        self.add_links_to_cfg(leader_indexes)
        return self.cfg

    def get_leader_indexes(self) -> List[int]:
        if not self.code:
            return []
        leader_indexes = {0}
        for index, instruction in enumerate(self.code):
            if isinstance(instruction, Jump):
                if instruction.condition and index < len(self.code) - 1:
                    leader_indexes.add(index + 1)
                leader_indexes.add(instruction.target)
        return sorted(leader_indexes)

    def add_basic_blocks_to_cfg(self, leader_indexes: List) -> None:
        basic_blocks_ranges = zip(leader_indexes, leader_indexes[1:] + [None])
        for index, (start, end) in enumerate(basic_blocks_ranges):
            basic_block = BasicBlock(index, self.code[start:end])
            self.cfg.add_basic_block(basic_block)

    def create_conditional_jump_links(self, jump: Jump, current_basic_block_index: int, target_basic_block_index: int):
        branch_taken_link = Link(current_basic_block_index, target_basic_block_index, jump.condition, True)
        self.cfg.add_link(branch_taken_link)
        branch_not_taken_link = Link(current_basic_block_index, current_basic_block_index + 1, jump.condition, False)
        self.cfg.add_link(branch_not_taken_link)

    def create_unconditional_jump_link(self, current_basic_block_index: int, target_basic_block_index: int):
        unconditional_link = Link(current_basic_block_index, target_basic_block_index)
        self.cfg.add_link(unconditional_link)

    def create_jump_links(self, leader_indexes: List[int], current_basic_block_index: int, jump: Jump) -> None:
        if jump.target in leader_indexes:
            target_basic_block_index = leader_indexes.index(jump.target)
            if jump.condition and current_basic_block_index < len(self.cfg.basic_blocks) - 1:
                self.create_conditional_jump_links(jump, current_basic_block_index, target_basic_block_index)
            else:
                self.create_unconditional_jump_link(current_basic_block_index, target_basic_block_index)

    def add_links_to_cfg(self, leader_indexes: List[int]) -> None:
        for basic_block in self.cfg.basic_blocks:
            if isinstance(basic_block.instructions[-1], Jump):
                self.create_jump_links(leader_indexes, basic_block.index, basic_block.instructions[-1])
            elif basic_block.index < len(self.cfg.basic_blocks) - 1:
                link = Link(basic_block.index, basic_block.index + 1)
                self.cfg.add_link(link)
