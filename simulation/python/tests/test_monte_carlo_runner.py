#!/usr/bin/env python3
import unittest
import numpy as np
from simulation.python.monte_carlo_runner import monte_carlo_simulation

class TestMonteCarloRunner(unittest.TestCase):
    def test_simulation(self):
        errors = monte_carlo_simulation(num_trials=100)
        self.assertEqual(len(errors), 100)
        self.assertTrue(np.all(errors >= 0))

if __name__ == '__main__':
    unittest.main()
