# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# class typing.Generator(Iterator[T_co], Generic[T_co, T_contra, V_co]) 
# A generator can be annotated by the generic type Generator[YieldType, SendType, ReturnType].
#
# For example:
# 

def echo_round() -> Generator[int, float, str]:
    sent = yield 0

    while sent >= 0:
        sent = yield round(sent)

    return 'Done'
