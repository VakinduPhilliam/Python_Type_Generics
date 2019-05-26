# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# When the type of a value is object, a type checker will reject almost all operations on it, and assigning
# it to a variable (or using it as a return value) of a more specialized type is a type error.
 
def hash_a(item: object) -> int:

    # Fails; an object does not have a 'magic' method.

    item.magic()

#    ...

def hash_b(item: Any) -> int:

    # Typechecks

    item.magic()

#    ...

# Typechecks, since ints and strs are subclasses of object

hash_a(42)
hash_a("foo")

# Typechecks, since Any is compatible with all types

hash_b(42)
hash_b("foo")

