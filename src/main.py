import networkx as nx
import matplotlib.pyplot as plt

from src.cfg_construction import Assignment, Var, Expression, Operation, Jump, Call, Value
from src.graph_update import add_assignment, add_jump, add_call


graph_update_functions = {
    Assignment: lambda graph, current_node, assignment: add_assignment(graph, current_node, assignment),
    Jump: lambda graph, current_node, jump: add_jump(graph, current_node, jump),
    Call: lambda graph, current_node, call: add_call(graph, current_node, call),
}


def build_cfg(instructions):
    graph = nx.Graph()
    pos = nx.spring_layout(graph)
    current_node = (1, "Start")
    graph.add_node(current_node)
    for line, instruction in enumerate(instructions, start=1):
        current_node = graph_update_functions[type(instruction)](graph, current_node, instruction)
    nx.draw(graph, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels={}, font_color="red")
    plt.savefig("../path.png")


base = Var("base")
counter = Var("counter")
output = Var("output")
code = [
    Assignment(base, 2),  # 0
    Assignment(counter, 5),  # 1
    Assignment(output, 1),  # 2
    # Loop start
    Assignment(output, Expression(output, base, Operation.MUL)),  # 3
    Assignment(counter, Expression(counter, 1, Operation.SUB)),  # 4
    Jump(3, counter),  # 5
    Call("print", [output])  # 6
]
build_cfg(code)
