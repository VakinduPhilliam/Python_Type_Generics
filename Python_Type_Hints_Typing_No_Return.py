# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# typing.NoReturn 
# Special type indicating that a function never returns.
#
# For example:
# 

from typing import NoReturn

def stop() -> NoReturn:

    raise RuntimeError('no way')
