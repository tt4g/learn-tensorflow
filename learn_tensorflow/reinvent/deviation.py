from numbers import Number
from typing import Iterable, TypeVar

from .mean import mean


_T = TypeVar("_T", bound=Number)

def deviation(x: Iterable[_T]) -> Iterable[Number]:
    m = mean(x)

    return [_x - m for _x in x]
