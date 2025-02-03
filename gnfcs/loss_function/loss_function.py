# gnfcs/loss_function.py
import tensorflow as tf

class LossFunction:
    @staticmethod
    def compute_loss(y_true, y_pred):
        mse_loss = tf.reduce_mean(tf.square(y_true - y_pred))
        pde_loss = 0.0  # Stub: add PDE-based regularization if needed.
        return mse_loss + pde_loss

# --- Test for loss_function ---
if __name__ == "__main__":
    import numpy as np
    y_true = np.array([1.0, 2.0, 3.0])
    y_pred = np.array([1.1, 1.9, 3.2])
    loss = LossFunction.compute_loss(y_true, y_pred)
    print("Computed loss:", loss.numpy())
