from numbers import Number
from typing import Iterable, TypeVar

from .deviation import deviation


_T = TypeVar("_T", bound=Number)

def variance(x: Iterable[_T]) -> Number:
    # $$\frac{1}{N} \sum_{n=1}^{n}(n - mean(N))^2$$
    # `N` is `len(x)`
    return sum([d ** 2 for d in deviation(x)]) / len(x)
