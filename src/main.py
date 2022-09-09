from typing import List

from src.logic.assembly_validtor import validate_assembly_code
from src.logic.cfg_builder import CFGBuilder
from src.ui.graph_drawer import CFGDrawer


def build_cfg(instructions: List) -> None:
    cfg_builder = CFGBuilder("CFG", instructions, validate_assembly_code)
    cfg = cfg_builder.build()
    cfg_drawer = CFGDrawer(cfg.graph)
    cfg_drawer.draw()
