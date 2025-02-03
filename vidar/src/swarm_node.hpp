#include "vidar/swarm_node.hpp"

namespace vidar {

SwarmNode::SwarmNode() {
    std::cout << "SwarmNode created." << std::endl;
}

SwarmNode::~SwarmNode() {
    std::cout << "SwarmNode destroyed." << std::endl;
}

void SwarmNode::initialize() {
    std::cout << "SwarmNode initialized." << std::endl;
}

void SwarmNode::broadcast(const std::string& message) {
    std::cout << "Broadcasting: " << message << std::endl;
}

std::string SwarmNode::receive() {
    std::string msg = "Dummy swarm message";
    std::cout << "Received: " << msg << std::endl;
    return msg;
}

} // namespace vidar
