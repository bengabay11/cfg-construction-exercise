from typing import List

from src.logic.assembly_validtor import validate_assembly_code
from src.logic.cfg_builder import CFGBuilder
from src.ui.graph_draw import draw_graph


def build_cfg(instructions: List) -> None:
    validate_assembly_code(instructions)
    cfg_builder = CFGBuilder("CFG", instructions)
    cfg = cfg_builder.build()
    draw_graph(cfg.graph)
