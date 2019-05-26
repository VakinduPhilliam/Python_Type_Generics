# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# class typing.List(list, MutableSequence[T]). 
# Generic version of list. Useful for annotating return types.
# To annotate arguments it is preferred to use abstract collection types such as Mapping, Sequence, or AbstractSet.
#
# This type may be used as follows:
# 

T = TypeVar('T', int, float)

def vec2(x: T, y: T) -> List[T]:
    return [x, y]

def keep_positives(vector: Sequence[T]) -> List[T]:
    return [item for item in vector if item > 0]
