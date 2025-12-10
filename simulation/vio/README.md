# 360° Visual-Inertial Odometry Sandbox Bootstrap

This folder provides an **offline-friendly bootstrap** for building a lightweight VIO sandbox from
[93won/360_visual_inertial_odometry](https://github.com/93won/360_visual_inertial_odometry).
It mirrors the user story: clone/fork the repo, drop in a pose logger + optional ZeroMQ publisher,
wires VS Code for one-click CMake configure/build/run, and gives a pose-stream bridge so you can feed
poses into nav/control/RL loops without dragging in a full simulator.

Because the upstream repo is fetched from GitHub, cloning is deferred to a setup script. Run the steps
below on a machine with network access.

## 0) Dependencies (Ubuntu 20.04/22.04)
```bash
sudo apt update
sudo apt install -y build-essential cmake pkg-config git \
  libeigen3-dev libopencv-dev libgl1-mesa-dev libglew-dev \
  libxkbcommon-dev libwayland-dev libpython3-dev
# Optional for ZeroMQ pose streaming
sudo apt install -y libzmq3-dev
```

## 1) Clone fork (with submodules)
```bash
export VIO_FORK_URL=https://github.com/AVIUS001/aviabox_2025/360_visual_inertial_odometry.git
# Or point to your fork of 93won/360_visual_inertial_odometry
./simulation/vio/setup_360_vio_sandbox.sh --clone "$VIO_FORK_URL"
```
The script clones to `simulation/vio/360_visual_inertial_odometry` and runs `git submodule update --init --recursive`.

## 2) Apply sandbox customizations
`setup_360_vio_sandbox.sh` also:
- Adds **PoseLogger** (TUM CSV + stdout + optional ZeroMQ) via `src/utils/pose_logger.*` and appends a
  CMake block enabling `ENABLE_ZMQ_POSE_STREAM`.
- Drops in `.vscode/settings.json`, `launch.json`, and `tasks.json` that CMake Tools understands.
- Leaves a marker `# === aviabox VIO sandbox ===` in `CMakeLists.txt` to make the patch idempotent.

If you already cloned manually, run:
```bash
./simulation/vio/setup_360_vio_sandbox.sh --patch-only simulation/vio/360_visual_inertial_odometry
```

## 3) Dataset wiring
Download the `seq1_vio` dataset referenced in the upstream README and set an environment variable used
by the VS Code launch configuration:
```bash
export VIO_DATASET_PATH=$HOME/data/360/seq1_vio/
```
You can test the pose bridge without a heavy dataset using the tiny sample at
`simulation/vio/sample_data/seq1_vio/poses_tum_sample.csv`.

## 4) Build & run (terminal)
```bash
cd simulation/vio/360_visual_inertial_odometry
./build.sh
./build/bin/360_vio_example "$VIO_DATASET_PATH"
```
`360_vio_example` will emit poses. With the patch applied, you can wire in the logger in `examples/360_vio_example.cpp`:
```cpp
#include "utils/pose_logger.h"
...
PoseLogger logger("poses_tum.csv", true, "tcp://127.0.0.1:5556");
// After each pose update:
logger.log(timestamp_s, position, orientation);
```

## 5) VS Code one-click run
Open `simulation/vio/360_visual_inertial_odometry` in VS Code with the **CMake Tools** and **C/C++**
extensions installed. On open, CMake will configure automatically. Use the status bar to **Build** and
launch the provided `Run 360 VIO (seq1_vio)` debug target. The launch configuration reads
`VIO_DATASET_PATH` for the dataset location.

## 6) Pose-stream bridge (Python)
`simulation/vio/pose_stream_bridge.py` tails a TUM CSV and optionally republishes over ZeroMQ so you can
feed nav/control/RL loops without additional simulation. Example:
```bash
python simulation/vio/pose_stream_bridge.py simulation/vio/sample_data/seq1_vio/poses_tum_sample.csv
python simulation/vio/pose_stream_bridge.py poses_tum.csv --follow --zmq-endpoint tcp://127.0.0.1:5556
```
Downstream Python consumer:
```python
import zmq, struct
ctx = zmq.Context(); sub = ctx.socket(zmq.SUB)
sub.connect("tcp://127.0.0.1:5556")
sub.setsockopt_string(zmq.SUBSCRIBE, "")
packet = sub.recv()
t, px, py, pz, qx, qy, qz, qw = struct.unpack('d ddd dddd', packet)
```

## 7) Files in this sandbox folder
- `setup_360_vio_sandbox.sh`: clone + patch helper
- `templates/pose_logger.*`: logger source injected into the upstream repo
- `templates/cmake_pose_logger_append.cmake`: CMake snippet appended to `CMakeLists.txt`
- `templates/.vscode/*`: VS Code CMake settings
- `pose_stream_bridge.py`: tail/bridge script
- `sample_data/seq1_vio/poses_tum_sample.csv`: tiny sample log for testing the bridge

