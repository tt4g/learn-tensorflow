import numpy as np

from learn_tensorflow.reinvent.mean import mean


def test_mean():
    assert mean([1, 2, 3]) == 2

    float_numbers = [48.3, 96634.72, -29.4]
    assert mean([48.3, 96634.72, -29.4]) == np.mean(float_numbers)
