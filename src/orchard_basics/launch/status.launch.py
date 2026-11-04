from launch import LaunchDescription
from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    config_file = str(
        Path(get_package_share_directory('orchard_basics'))
        / 'config'
        / 'status.yaml'
    )

    return LaunchDescription([
        Node(
            package='orchard_basics',
            executable='status_publisher',
            parameters=[config_file],
            output='screen',
        ),
        Node(
            package='orchard_basics',
            executable='status_subscriber',
            output='screen',
        ),
    ])
