# Pose logger + optional ZeroMQ publisher for 360_visual_inertial_odometry
option(ENABLE_ZMQ_POSE_STREAM "Publish poses over ZeroMQ in addition to CSV/stdout" OFF)

find_package(PkgConfig QUIET)
if(ENABLE_ZMQ_POSE_STREAM AND PKG_CONFIG_FOUND)
  pkg_check_modules(ZeroMQ REQUIRED libzmq)
endif()

add_library(pose_logger src/utils/pose_logger.cpp)
target_include_directories(pose_logger PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src)
target_link_libraries(pose_logger PUBLIC Eigen3::Eigen)
target_compile_features(pose_logger PUBLIC cxx_std_17)

if(ENABLE_ZMQ_POSE_STREAM AND ZeroMQ_FOUND)
  target_link_libraries(pose_logger PUBLIC ${ZeroMQ_LIBRARIES})
  target_include_directories(pose_logger PUBLIC ${ZeroMQ_INCLUDE_DIRS})
  target_compile_definitions(pose_logger PUBLIC ENABLE_ZMQ_POSE_STREAM)
endif()

if(TARGET 360_vio_example)
  target_link_libraries(360_vio_example PRIVATE pose_logger)
  if(ENABLE_ZMQ_POSE_STREAM AND ZeroMQ_FOUND)
    target_link_libraries(360_vio_example PRIVATE ${ZeroMQ_LIBRARIES})
    target_compile_definitions(360_vio_example PRIVATE ENABLE_ZMQ_POSE_STREAM)
  endif()
endif()

