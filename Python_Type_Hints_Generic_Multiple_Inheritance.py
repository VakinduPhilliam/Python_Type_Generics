# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# You can use multiple inheritance with Generic:
 
from typing import TypeVar, Generic, Sized

T = TypeVar('T')

class LinkedList(Sized, Generic[T]):

#    ...
