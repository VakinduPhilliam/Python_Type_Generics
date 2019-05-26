# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# Type aliases.
# A type alias is defined by assigning the type to the alias.
# In this example, Vector and List[float] will be treated as interchangeable synonyms:
 
from typing import List

Vector = List[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# typechecks; a list of floats qualifies as a Vector.

new_vector = scale(2.0, [1.0, -4.2, 5.4])
