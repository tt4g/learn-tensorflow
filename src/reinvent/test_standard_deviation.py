import numpy as np

from .standard_deviation import standard_deviation


def test_standard_deviation():
    assert np.isclose(
        standard_deviation([9324, 4, 33001]), 13889.50338285,
        atol=1e-08)

    floating_numbers = [-983255, -357885553, -74002]
    assert np.isclose(
        standard_deviation(floating_numbers),
        np.std(floating_numbers),
        atol=1e-08)
