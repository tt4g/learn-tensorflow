from numbers import Number
from typing import Iterable, TypeVar


_T = TypeVar("_T", bound=Number)


def mean(x: Iterable[_T]) -> _T:
    return sum(x) / len(x)
