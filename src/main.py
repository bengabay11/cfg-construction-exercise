from typing import List

from src.config import CFG_NAME, OUTPUT_FILE_PATH, NODE_SIZE, NODE_SHAPE, ARROWS, FIGURE_SIZE
from src.logic.assembly_validtor import validate_assembly_code
from src.logic.cfg_builder import CFGBuilder
from src.ui.graph_drawer import CFGDrawer


def build_cfg(instructions: List) -> None:
    cfg_builder = CFGBuilder(CFG_NAME, instructions, validate_assembly_code)
    cfg = cfg_builder.build()
    cfg_drawer = CFGDrawer(cfg.graph, NODE_SIZE, NODE_SHAPE, ARROWS, FIGURE_SIZE)
    cfg_drawer.draw(OUTPUT_FILE_PATH)
