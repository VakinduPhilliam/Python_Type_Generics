# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# class typing.Dict(dict, MutableMapping[KT, VT]) 
# A generic version of dict.
#
# The usage of this type is as follows:
#
 
def get_position_in_index(word_list: Dict[str, int], word: str) -> int:
    return word_list[word]
