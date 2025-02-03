#!/usr/bin/env python3
"""
vidar_perception.py

Integrates outputs from VIO, VINS, and ORB_SLAM3 nodes.
"""

import numpy as np

def process_perception(vio_pose, vins_state, orb_pose):
    # For demonstration, average the position from VIO and ORB_SLAM3.
    position = (np.array(vio_pose[:3]) + np.array(orb_pose[:3])) / 2.0
    return {
        "position": position.tolist(),
        "orientation": orb_pose[3:7],
        "vins_state": vins_state
    }

if __name__ == "__main__":
    vio_pose = [0, 0, 0, 1, 0, 0, 0]
    vins_state = [0, 0, 0, 0, 0, 0]
    orb_pose = [0.1, 0.1, 0.1, 0.98, 0, 0, 0]
    result = process_perception(vio_pose, vins_state, orb_pose)
    print("Perception output:", result)
