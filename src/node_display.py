from src.cfg_construction import Expression, Operation, Value, Var, Assignment, Jump, Call


def display_expression(expression: Expression):
    operations_display = {
        Operation.MUL: "*",
        Operation.SUB: "-",
        Operation.ADD: "+",
        Operation.DIV: "/"
    }
    left_var = display_value(expression.lhs)
    right_var = display_value(expression.rhs)
    return f"{left_var} {operations_display[expression.operation]} {right_var}"


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
