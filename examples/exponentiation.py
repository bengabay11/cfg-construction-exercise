from typing import List

from src.cfg_construction import Var, Assignment, Expression, Operation, Jump, Call
from src.main import build_cfg


def build_exponentiation_code() -> List:
    base = Var("base")
    counter = Var("counter")
    output = Var("output")
    return [
        Assignment(base, 2),  # 0
        Assignment(counter, 5),  # 1
        Assignment(output, 1),  # 2
        # Loop start
        Assignment(output, Expression(output, base, Operation.MUL)),  # 3
        Assignment(counter, Expression(counter, 1, Operation.SUB)),  # 4
        Jump(3, counter),  # 5
        Call("print", [output])  # 6
    ]


code = build_exponentiation_code()
build_cfg(code)
