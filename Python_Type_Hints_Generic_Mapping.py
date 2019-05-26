# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# A generic type is typically declared by inheriting from an instantiation of this class with one or more type variables.
# For example, a generic mapping type might be defined as:
 
class Mapping(Generic[KT, VT]):

    def __getitem__(self, key: KT) -> VT:

#        ...

        # Etc.
 
# This class can then be used as follows:
 
X = TypeVar('X')
Y = TypeVar('Y')

def lookup_name(mapping: Mapping[X, Y], key: X, default: Y) -> Y:

    try:
        return mapping[key]

    except KeyError:
        return default
