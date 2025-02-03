# vidar/CMakeLists.txt
cmake_minimum_required(VERSION 3.5)
project(vidar)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)

# Add the source files for the nodes.
add_library(vidar_nodes
    src/vio_node.cpp
    src/vins_node.cpp
    src/orb_slam3_node.cpp
    src/swarm_node.cpp
)

# Optionally create an executable for testing.
add_executable(vidar_test src/vio_node.cpp)
target_link_libraries(vidar_test vidar_nodes)
