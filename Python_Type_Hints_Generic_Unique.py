# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# Each type variable argument to Generic must be distinct.
#
# This is thus invalid:
# 

from typing import TypeVar, Generic

# ...

T = TypeVar('T')

class Pair(Generic[T, T]):   # INVALID

#    ...
