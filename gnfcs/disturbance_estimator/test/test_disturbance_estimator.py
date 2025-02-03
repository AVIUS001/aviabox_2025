# gnfcs/disturbance_estimator/test/test_disturbance_estimator.py
import unittest
import numpy as np
from gnfcs.disturbance_estimator import DisturbanceEstimator

class TestDisturbanceEstimator(unittest.TestCase):
    def test_estimate(self):
        estimator = DisturbanceEstimator()
        data = {'acceleration': np.array([0.2, 0.1, 0.0])}
        disturbance = estimator.estimate(data)
        np.testing.assert_array_almost_equal(disturbance, [0.2, 0.1, 0.0])

if __name__ == '__main__':
    unittest.main()
