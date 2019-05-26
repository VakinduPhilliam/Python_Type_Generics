# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# Using a generic class without specifying type parameters assumes Any for each position.
# In the following example, MyIterable is not generic but implicitly inherits from Iterable[Any]:
 
from typing import Iterable

class MyIterable(Iterable): # Same as Iterable[Any]
