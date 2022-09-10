from typing import List

from src.config import CFG_NAME, OUTPUT_FILE_PATH, NODE_SIZE, NODE_SHAPE, ARROWS, FIGURE_SIZE, FONT_SIZE
from src.logic.assembly_validtor import validate_assembly_code
from src.logic.cfg_builder import CFGBuilder
from src.ui.graph_drawer import CFGDrawer
from src.ui.str_assembly import str_jump_condition, str_instructions


def build_cfg(instructions: List) -> None:
    cfg_builder = CFGBuilder(CFG_NAME, instructions, validate_assembly_code)
    cfg = cfg_builder.build()
    cfg_drawer_options = {
        "node_size": NODE_SIZE,
        "node_shape": NODE_SHAPE,
        "arrows": ARROWS,
        "font_size": FONT_SIZE
    }
    cfg_drawer = CFGDrawer(cfg.graph, str_instructions, str_jump_condition, **cfg_drawer_options)
    cfg_drawer.draw(cfg_builder.cfg.name, OUTPUT_FILE_PATH, FIGURE_SIZE)
