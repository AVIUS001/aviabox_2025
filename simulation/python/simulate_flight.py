#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def simulate_flight(duration=10, dt=0.1):
    t = np.arange(0, duration, dt)
    altitude = 10 + 2 * np.sin(0.5 * t) + np.random.normal(0, 0.2, len(t))
    return t, altitude

def main():
    t, altitude = simulate_flight()
    plt.plot(t, altitude)
    plt.xlabel("Time (s)")
    plt.ylabel("Altitude (m)")
    plt.title("Simulated Flight Altitude")
    plt.show()

if __name__ == "__main__":
    main()
