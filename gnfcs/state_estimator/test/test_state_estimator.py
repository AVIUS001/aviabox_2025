# gnfcs/state_estimator/test/test_state_estimator.py
import unittest
import numpy as np
from gnfcs.state_estimator import StateEstimator

class TestStateEstimator(unittest.TestCase):
    def test_estimate(self):
        estimator = StateEstimator(dt=0.1)
        measurement = np.array([0, 0, 10, 0, 0, 0])
        state = estimator.estimate(measurement)
        self.assertEqual(len(state), 6)
        self.assertAlmostEqual(state[2], 10, delta=1)

if __name__ == '__main__':
    unittest.main()
