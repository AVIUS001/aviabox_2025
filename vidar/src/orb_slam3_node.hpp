#include "vidar/orb_slam3_node.hpp"

namespace vidar {

ORB_SLAM3Node::ORB_SLAM3Node() {
    std::cout << "ORB_SLAM3Node created." << std::endl;
}

ORB_SLAM3Node::~ORB_SLAM3Node() {
    std::cout << "ORB_SLAM3Node destroyed." << std::endl;
}

void ORB_SLAM3Node::initialize() {
    std::cout << "ORB_SLAM3Node initialized." << std::endl;
}

std::vector<double> ORB_SLAM3Node::process(const std::vector<unsigned char>& image_data) {
    std::cout << "Processing ORB_SLAM3 data." << std::endl;
    return std::vector<double>{0.1, 0.1, 0.1, 0.98, 0.0, 0.0, 0.0};
}

} // namespace vidar
