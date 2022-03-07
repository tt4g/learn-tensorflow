import numpy as np

from .variance import variance


def test_variance():
    nums = [19, 862, 69]
    assert variance(nums) == np.var(nums)
