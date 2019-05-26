# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# The Generic base class uses a metaclass that defines __getitem__() so that LoggedVar[t] is valid as a type:
 
from typing import Iterable

def zero_all_vars(vars: Iterable[LoggedVar[int]]) -> None:

    for var in vars:
        var.set(0)
