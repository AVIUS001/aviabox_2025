# gnfcs/dual_quaternion_kinematics.py
import numpy as np

class DualQuaternion:
    def __init__(self, real, dual):
        self.real = np.array(real)   # [w, x, y, z]
        self.dual = np.array(dual)

    def __mul__(self, other):
        r1, d1 = self.real, self.dual
        r2, d2 = other.real, other.dual
        real = self.quaternion_multiply(r1, r2)
        dual = self.quaternion_multiply(r1, d2) + self.quaternion_multiply(d1, r2)
        return DualQuaternion(real, dual)

    @staticmethod
    def quaternion_multiply(q1, q2):
        w1, x1, y1, z1 = q1
        w2, x2, y2, z2 = q2
        w = w1*w2 - x1*x2 - y1*y2 - z1*z2
        x = w1*x2 + x1*w2 + y1*z2 - z1*y2
        y = w1*y2 - x1*z2 + y1*w2 + z1*x2
        z = w1*z2 + x1*y2 - y1*x2 + z1*w2
        return np.array([w, x, y, z])

    def conjugate(self):
        return DualQuaternion(self.real * np.array([1, -1, -1, -1]),
                              self.dual * np.array([1, -1, -1, -1]))

    def normalize(self):
        norm = np.linalg.norm(self.real)
        self.real /= norm
        self.dual /= norm
        return self

    def to_transformation_matrix(self):
        q = self.real
        w, x, y, z = q
        R = np.array([
            [1 - 2*(y*y+z*z), 2*(x*y - z*w), 2*(x*z + y*w)],
            [2*(x*y + z*w), 1 - 2*(x*x+z*z), 2*(y*z - x*w)],
            [2*(x*z - y*w), 2*(y*z + x*w), 1 - 2*(x*x+y*y)]
        ])
        t = 2 * self.quaternion_multiply(self.dual, self.quaternion_conjugate(self.real))[1:]
        T = np.eye(4)
        T[:3, :3] = R
        T[:3, 3] = t
        return T

    @staticmethod
    def quaternion_conjugate(q):
        return np.array([q[0], -q[1], -q[2], -q[3]])

# --- Test for dual_quaternion_kinematics ---
if __name__ == "__main__":
    dq = DualQuaternion([1, 0, 0, 0], [0, 1, 0, 0]).normalize()
    print("Transformation matrix:\n", dq.to_transformation_matrix())
