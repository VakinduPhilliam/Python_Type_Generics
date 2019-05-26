# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# Classes, functions, and decorators.
# The module defines the following classes, functions and decorators:
#
# class typing.TypeVar 
#
# Type variable.
#
# Usage:
# 

T = TypeVar('T')  # Can be anything
A = TypeVar('A', str, bytes)  # Must be str or bytes

# 
# Type variables exist primarily for the benefit of static type checkers.
# They serve as the parameters for generic types as well as for generic function definitions.
#
# Generic functions work as follows:
# 

def repeat(x: T, n: int) -> Sequence[T]:
    """Return a list containing n references to x."""

    return [x]*n

def longest(x: A, y: A) -> A:
    """Return the longest of two strings."""

    return x if len(x) >= len(y) else y

#
# The latter example’s signature is essentially the overloading of (str, str) -> str and (bytes, bytes) -> bytes.
#