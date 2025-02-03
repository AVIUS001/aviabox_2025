# gnfcs/data_loader.py
import numpy as np

class DataLoader:
    def __init__(self, filepath, delimiter=','):
        self.filepath = filepath
        self.delimiter = delimiter

    def load_data(self):
        data = np.loadtxt(self.filepath, delimiter=self.delimiter)
        X = data[:, :-1]
        y = data[:, -1]
        return X, y
