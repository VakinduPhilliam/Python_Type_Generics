# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# All functions without a return type or parameter types will implicitly default to using Any:
 
def legacy_parser(text):

#     ...

    return data

# A static type checker will treat the above
# as having the same signature as:

def legacy_parser(text: Any) -> Any:

#    ...

    return data
