import math
from numbers import Number
from typing import Iterable, TypeVar

from .variance import variance


_T = TypeVar("_T", bound=Number)


def standard_deviation(x: Iterable[_T]) -> float:
    return math.sqrt(variance(x))
