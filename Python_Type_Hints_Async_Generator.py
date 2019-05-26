# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# class typing.AsyncGenerator(AsyncIterator[T_co], Generic[T_co, T_contra]) 
# An async generator can be annotated by the generic type AsyncGenerator[YieldType, SendType].
#
# For example:
# 

async def echo_round() -> AsyncGenerator[int, float]:
    sent = yield 0

    while sent >= 0.0:
        rounded = await round(sent)

        sent = yield rounded
