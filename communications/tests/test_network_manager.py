# communications/tests/test_network_manager.py
import unittest
from communications.network_manager import NetworkManager

class TestNetworkManager(unittest.TestCase):
    def test_connection(self):
        nm = NetworkManager()
        nm.connect("127.0.0.1")
        self.assertEqual(nm.status, "connected")
        nm.disconnect()
        self.assertEqual(nm.status, "disconnected")

if __name__ == '__main__':
    unittest.main()
