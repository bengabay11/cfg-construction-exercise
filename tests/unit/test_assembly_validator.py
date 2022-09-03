import pytest

from src.assembly_validtor import validate_jump
from src.cfg_construction import Jump, Var
from src.exceptions.invalid_jump_target_exception import InvalidJumpTargetException


def test_jump_validator_valid_target():
    var1 = Var('var1')
    instructions_count = 6
    jump = Jump(5, var1)
    with pytest.raises(InvalidJumpTargetException):
        validate_jump(instructions_count, jump)


def test_jump_validator_big_target():
    var1 = Var('var1')
    instructions_count = 6
    jump = Jump(6, var1)
    with pytest.raises(InvalidJumpTargetException):
        validate_jump(instructions_count, jump)


def test_jump_validator_negative_target():
    var1 = Var('var1')
    instructions_count = 6
    jump = Jump(-1, var1)
    with pytest.raises(InvalidJumpTargetException):
        validate_jump(instructions_count, jump)

