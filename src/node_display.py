from src.cfg_construction import Expression, Operation, Value, Var, Assignment, Jump, Call

EXPRESSION_OPERATIONS_DISPLAY = {
    Operation.MUL: "*",
    Operation.SUB: "-",
    Operation.ADD: "+",
    Operation.DIV: "/"
}


def display_expression(expression: Expression):
    left_var = display_value(expression.lhs)
    right_var = display_value(expression.rhs)
    return f"{left_var} {EXPRESSION_OPERATIONS_DISPLAY[expression.operation]} {right_var}"


def display_value(value: Value):
    return value.name if isinstance(value, Var) else str(value)


def display_assignment(assignment: Assignment):
    map_src = {
        Expression: lambda src: display_expression(src),
        Value: lambda src: display_value(src),
        int: lambda src: str(src)
    }
    src = map_src[type(assignment.src)](assignment.src)
    return f"{assignment.dst.name} = {src}"


def display_call(call: Call):
    args = list(map(display_value, call.args))
    return f"{call.function_name}({','.join(str(arg) for arg in args)})"


def display_jump_branch_taken(jump: Jump):
    return f"{jump.condition.name} != 0"


def instructions_node_display(instructions):
    instructions_to_display = []
    for instruction in instructions:
        instructions_to_display.append(display_instruction_functions[type(instruction)](instruction))
    return "\n".join(instructions_to_display)


display_instruction_functions = {
    Assignment: lambda assignment: display_assignment(assignment),
    Jump: lambda jump: "",
    Call: lambda call: display_call(call),
}
