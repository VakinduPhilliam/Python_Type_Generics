# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# class typing.Type(Generic[CT_co]). 
# A variable annotated with C may accept a value of type C. In contrast, a variable annotated with Type[C] may accept
# values that are classes themselves – specifically, it will accept the class object of C.
#
# For example:
# 

a = 3         # Has type 'int'
b = int       # Has type 'Type[int]'
c = type(a)   # Also has type 'Type[int]'
 
#
# Note that Type[C] is covariant:
# 

class User: ...
class BasicUser(User): ...

class ProUser(User): ...
class TeamUser(User): ...

# Accepts User, BasicUser, ProUser, TeamUser, ...

def make_new_user(user_class: Type[User]) -> User:

    # ...

    return user_class()
