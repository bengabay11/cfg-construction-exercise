from src.cfg_construction import Assignment, Call, Jump, Var, Expression, Operation, build_cfg


def main():
    counter = Var("counter")
    output = Var("output")
    code = [
        Assignment(counter, 6),  # 1
        Assignment(output, 1),  # 2
        Call("print", [output]),  # 3
        Assignment(counter, Expression(counter, 1, Operation.SUB)),  # 4
        Jump(3, counter),  # 5
        Call("print", [output])  # 6
    ]
    build_cfg(code)


if __name__ == '__main__':
    main()
