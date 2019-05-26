# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# typing.Optional 
# Optional type.
# Optional[X] is equivalent to Union[X, None].
# Note that this is not the same concept as an optional argument, which is one that has a default.
# An optional argument with a default does not require the Optional qualifier on its type annotation just because it is optional.
#
# For example:
# 

def foo(arg: int = 0) -> None:

#    ...

# 
# On the other hand, if an explicit value of None is allowed, the use of Optional is appropriate, whether the argument is optional
# or not.
#
# For example:
# 

def foo(arg: Optional[int] = None) -> None:

#    ...
