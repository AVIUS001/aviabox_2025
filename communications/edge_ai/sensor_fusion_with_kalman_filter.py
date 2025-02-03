# communications/sensor_fusion_with_kalman_filter.py
import numpy as np

def kalman_filter(measurements, dt=0.1):
    # Simple 1D Kalman filter stub.
    x = 0
    P = 1
    Q = 0.01
    R = 0.1
    results = []
    for z in measurements:
        # Prediction
        x_pred = x
        P_pred = P + Q
        # Update
        K = P_pred / (P_pred + R)
        x = x_pred + K * (z - x_pred)
        P = (1 - K) * P_pred
        results.append(x)
    return results

if __name__ == "__main__":
    measurements = np.random.normal(10, 0.5, 10)
    print("Kalman Filter Results:", kalman_filter(measurements))
