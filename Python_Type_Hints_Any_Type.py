# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# The 'Any' type
# A special kind of type is Any. A static type checker will treat every type as being compatible with Any and Any as
# being compatible with every type.
# This means that it is possible to perform any operation or method call on a value of type on Any and assign it to any
# variable:
 
from typing import Any

a = None    # type: Any
a = []      # OK
a = 2       # OK

s = ''      # type: str
s = a       # OK

def foo(item: Any) -> int:

    # Typechecks; 'item' could be any type,
    # and that type might have a 'bar' method

    item.bar()

#    ...
