#include "vidar/vio_node.hpp"

namespace vidar {

VIONode::VIONode() {
    std::cout << "VIONode created." << std::endl;
}

VIONode::~VIONode() {
    std::cout << "VIONode destroyed." << std::endl;
}

void VIONode::initialize() {
    std::cout << "VIONode initialized." << std::endl;
}

std::vector<double> VIONode::process(const std::vector<unsigned char>& image_data,
                                       const std::vector<double>& imu_data) {
    std::cout << "Processing VIO data." << std::endl;
    // Return dummy pose: [x, y, z, qx, qy, qz, qw]
    return std::vector<double>{0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0};
}

} // namespace vidar
