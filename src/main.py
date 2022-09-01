from src.assembly_validtor import validate_assembly_code
from src.cfg_builder import create_cfg
from src.cfg_construction import Assignment, Call, Jump, Var, Expression, Operation
from src.graph_draw import draw_graph


def main():
    base = Var("base")
    counter = Var("counter")
    output = Var("output")
    # code = [
    #     Assignment(base, 2),  # 0
    #     Assignment(counter, 5),  # 1
    #     Assignment(output, 1),  # 2
    #     # Loop start
    #     Assignment(output, Expression(output, base, Operation.MUL)),  # 3
    #     Assignment(counter, Expression(counter, 1, Operation.SUB)),  # 4
    #     Jump(3, counter),  # 5
    #     Call("print", [output])  # 6
    # ]
    code = [
        Assignment(counter, 6),  # 0
        Assignment(output, 1),  # 1
        Jump(6, counter),  # 2
        "Hello",
        Call("insmod", [6]),  # 3
        Call("lsmod", [6]),  # 4
        Jump(9, counter),  # 5
        Call("print1", [output]),  # 6
        Call("print2", [output]),  # 7
        Call("print3", [output]),  # 8
        Call("exit", [output])  # 9
    ]
    validate_assembly_code(code)
    graph = create_cfg(code)
    draw_graph(graph)


if __name__ == '__main__':
    main()
