# gnfcs/hybrid_controller/test/test_hybrid_controller.py
import unittest
from gnfcs.hybrid_controller import HybridController
from gnfcs.neural_network_policy import NeuralNetworkPolicy

class TestHybridController(unittest.TestCase):
    def test_pid_control(self):
        pid_params = {'kp': 1.0, 'ki': 0.0, 'kd': 0.0}
        nn_policy = NeuralNetworkPolicy(state_dim=6, action_dim=76)
        controller = HybridController(pid_params, nn_policy)
        # Test PID: with setpoint 15 and measurement 10, error=5 => output should be 5 (if only kp used)
        control_value = controller.pid_control(15, 10, 0.1)
        self.assertAlmostEqual(control_value, 5.0, delta=0.1)

if __name__ == '__main__':
    unittest.main()
