from src.cfg_builder import create_cfg
from src.cfg_construction import Assignment, Call, Jump, Var, Expression, Operation
from src.graph_draw import draw_graph


def main():
    counter = Var("counter")
    output = Var("output")
    true = Var("start again")
    code = [
        Assignment(counter, 6),  # 1
        Assignment(output, 1),  # 2
        Call("print", [output]),  # 3
        Assignment(counter, Expression(counter, 1, Operation.SUB)),  # 4
        Jump(3, counter),  # 5
        Call("print", [output]),  # 6
        Jump(1, true),
        Call("exit", [0])
    ]
    graph = create_cfg(code)
    draw_graph(graph)


if __name__ == '__main__':
    main()
