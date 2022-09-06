from typing import List, Optional

from src.cfg_construction import Expression, Operation, Value, Var, Assignment, Jump, Call

EXPRESSION_OPERATIONS_DISPLAY = {
    Operation.MUL: "*",
    Operation.SUB: "-",
    Operation.ADD: "+",
    Operation.DIV: "/"
}


def str_expression(expression: Expression) -> str:
    left_var = str_value(expression.lhs)
    right_var = str_value(expression.rhs)
    return f"{left_var} {EXPRESSION_OPERATIONS_DISPLAY[expression.operation]} {right_var}"


def str_value(value: Value) -> str:
    return value.name if isinstance(value, Var) else str(value)


def str_assignment(assignment: Assignment) -> str:
    map_src = {
        Expression: str_expression,
        Value: str_value,
        int: str
    }
    src = map_src[type(assignment.src)](assignment.src)
    return f"{assignment.dst.name} = {src}"


def str_call(call: Call) -> str:
    args = list(map(str_value, call.args))
    return f"{call.function_name}({','.join(str(arg) for arg in args)})"


def str_jump_condition(condition: Optional[Var], branch_taken: bool) -> str:
    return f"{condition.name} != 0" if branch_taken else f"{condition.name} == 0"


STR_FUNCTIONS = {
    Assignment: str_assignment,
    Jump: lambda jump: "",
    Call: str_call
}


def str_instructions(instructions: List) -> str:
    instructions_to_display = []
    for instruction in instructions:
        instructions_to_display.append(STR_FUNCTIONS[type(instruction)](instruction))
    return "\n".join(instructions_to_display)
