# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# When inheriting from generic classes, some type variables could be fixed:
 
from typing import TypeVar, Mapping

T = TypeVar('T')

class MyDict(Mapping[str, T]):

#    ...
