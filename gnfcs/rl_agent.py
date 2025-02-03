# gnfcs/rl_agent.py
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

class RLAgent:
    def __init__(self, state_dim=6, action_dim=76, lr=0.001):
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

    def select_action(self, state):
        state = np.expand_dims(state, axis=0)
        action_values = self.model.predict(state, verbose=0)
        return np.argmax(action_values)

    def update(self, state, action, reward, next_state, done, gamma=0.99):
        state = np.expand_dims(state, axis=0)
        next_state = np.expand_dims(next_state, axis=0)
        target = self.model.predict(state, verbose=0)
        if done:
            target[0][action] = reward
        else:
            t = self.model.predict(next_state, verbose=0)
            target[0][action] = reward + gamma * np.amax(t)
        self.model.fit(state, target, verbose=0)
