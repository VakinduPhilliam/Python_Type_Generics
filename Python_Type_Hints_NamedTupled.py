# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# Fields with a default value must come after any fields without a default.
# The resulting class has two extra attributes: _field_types, giving a dict mapping field names to types, and _field_defaults,
# a dict mapping field names to default values. (The field names are in the _fields attribute, which is part of the namedtuple
# API.)
# 
# NamedTuple subclasses can also have docstrings and methods:
# 

class Employee(NamedTuple):
    """Represents an employee."""

    name: str
    id: int = 3

    def __repr__(self) -> str:
        return f'<Employee {self.name}, id={self.id}>'
 
#
# Backward-compatible usage:
# 

Employee = NamedTuple('Employee', [('name', str), ('id', int)])
