# gnfcs/model_parameter_adapter.py
class ModelParameterAdapter:
    def __init__(self):
        self.parameters = {
            'inertia': 1.0,
            'drag': 0.1,
            'noise': 0.01
        }

    def adapt(self, sensor_feedback):
        if 'vibration' in sensor_feedback:
            self.parameters['inertia'] *= (1 + sensor_feedback['vibration'] * 0.01)
        return self.parameters

# --- Test for model_parameter_adapter ---
if __name__ == "__main__":
    adapter = ModelParameterAdapter()
    params = adapter.adapt({'vibration': 0.5})
    print("Adapted parameters:", params)
