from typing import List

from src.assembly_validtor import validate_assembly_code
from src.cfg_builder import create_cfg
from src.ui.graph_draw import draw_graph


def build_cfg(instructions: List) -> None:
    validate_assembly_code(instructions)
    graph = create_cfg(instructions)
    draw_graph(graph)
