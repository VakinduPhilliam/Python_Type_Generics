# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# Unlike normal generators, async generators cannot return a value, so there is no ReturnType type parameter.
# As with Generator, the SendType behaves contravariantly.
# 
# If your generator will only yield values, set the SendType to None:
# 

async def infinite_stream(start: int) -> AsyncGenerator[int, None]:

    while True:
        yield start

        start = await increment(start)
