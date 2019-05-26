# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# If your generator will only yield values, annotate your generator as having a return type of either AsyncIterable[YieldType]
# or AsyncIterator[YieldType]:
 
async def infinite_stream(start: int) -> AsyncIterator[int]:

    while True:
        yield start

        start = await increment(start)
