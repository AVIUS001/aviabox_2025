"""Tiny pose-stream bridge for 360 VIO TUM CSV logs.

- Reads TUM-style pose CSV (timestamp tx ty tz qx qy qz qw).
- Optionally follows the file for new poses and republishes over ZeroMQ.
- Prints each pose to stdout/CSV to make it easy to feed nav/control/RL loops.
"""

import argparse
import csv
import time
from pathlib import Path

try:
    import zmq  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    zmq = None


POSE_FIELDS = ["timestamp", "tx", "ty", "tz", "qx", "qy", "qz", "qw"]


def send_zmq(socket, row):
    if socket is None:
        return
    import struct

    packet = struct.pack(
        "d ddd dddd",
        float(row["timestamp"]),
        float(row["tx"]),
        float(row["ty"]),
        float(row["tz"]),
        float(row["qx"]),
        float(row["qy"]),
        float(row["qz"]),
        float(row["qw"]),
    )
    socket.send(packet)


def open_zmq(endpoint):
    if not endpoint:
        return None
    if zmq is None:
        raise RuntimeError("pyzmq is not installed; install with `pip install pyzmq`. ")
    ctx = zmq.Context.instance()
    sock = ctx.socket(zmq.PUB)
    sock.bind(endpoint)
    return sock


def stream_file(path: Path, follow: bool, zmq_endpoint: str):
    socket = open_zmq(zmq_endpoint) if zmq_endpoint else None
    last_size = 0
    while True:
        if not path.exists():
            if follow:
                time.sleep(0.2)
                continue
            raise FileNotFoundError(path)

        with path.open("r", newline="") as f:
            reader = csv.DictReader(f, fieldnames=POSE_FIELDS, delimiter=" ")
            for row in reader:
                # skip comments
                if row["timestamp"].startswith("#"):
                    continue
                print(
                    f"{row['timestamp']} {row['tx']} {row['ty']} {row['tz']} "
                    f"{row['qx']} {row['qy']} {row['qz']} {row['qw']}"
                )
                send_zmq(socket, row)

        if not follow:
            break
        current_size = path.stat().st_size
        if current_size == last_size:
            time.sleep(0.2)
        last_size = current_size


def main():
    parser = argparse.ArgumentParser(description="Pose stream bridge for 360 VIO")
    parser.add_argument(
        "log_path",
        type=Path,
        help="Path to TUM-style pose CSV (e.g., poses_tum.csv from 360_vio_example)",
    )
    parser.add_argument("--follow", action="store_true", help="Tail the file for new poses")
    parser.add_argument(
        "--zmq-endpoint",
        default="",
        help="Optional ZeroMQ PUB endpoint to mirror poses (e.g., tcp://127.0.0.1:5556)",
    )
    args = parser.parse_args()

    stream_file(args.log_path, args.follow, args.zmq_endpoint)


if __name__ == "__main__":
    main()
