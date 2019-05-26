# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# typing.AnyStr 
# AnyStr is a type variable defined as AnyStr = TypeVar('AnyStr', str, bytes).
# It is meant to be used for functions that may accept any kind of string without allowing different kinds of strings to mix.
#
# For example:
# 

def concat(a: AnyStr, b: AnyStr) -> AnyStr:
    return a + b

concat(u"foo", u"bar")  # Ok, output has type 'unicode'
concat(b"foo", b"bar")  # Ok, output has type 'bytes'

concat(u"foo", b"bar")  # Error, cannot mix unicode and bytes
