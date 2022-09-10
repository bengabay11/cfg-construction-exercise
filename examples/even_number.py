from typing import List

from src.cfg_construction import Var, Assignment, Jump, Call, Value, Expression, Operation
from src.main import build_cfg


def build_even_number_code() -> List:
    num = Var("num")
    result = Var("result")
    output = Var("output")
    return [
        Assignment(result, Expression(num, 2, Operation.DIV)),  # 0
        Jump(4, result),  # 1
        Call("even_number", [num]),  # 2
        Jump(5, None),  # 3
        Call("odd_number", [num]),  # 4
        Call("exit", [output])  # 5
    ]


code = build_even_number_code()
build_cfg(code)
