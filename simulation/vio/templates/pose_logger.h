#pragma once

#include <Eigen/Dense>
#include <Eigen/Geometry>
#include <fstream>
#include <optional>
#include <string>

// Lightweight pose logger that can write TUM-style CSV, mirror output to stdout,
// and optionally publish binary pose packets over ZeroMQ (if ENABLE_ZMQ_POSE_STREAM is set).
class PoseLogger {
public:
  // tum_path: file path for TUM CSV output. Leave empty to disable file logging.
  // also_stdout: if true, mirror each log line to stdout for quick inspection.
  // zmq_endpoint: e.g., "tcp://127.0.0.1:5556". Only used when built with ENABLE_ZMQ_POSE_STREAM.
  PoseLogger(const std::string &tum_path, bool also_stdout = true, const std::string &zmq_endpoint = "");

  // Log a pose in seconds + translation + quaternion (xyzw ordering for TUM compatibility).
  void log(double timestamp_s, const Eigen::Vector3d &p, const Eigen::Quaterniond &q);

  ~PoseLogger();

private:
  std::optional<std::ofstream> file_;
  bool to_stdout_ = true;

#ifdef ENABLE_ZMQ_POSE_STREAM
  void *zmq_ctx_ = nullptr;
  void *zmq_pub_ = nullptr;
#endif
};

