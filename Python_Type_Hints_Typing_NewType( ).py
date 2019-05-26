# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# typing.NewType(typ) 
# A helper function to indicate a distinct types to a typechecker.
# At runtime it returns a function that returns its argument.
#
# Usage:
# 

UserId = NewType('UserId', int)
first_user = UserId(1)
