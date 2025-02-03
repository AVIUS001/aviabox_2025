# communications/tests/test_edge_ai.py
import unittest
from communications.edge_ai.edge_ai_for_object_detection import detect_objects

class TestEdgeAI(unittest.TestCase):
    def test_detection(self):
        result = detect_objects(None)
        self.assertIsInstance(result, list)
        self.assertGreaterEqual(result[0]["confidence"], 0)

if __name__ == '__main__':
    unittest.main()
