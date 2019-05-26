# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# Type aliases are useful for simplifying complex type signatures.
# For example:
#
# Note that None as a type hint is a special case and is replaced by type(None).
#
 
from typing import Dict, Tuple, List

ConnectionOptions = Dict[str, str]

Address = Tuple[str, int]
Server = Tuple[Address, ConnectionOptions]

def broadcast_message(message: str, servers: List[Server]) -> None:

#    ...

# The static type checker will treat the previous type signature as
# being exactly equivalent to this one.

def broadcast_message(
        message: str,
        servers: List[Tuple[Tuple[str, int], Dict[str, str]]]) -> None:

#    ...
