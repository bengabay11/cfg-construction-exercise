"""
In this exercise, we will convert a simple assembly language into a CFG (control flow graph).
CFGs (https://en.wikipedia.org/wiki/Control-flow_graph) are directed graphs (https://en.wikipedia.org/wiki/Directed_graph), 
where the nodes are usually instructions or basic blocks (https://en.wikipedia.org/wiki/Basic_block) and the edges represent 
possible flows between the nodes.
Usually, there are two kinds of edges - plain ones (meaning unconditional flow from one node to another) or conditional 
flows (meaning the flow will be decided from two options depending on some condition).

CFGs are useful for many kinds of analyses (liveness/dead code, stack recovery, pointer analysis,
folding, slicing, etc.)

Enough talk, let's get down to business!

Here's the definition for our assembly language:
"""
import enum
from dataclasses import dataclass
from typing import Optional, Union, List


class Operation(enum.Enum):
    ADD = enum.auto()
    SUB = enum.auto()
    MUL = enum.auto()
    DIV = enum.auto()


@dataclass
class Var:
    name: str


Value = Union[Var, int]  # Variable (e.g. "foo", "x") or int for a const


@dataclass
class Expression:
    lhs: Value
    rhs: Value
    operation: Operation


@dataclass
class Assignment:
    dst: Var
    src: Union[Value, Expression]


@dataclass
class Jump:
    target: int
    condition: Optional[Var]  # If a condition is provided, the branch is taken if the var is not zero


@dataclass
class Call:
    function_name: str
    args: List[Value]


"""
Now let's write some code - e.g. exponentiation
"""

base = Var("base")
counter = Var("counter")
output = Var("output")

code = [
    Assignment(base, 2),  # 0
    Assignment(counter, 5),  # 1
    Assignment(output, 1),  # 2
    # Loop start
    Assignment(output, Expression(output, base, Operation.MUL)),  # 3
    Assignment(counter, Expression(counter, 1, Operation.SUB)),  # 4
    Jump(3, counter),  # 5
    Call("print", [output])  # 6
]


"""
Now, we want to build a control flow graph from this function.

Our nodes will be instructions, and our edges will contain conditions. For example, the code:

    a = 1
    jump(AFTER, a)
    b = 2
    jump(END)
    AFTER:
    b = 3
    END:
    print(b)
    
Would be represented as:

  a = 1
 ||    \\
 || !a  \\  a
 ||      \\
 b = 2    b = 3
 ||       //
 ||      //
 print(b)

You can use any library for basic graph functions - e.g. networkx. Don't forget to write tests!
"""
