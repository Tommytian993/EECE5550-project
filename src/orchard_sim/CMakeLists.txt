cmake_minimum_required(VERSION 3.16)
project(orchard_sim)

find_package(ament_cmake REQUIRED)

install(DIRECTORY launch config models worlds
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
