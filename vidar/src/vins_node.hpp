#include "vidar/vins_node.hpp"

namespace vidar {

VINSNode::VINSNode() {
    std::cout << "VINSNode created." << std::endl;
}

VINSNode::~VINSNode() {
    std::cout << "VINSNode destroyed." << std::endl;
}

void VINSNode::initialize() {
    std::cout << "VINSNode initialized." << std::endl;
}

std::vector<double> VINSNode::process(const std::vector<unsigned char>& image_data,
                                       const std::vector<double>& imu_data) {
    std::cout << "Processing VINS data." << std::endl;
    return std::vector<double>{0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
}

} // namespace vidar
