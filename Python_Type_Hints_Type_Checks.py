# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# The static type checker will treat the new type as if it were a subclass of the original type.
# This is useful in helping catch logical errors:
 
def get_user_name(user_id: UserId) -> str:

#    ...

# typechecks

user_a = get_user_name(UserId(42351))

# does not typecheck; an int is not a UserId

user_b = get_user_name(-1)
 
# You may still perform all int operations on a variable of type UserId, but the result will always be of type int. 
# This lets you pass in a UserId wherever an int might be expected, but will prevent you from accidentally creating a
# UserId in an invalid way:
 
# 'output' is of type 'int', not 'UserId'

output = UserId(23413) + UserId(54341)
