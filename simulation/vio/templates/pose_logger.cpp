#include "pose_logger.h"

#include <iomanip>
#include <iostream>

#ifdef ENABLE_ZMQ_POSE_STREAM
#include <zmq.h>
#endif

namespace {
constexpr int kPrecision = 9;
}

PoseLogger::PoseLogger(const std::string &tum_path, bool also_stdout, const std::string &zmq_endpoint)
    : to_stdout_(also_stdout) {
  if (!tum_path.empty()) {
    file_.emplace(tum_path);
    (*file_) << "# timestamp tx ty tz qx qy qz qw\n";
  }

#ifdef ENABLE_ZMQ_POSE_STREAM
  if (!zmq_endpoint.empty()) {
    zmq_ctx_ = zmq_ctx_new();
    zmq_pub_ = zmq_socket(zmq_ctx_, ZMQ_PUB);
    if (zmq_pub_) {
      // Bind in-process publisher. Users connect via SUB on the same endpoint.
      if (zmq_bind(zmq_pub_, zmq_endpoint.c_str()) != 0) {
        std::cerr << "[PoseLogger] Failed to bind ZMQ endpoint " << zmq_endpoint << "\n";
        zmq_close(zmq_pub_);
        zmq_pub_ = nullptr;
      }
    }
  }
#endif
}

PoseLogger::~PoseLogger() {
#ifdef ENABLE_ZMQ_POSE_STREAM
  if (zmq_pub_) {
    zmq_close(zmq_pub_);
    zmq_pub_ = nullptr;
  }
  if (zmq_ctx_) {
    zmq_ctx_term(zmq_ctx_);
    zmq_ctx_ = nullptr;
  }
#endif
}

void PoseLogger::log(double timestamp_s, const Eigen::Vector3d &p, const Eigen::Quaterniond &q) {
  std::ostringstream oss;
  oss << std::fixed << std::setprecision(kPrecision) << timestamp_s << ' '
      << p.x() << ' ' << p.y() << ' ' << p.z() << ' '
      << q.x() << ' ' << q.y() << ' ' << q.z() << ' ' << q.w();

  if (file_) {
    (*file_) << oss.str() << '\n';
  }
  if (to_stdout_) {
    std::cout << oss.str() << std::endl;
  }

#ifdef ENABLE_ZMQ_POSE_STREAM
  if (zmq_pub_) {
    struct PosePacket {
      double t;
      double p[3];
      double q[4];
    } packet{timestamp_s, {p.x(), p.y(), p.z()}, {q.x(), q.y(), q.z(), q.w()}};

    // Non-blocking send; downstream consumers can SUB and unpack with struct "d ddd dddd".
    zmq_send(zmq_pub_, &packet, sizeof(packet), ZMQ_DONTWAIT);
  }
#endif
}

