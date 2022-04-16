import numpy as np

from learn_tensorflow.reinvent.deviation import deviation


def test_deviation():
    assert np.allclose(
        deviation([19, 862, 69]), [-297.666, 545.333, -247.666],
        atol=1e-08)
