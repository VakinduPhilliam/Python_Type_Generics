# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
#
# The function below takes and returns a string:
# 
# In the function greeting, the argument name is expected to be of type str and the return type str.
# Subtypes are accepted as arguments.
#

def greeting(name: str) -> str:
    return 'Hello ' + name
 