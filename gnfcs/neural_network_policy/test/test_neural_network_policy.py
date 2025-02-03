# gnfcs/neural_network_policy/test/test_neural_network_policy.py
import unittest
import numpy as np
from gnfcs.neural_network_policy import NeuralNetworkPolicy

class TestNeuralNetworkPolicy(unittest.TestCase):
    def test_policy_output_shape(self):
        policy = NeuralNetworkPolicy(state_dim=6, action_dim=76)
        state = np.random.rand(1, 6)
        output = policy.predict(state)
        self.assertEqual(output.shape[1], 76)

if __name__ == '__main__':
    unittest.main()
