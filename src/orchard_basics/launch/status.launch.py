from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='orchard_basics',
            executable='status_publisher',
            output='screen',
        ),
        Node(
            package='orchard_basics',
            executable='status_subscriber',
            output='screen',
        ),
    ])

