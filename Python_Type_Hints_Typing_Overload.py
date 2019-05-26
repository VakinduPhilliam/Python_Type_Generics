# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# @typing.overload 
# The @overload decorator allows describing functions and methods that support multiple different combinations of argument types.
# A series of @overload-decorated definitions must be followed by exactly one non-@overload-decorated definition (for the same function/method).
# The @overload-decorated definitions are for the benefit of the type checker only, since they will be overwritten by the non-@overload-decorated
# definition, while the latter is used at runtime but should be ignored by a type checker. At runtime, calling a @overload-decorated function
# directly will raise NotImplementedError. An example of overload that gives a more precise type than can be expressed using a union or a type
# variable:
 
@overload
def process(response: None) -> None:

#    ...

@overload
def process(response: int) -> Tuple[int, str]:

#    ...

@overload
def process(response: bytes) -> str:

#    ...

def process(response):

#    <actual implementation>
