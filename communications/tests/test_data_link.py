# communications/tests/test_data_link.py
import unittest
from communications.data_link import DataLink

class TestDataLink(unittest.TestCase):
    def test_send_receive(self):
        dl = DataLink()
        dl.send("Test")
        received = dl.receive()
        self.assertEqual(received, "Test")

if __name__ == '__main__':
    unittest.main()
