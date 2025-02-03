# gnfcs/loss_function/test/test_loss_function.py
import unittest
import numpy as np
import tensorflow as tf
from gnfcs.loss_function import LossFunction

class TestLossFunction(unittest.TestCase):
    def test_compute_loss(self):
        y_true = tf.constant([1.0, 2.0, 3.0])
        y_pred = tf.constant([1.1, 1.9, 3.2])
        loss = LossFunction.compute_loss(y_true, y_pred)
        self.assertTrue(loss.numpy() > 0)

if __name__ == '__main__':
    unittest.main()
