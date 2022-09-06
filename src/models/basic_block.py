from typing import List
from dataclasses import dataclass


@dataclass
class BasicBlock(object):
    index: int
    instructions: List[any]
