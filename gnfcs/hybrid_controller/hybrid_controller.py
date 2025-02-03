# gnfcs/hybrid_controller.py
import numpy as np

class HybridController:
    def __init__(self, pid_params, policy):
        self.pid_params = pid_params  # dictionary: {'kp':..., 'ki':..., 'kd':...}
        self.policy = policy
        self.integral_error = 0.0
        self.previous_error = 0.0

    def pid_control(self, setpoint, measurement, dt):
        error = setpoint - measurement
        self.integral_error += error * dt
        derivative = (error - self.previous_error) / dt if dt > 0 else 0.0
        self.previous_error = error
        return (self.pid_params['kp'] * error +
                self.pid_params['ki'] * self.integral_error +
                self.pid_params['kd'] * derivative)

    def compute_control(self, state, setpoint, dt):
        # Assume state[2] is altitude.
        altitude_control = self.pid_control(setpoint, state[2], dt)
        policy_output = self.policy.model.predict(np.expand_dims(state, axis=0))[0]
        combined_control = policy_output.copy()
        combined_control[0] += altitude_control
        return combined_control

# --- Test for hybrid_controller ---
if __name__ == "__main__":
    from gnfcs.neural_network_policy import NeuralNetworkPolicy
    pid_params = {'kp': 1.0, 'ki': 0.1, 'kd': 0.05}
    nn_policy = NeuralNetworkPolicy(state_dim=6, action_dim=76)
    controller = HybridController(pid_params, nn_policy)
    state = [0, 0, 10, 0, 0, 0]
    control = controller.compute_control(state, setpoint=15, dt=0.1)
    print("Control command:", control)
