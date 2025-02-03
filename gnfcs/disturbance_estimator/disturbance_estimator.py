# gnfcs/disturbance_estimator.py
import numpy as np

class DisturbanceEstimator:
    def __init__(self):
        self.estimated_disturbance = np.zeros(3)

    def estimate(self, sensor_data):
        # Assume sensor_data contains a key 'acceleration'
        acc = sensor_data.get('acceleration', np.zeros(3))
        self.estimated_disturbance = acc  # Stub: in reality, process the sensor data.
        return self.estimated_disturbance

# --- Test for disturbance_estimator ---
if __name__ == "__main__":
    estimator = DisturbanceEstimator()
    data = {'acceleration': np.array([0.1, 0.0, -0.05])}
    print("Estimated disturbance:", estimator.estimate(data))
