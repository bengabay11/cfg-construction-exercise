from typing import Optional
from dataclasses import dataclass

from src.cfg_construction import Var


@dataclass
class Link(object):
    source: int
    target: int
    condition: Optional[Var] = None
    branch_taken: bool = None
