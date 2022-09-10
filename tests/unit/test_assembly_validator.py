import pytest

from src.logic.assembly_validtor import validate_jump, validate_assembly_code
from src.cfg_construction import Jump, Var, Assignment, Call, Expression, Operation
from src.exceptions.invalid_assembly_instruction_exception import InvalidAssemblyInstruction
from src.exceptions.invalid_jump_target_exception import InvalidJumpTargetException


def test_jump_validator_valid_target(var: Var):
    instructions_count = 6
    jump = Jump(5, var)
    validate_jump(instructions_count, jump)


def test_jump_validator_big_target(var: Var):
    instructions_count = 6
    jump = Jump(6, var)
    with pytest.raises(InvalidJumpTargetException):
        validate_jump(instructions_count, jump)


def test_jump_validator_negative_target(var: Var):
    instructions_count = 6
    jump = Jump(-1, var)
    with pytest.raises(InvalidJumpTargetException):
        validate_jump(instructions_count, jump)


def test_empty_assembly_code():
    validate_assembly_code([])


def test_assembly_code_valid(var: Var, exit_instruction: Call):
    code = [
        Assignment(var, 1),
        Assignment(var, Expression(var, 2, Operation.MUL)),
        Jump(0, var),
        exit_instruction
    ]
    validate_assembly_code(code)


def test_assembly_code_invalid_instruction(var: Var, exit_instruction: Call):
    code = [
        Assignment(var, 1),
        "test",
        exit_instruction
    ]
    with pytest.raises(InvalidAssemblyInstruction):
        validate_assembly_code(code)


def test_assembly_code_not_iterable_code():
    code = 6
    with pytest.raises(TypeError):
        validate_assembly_code(code)


def test_assembly_code_iterable_invalid_code():
    code = "test"
    with pytest.raises(TypeError):
        validate_assembly_code(code)
