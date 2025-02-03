# gnfcs/dual_quaternion_kinematics/test/test_dual_quaternion_kinematics.py
import unittest
import numpy as np
from gnfcs.dual_quaternion_kinematics import DualQuaternion

class TestDualQuaternion(unittest.TestCase):
    def test_normalize(self):
        dq = DualQuaternion([2, 0, 0, 0], [0, 2, 0, 0])
        dq.normalize()
        norm = np.linalg.norm(dq.real)
        self.assertAlmostEqual(norm, 1.0, delta=1e-5)

if __name__ == '__main__':
    unittest.main()
