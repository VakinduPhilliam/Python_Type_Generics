# Python Type Hints
# typing — Support for type hints
# This module supports type hints as specified by PEP 484 and PEP 526.
# The most fundamental support consists of the types 'Any', 'Union', 'Tuple', 'Callable', 'TypeVar', and 'Generic'.
# User-defined generic types.
# A user-defined class can be defined as a generic class.
 
from typing import TypeVar, Generic
from logging import Logger

T = TypeVar('T')

class LoggedVar(Generic[T]):

    def __init__(self, value: T, name: str, logger: Logger) -> None:

        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:

        self.log('Set ' + repr(self.value))
        self.value = new

    def get(self) -> T:

        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:

        self.logger.info('%s: %s', self.name, message)
