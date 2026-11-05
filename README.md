# Orchard ROS 2 Basics

A basic ROS 2 Lyrical workspace.

## Build

```bash
cd ~/orchard_ws
source /opt/ros/lyrical/setup.bash
colcon build --packages-select orchard_basics --symlink-install
source install/setup.bash
```

In each new terminal:

```bash
source /opt/ros/lyrical/setup.bash
source ~/orchard_ws/install/setup.bash
```

## Run

Publisher and subscriber (Ctrl+C to stop):

```bash
ros2 launch orchard_basics status.launch.py
```

Readiness server and client (separate terminals):

```bash
ros2 run orchard_basics readiness_server
```

```bash
ros2 run orchard_basics readiness_client
```

## Test

From the workspace root:

```bash
colcon test --packages-select orchard_basics
colcon test-result --verbose
```
