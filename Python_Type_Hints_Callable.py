# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# Callable
# Frameworks expecting callback functions of specific signatures might be type hinted using Callable[[Arg1Type, Arg2Type],
# ReturnType].
# 
# For example:
# 

from typing import Callable

def feeder(get_next_item: Callable[[], str]) -> None:

    # Body

def async_query(on_success: Callable[[int], None],
                on_error: Callable[[int, Exception], None]) -> None:

    # Body
