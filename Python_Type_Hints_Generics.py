# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# Generics
# Since type information about objects kept in containers cannot be statically inferred in a generic way, abstract base
# classes have been extended to support subscription to denote expected types for container elements.
 
from typing import Mapping, Sequence

def notify_by_email(employees: Sequence[Employee],
                    overrides: Mapping[str, str]) -> None: 

# ...
