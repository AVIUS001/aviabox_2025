# gnfcs/trainer.py
class Trainer:
    def __init__(self, policy, loss_function, learning_rate=0.0003):
        self.policy = policy
        self.loss_function = loss_function
        self.learning_rate = learning_rate

    def train(self, states, targets, epochs=1):
        self.policy.train(states, targets, epochs=epochs)
