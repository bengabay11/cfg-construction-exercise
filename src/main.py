from typing import List

from src.logic.assembly_validtor import AssemblyValidator
from src.logic.cfg_builder import CFGBuilder
from src.ui.graph_drawer import CFGDrawer


def build_cfg(instructions: List) -> None:
    assembly_validator = AssemblyValidator(instructions)
    cfg_builder = CFGBuilder("CFG", instructions, assembly_validator)
    cfg = cfg_builder.build()
    cfg_drawer = CFGDrawer(cfg.graph)
    cfg_drawer.draw()
