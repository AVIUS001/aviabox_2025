#ifndef VIDAR_VIO_NODE_HPP
#define VIDAR_VIO_NODE_HPP

#include <vector>
#include <iostream>

namespace vidar {

/**
 * @brief Visual Inertial Odometry (VIO) Node.
 *
 * This class provides a stub for a VIO node responsible for processing
 * visual and inertial sensor data to estimate the pose and trajectory.
 */
class VIONode {
public:
    VIONode();
    ~VIONode();

    /**
     * @brief Initialize the VIO node.
     */
    void initialize();

    /**
     * @brief Process sensor data.
     *
     * @param image_data The image data (for example, as a vector of bytes).
     * @param imu_data The inertial measurement data (e.g., accelerometer and gyroscope readings).
     * @return Estimated pose as a vector (e.g., [x, y, z, qx, qy, qz, qw]).
     */
    std::vector<double> process(const std::vector<unsigned char>& image_data,
                                const std::vector<double>& imu_data);
};

} // namespace vidar

#endif // VIDAR_VIO_NODE_HPP
