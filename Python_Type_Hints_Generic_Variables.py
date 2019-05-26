# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# A generic type can have any number of type variables, and type variables may be constrained:
 
from typing import TypeVar, Generic

# ...

T = TypeVar('T')
S = TypeVar('S', int, str)

class StrangePair(Generic[T, S]):

#    ...
