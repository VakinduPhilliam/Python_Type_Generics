# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# class typing.Text 
# Text is an alias for str. It is provided to supply a forward compatible path for Python 2 code: in Python 2, Text is
# an alias for unicode.
# Use Text to indicate that a value must contain a unicode string in a manner that is compatible with both Python 2 and
# Python 3:
 
def add_unicode_checkmark(text: Text) -> Text:
    return text + u' \u2713'
