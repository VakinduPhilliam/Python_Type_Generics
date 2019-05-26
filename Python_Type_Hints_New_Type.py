# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# NewType
# Use the NewType() helper function to create distinct types:
 
from typing import NewType

UserId = NewType('UserId', int)
some_id = UserId(524313)
