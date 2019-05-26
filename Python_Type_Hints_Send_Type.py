# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# Note that unlike many other generics in the typing module, the SendType of Generator behaves contravariantly, not
# covariantly or invariantly.
# 
# If your generator will only yield values, set the SendType and ReturnType to None:
# 

def infinite_stream(start: int) -> Generator[int, None, None]:

    while True:
        yield start

        start += 1
