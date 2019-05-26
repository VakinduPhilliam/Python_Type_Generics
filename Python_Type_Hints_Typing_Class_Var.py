# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# typing.ClassVar 
# Special type construct to mark class variables.
# A variable annotation wrapped in ClassVar indicates that a given attribute is intended to be used as a class variable
# and should not be set on instances of that class.
#
# Usage:
# 

class Starship:
    stats: ClassVar[Dict[str, int]] = {} # class variable

    damage: int = 10                     # instance variable
