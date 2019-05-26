# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# It is not possible to create a subtype of Derived since it is an identity function at runtime, not an actual type:
 
from typing import NewType

UserId = NewType('UserId', int)

# Fails at runtime and does not typecheck

class AdminUserId(UserId): pass
