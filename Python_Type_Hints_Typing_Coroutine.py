# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# class typing.Coroutine(Awaitable[V_co], Generic[T_co T_contra, V_co]). 
# A generic version of collections.abc.Coroutine. The variance and order of type variables correspond to those of Generator,
# for example:
 
from typing import List, Coroutine

c = None # type: Coroutine[List[str], str, int]

# ...

x = c.send('hi') # type: List[str]

async def bar() -> None:
    x = await c # type: int
