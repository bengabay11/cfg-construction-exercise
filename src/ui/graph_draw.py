import networkx as nx
from matplotlib import pyplot as plt

from src.config import NODE_SIZE, NODE_SHAPE, FILE_PATH
from src.ui.str_assembly import str_instructions, str_jump_condition


def draw_nodes(graph: nx.DiGraph, pos: dict) -> None:
    node_labels = nx.get_node_attributes(graph, "instructions")
    node_labels = {node: str_instructions(instructions) for node, instructions in node_labels.items()}
    nx.draw_networkx_nodes(graph, pos, node_shape=NODE_SHAPE, node_size=NODE_SIZE)
    nx.draw_networkx_labels(graph, pos, labels=node_labels, font_size=6)


def draw_branch_not_taken_edges(graph: nx.DiGraph, pos: dict):
    graph_edges = list(graph.edges(data=True))
    unconditional_edges = []
    conditional_edge_labels = {}
    for source, target, data in graph_edges:
        if data["condition"] is None:
            unconditional_edges.append((source, target))
        else:
            conditional_edge_labels[(source, target)] = str_jump_condition(**data)
    nx.draw_networkx_edges(
        graph,
        pos,
        edgelist=unconditional_edges,
        arrows=True,
        node_size=NODE_SIZE,
        node_shape=NODE_SHAPE
    )
    nx.draw_networkx_edges(
        graph,
        pos,
        edgelist=conditional_edge_labels.keys(),
        arrows=True,
        node_size=NODE_SIZE,
        node_shape=NODE_SHAPE
    )
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=conditional_edge_labels)


def draw_edges(graph: nx.DiGraph, pos: dict) -> None:
    draw_branch_not_taken_edges(graph, pos)
    # graph_edges = list(graph.edges(data=True))
    # branch_taken_edges = [edge for edge in graph_edges if edge[2]["branch_taken"]]
    # regular_edges = [edge for edge in graph_edges if edge[2]["branch_taken"] is None]
    # edge_jump_labels = nx.get_edge_attributes(graph, "jump")
    # edge_jump_labels = {edge: str_jump_branch_taken(jump) for edge, jump in edge_jump_labels.items()}
    #
    # edge_no_jump_labels = nx.get_edge_attributes(graph, "no_jump")
    # edge_no_jump_labels = {edge: str_jump_branch_not_taken(jump) for edge, jump in edge_no_jump_labels.items()}
    #
    # jump_edges_options = {
    #     "edgelist": edge_jump_labels.keys(),
    #     "arrows": True,
    #     "node_size": NODE_SIZE,
    #     "node_shape": NODE_SHAPE,
    #     "edge_color": "b",
    #     "connectionstyle": "arc3,rad=0.6"
    # }
    # nx.draw_networkx_edges(graph, pos, **jump_edges_options)
    # nx.draw_networkx_edges(graph, pos, edgelist=graph.edges - edge_jump_labels.keys(), arrows=True, node_size=NODE_SIZE, node_shape=NODE_SHAPE)
    #
    # nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_jump_labels)
    # nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_no_jump_labels)


def draw_graph(graph: nx.DiGraph) -> None:
    # pos = nx.spring_layout(graph)
    pos = nx.shell_layout(graph)
    # pos = nx.multipartite_layout(graph, subset_key="level", align="horizontal")
    plt.figure(figsize=(20, 20))
    plt.axis('equal')
    draw_nodes(graph, pos)
    draw_edges(graph, pos)
    plt.savefig(FILE_PATH)
    plt.show()
