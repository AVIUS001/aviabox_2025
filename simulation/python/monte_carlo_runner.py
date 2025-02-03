#!/usr/bin/env python3
import numpy as np

def monte_carlo_simulation(num_trials=1000):
    errors = []
    for _ in range(num_trials):
        noise = np.random.normal(0, 0.5)
        measured_altitude = 10 + noise
        error = abs(measured_altitude - 10)
        errors.append(error)
    return np.array(errors)

def main():
    errors = monte_carlo_simulation()
    print("Mean error:", np.mean(errors))
    print("Std error:", np.std(errors))

if __name__ == "__main__":
    main()
