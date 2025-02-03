# gnfcs/neural_network_policy.py
import tensorflow as tf
from tensorflow.keras import layers, models

class NeuralNetworkPolicy:
    def __init__(self, state_dim=6, action_dim=76, lr=0.0003):
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.lr = lr
        self.model = self.build_model()

    def build_model(self):
        inputs = layers.Input(shape=(self.state_dim,))
        x = layers.Dense(128, activation='relu')(inputs)
        x = layers.Dense(128, activation='relu')(x)
        outputs = layers.Dense(self.action_dim, activation='linear')(x)
        model = models.Model(inputs, outputs)
        model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=self.lr),
                      loss='mse')
        return model

    def predict(self, state):
        state = tf.convert_to_tensor(state, dtype=tf.float32)
        return self.model(state)

    def train(self, states, targets, epochs=1):
        self.model.fit(states, targets, epochs=epochs, verbose=0)

# --- Test for neural_network_policy ---
if __name__ == "__main__":
    import numpy as np
    policy = NeuralNetworkPolicy(state_dim=6, action_dim=76)
    dummy_state = np.random.rand(1, 6)
    print("Policy output:", policy.predict(dummy_state))
