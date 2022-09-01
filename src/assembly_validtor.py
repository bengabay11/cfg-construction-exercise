from typing import List

from src.cfg_construction import Jump, Expression, Operation, Var, Assignment, Call
from src.exceptions.invalid_assembly_instruction_exception import InvalidAssemblyInstruction
from src.exceptions.invalid_jump_target_exception import InvalidJumpTargetException


VALID_ASSEMBLY_INSTRUCTIONS = [Jump, Expression, Operation, Var, Assignment, Call]


def validate_jump(instructions_count: int, jump: Jump) -> None:
    if jump.target >= instructions_count or jump.target < 0:
        raise InvalidJumpTargetException(jump)


def validate_assembly_code(code: List) -> None:
    for line, instruction in enumerate(code):
        if isinstance(instruction, Jump):
            validate_jump(len(code), instruction)
        if type(instruction) not in VALID_ASSEMBLY_INSTRUCTIONS:
            raise InvalidAssemblyInstruction(instruction, line)
