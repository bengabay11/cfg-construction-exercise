import networkx as nx

from src.models.basic_block import BasicBlock
from src.models.link import Link


class CFG(object):
    def __init__(self, name: str, basic_blocks=None, links=None):
        if links is None:
            links = []
        if basic_blocks is None:
            basic_blocks = []
        self.name = name
        self.graph = nx.DiGraph()
        self.basic_blocks = basic_blocks
        self.links = links

    def add_basic_block(self, basic_block: BasicBlock):
        self.basic_blocks.append(basic_block)
        self.graph.add_node(basic_block.index, instructions=basic_block.instructions, level=basic_block.index)

    def add_link(self, link: Link):
        self.links.append(link)
        self.graph.add_edge(link.source, link.target, condition=link.condition, branch_taken=link.branch_taken)
