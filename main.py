# gnfcs/main.py
import time
import numpy as np
from gnfcs.sensor_fusion import SensorFusion
from gnfcs.state_estimator import StateEstimator
from gnfcs.rl_agent import RLAgent
from gnfcs.pinn import PINN
from gnfcs.neural_network_policy import NeuralNetworkPolicy
from gnfcs.loss_function import LossFunction
from gnfcs.data_loader import DataLoader
from gnfcs.trainer import Trainer
from gnfcs.evaluator import Evaluator
from gnfcs.hybrid_controller import HybridController
from gnfcs.dual_quaternion_kinematics import DualQuaternion
from gnfcs.disturbance_estimator import DisturbanceEstimator
from gnfcs.model_parameter_adapter import ModelParameterAdapter
from gnfcs.predictive_path_controller import PredictivePathController

def main():
    dt = 0.1

    # Sensor fusion and state estimation.
    state_estimator = StateEstimator(dt=dt)
    measurement = np.array([0, 0, 10, 0, 0, 0])
    state = state_estimator.estimate(measurement)
    print("Estimated State:", state)

    # RL Agent and NN Policy.
    rl_agent = RLAgent(state_dim=6, action_dim=76)
    nn_policy = NeuralNetworkPolicy(state_dim=6, action_dim=76)

    # Hybrid Controller.
    pid_params = {'kp': 1.0, 'ki': 0.1, 'kd': 0.05}
    hybrid_controller = HybridController(pid_params, nn_policy)

    # Disturbance Estimator.
    disturbance_estimator = DisturbanceEstimator()
    sensor_data = {'acceleration': np.array([0.1, 0.0, -0.05])}
    disturbance = disturbance_estimator.estimate(sensor_data)
    print("Estimated Disturbance:", disturbance)

    # Model Parameter Adapter.
    adapter = ModelParameterAdapter()
    adapted_params = adapter.adapt({'vibration': 0.2})
    print("Adapted Parameters:", adapted_params)

    # Predictive Path Controller.
    predictive_controller = PredictivePathController(horizon=10, dt=dt)
    current_state = state
    target_state = np.array([0, 0, 15, 0, 0, 0])
    control = predictive_controller.compute_control(current_state, target_state)
    path = predictive_controller.predict_path(current_state, [control]*10)
    print("Predicted Path:\n", path)

    # Simulation loop.
    for step in range(10):
        sensor_measurement = measurement + np.random.normal(0, 0.1, 6)
        current_state = state_estimator.estimate(sensor_measurement)
        control_command = hybrid_controller.compute_control(current_state, setpoint=15, dt=dt)
        print(f"Step {step}: Control Command: {control_command}")

        action = rl_agent.select_action(current_state)
        next_state = current_state + np.random.normal(0, 0.1, 6)  # dummy update
        rl_agent.update(current_state, action, reward=1.0, next_state=next_state, done=False)
        time.sleep(dt)

    # Evaluate policy.
    evaluator = Evaluator(nn_policy, LossFunction)
    X_test = np.random.rand(100, 6)
    y_test = np.random.rand(100, 76)
    evaluator.evaluate(X_test, y_test)
    evaluator.plot_predictions(X_test, y_test)

if __name__ == "__main__":
    main()
