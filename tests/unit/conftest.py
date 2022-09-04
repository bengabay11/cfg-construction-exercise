import pytest

from src.cfg_construction import Call, Var


@pytest.fixture(scope="module")
def exit_instruction():
    return Call("exit", [0])


@pytest.fixture(scope="module")
def var():
    return Var("var")
