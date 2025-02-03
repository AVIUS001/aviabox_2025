# gnfcs/state_estimator.py
from .sensor_fusion import SensorFusion

class StateEstimator:
    def __init__(self, dt=0.1):
        self.fusion = SensorFusion(dt=dt)

    def estimate(self, measurement):
        self.fusion.predict()
        return self.fusion.update(measurement)

# --- Test for state_estimator ---
if __name__ == "__main__":
    import numpy as np
    estimator = StateEstimator(dt=0.1)
    measurement = np.array([0, 0, 10, 0, 0, 0])
    print("Estimated state:", estimator.estimate(measurement))
