# gnfcs/model_parameter_adapter/test/test_model_parameter_adapter.py
import unittest
from gnfcs.model_parameter_adapter import ModelParameterAdapter

class TestModelParameterAdapter(unittest.TestCase):
    def test_adapt(self):
        adapter = ModelParameterAdapter()
        params = adapter.adapt({'vibration': 1.0})
        self.assertTrue(params['inertia'] > 1.0)

if __name__ == '__main__':
    unittest.main()
