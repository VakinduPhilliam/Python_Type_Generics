# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# class typing.NamedTuple 
# Typed version of namedtuple.
# 
# Usage:
# 

class Employee(NamedTuple):

    name: str
    id: int

# 
# This is equivalent to:
# 

Employee = collections.namedtuple('Employee', ['name', 'id'])
 
#
# To give a field a default value, you can assign to it in the class body:
# 

class Employee(NamedTuple):

    name: str
    id: int = 3

employee = Employee('Guido')

assert employee.id == 3
