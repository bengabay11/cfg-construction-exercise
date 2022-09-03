from typing import List

from src.cfg_construction import Var, Assignment, Expression, Operation, Jump, Call
from src.main import build_cfg


def build_print_even_numbers_code() -> List:
    max_num = Var("max_num")
    current_num = Var("current_num")
    result = Var("result")
    return [
        Assignment(max_num, 10),  # 0
        Assignment(current_num, 0),  # 1
        Assignment(result, Expression(current_num, 2, Operation.DIV)),  # 2
        Jump(6, result),  # 3
        Call("printEvenNum", [current_num]),  # 4
        Jump(7, None),  # 5
        Call("printOddNum", [current_num]),  # 6
        Assignment(current_num, Expression(current_num, 1, Operation.ADD)),  # 7
        Assignment(current_num, Expression(max_num, 1, Operation.SUB)),  # 8
        Jump(2, max_num),  # 9
        Call("exit", [0])  # 10
    ]


code = build_print_even_numbers_code()
build_cfg(code)
