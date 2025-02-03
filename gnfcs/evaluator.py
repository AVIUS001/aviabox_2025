# gnfcs/evaluator.py
import matplotlib.pyplot as plt

class Evaluator:
    def __init__(self, policy, loss_function):
        self.policy = policy
        self.loss_function = loss_function

    def evaluate(self, X, y):
        predictions = self.policy.model.predict(X)
        loss = self.loss_function.compute_loss(y, predictions)
        print("Evaluation Loss:", loss.numpy())
        return loss.numpy()

    def plot_predictions(self, X, y):
        predictions = self.policy.model.predict(X)
        plt.figure()
        plt.plot(y, label='True')
        plt.plot(predictions, label='Predicted')
        plt.xlabel("Sample Index")
        plt.ylabel("Output")
        plt.legend()
        plt.show()
