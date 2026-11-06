# Orchard Simulation

Requires ROS 2 Lyrical and `ros-lyrical-ros-gz`.

## Build

```bash
cd ~/orchard_ws
source /opt/ros/lyrical/setup.bash
colcon build --packages-select orchard_sim --symlink-install
source install/setup.bash
```

## Run

```bash
ros2 launch orchard_sim sim.launch.py
```

Gazebo starts playing automatically. The launch also starts the ROS bridge.
Close old Gazebo and bridge processes before starting. Ctrl+C stops the launch.
Use `gui:=false` for headless mode.

## Control

In another ROS-enabled terminal:

```bash
ros2 topic pub --once /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.3}}"
```

The robot keeps moving until a new command arrives. Stop after a second or two:

```bash
ros2 topic pub --once /cmd_vel geometry_msgs/msg/Twist '{}'
ros2 topic echo /odom --once
```

Each launch uses an isolated Gazebo transport partition to avoid mixing scenes.
Use ROS `/cmd_vel` for control. For direct `gz` debugging, launch with
`gz_partition:=orchard_debug` and export `GZ_PARTITION=orchard_debug` in the debugging terminal.
