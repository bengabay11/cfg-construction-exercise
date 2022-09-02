from typing import List

from src.cfg_construction import Var, Assignment, Jump, Call, Value
from src.main import build_cfg


def build_if_statement_code() -> List:
    result = Var("result")
    output = Var("output")
    true = Var("true")
    return [
        Assignment(result, 6 % 2),  # 0
        Jump(4, result),  # 1
        Call("even_number", [6]),  # 2
        Jump(5, None),  # 4
        Call("odd_number", [6]),  # 4
        Call("exit", [output])  # 5
    ]


code = build_if_statement_code()
build_cfg(code)
