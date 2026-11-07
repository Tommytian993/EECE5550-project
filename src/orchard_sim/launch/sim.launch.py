"""Launch the robot simulation and ROS-Gazebo bridge together."""

from pathlib import Path
from uuid import uuid4

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, SetEnvironmentVariable
from launch.actions import Shutdown
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import EnvironmentVariable, LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    """Find installed resources, start Gazebo, and connect the ROS topics."""
    share = Path(get_package_share_directory('orchard_sim'))
    world = str(share / 'worlds' / 'empty_orchard.sdf')
    gui = LaunchConfiguration('gui')

    return LaunchDescription([
        DeclareLaunchArgument('gui', default_value='true'),
        DeclareLaunchArgument(
            'gz_partition', default_value='orchard_' + uuid4().hex[:8],
            description='Gazebo transport partition for this simulation',
        ),
        SetEnvironmentVariable('GZ_PARTITION', LaunchConfiguration('gz_partition')),

        SetEnvironmentVariable(
            'GZ_SIM_RESOURCE_PATH',
            [str(share / 'models'), ':',
             EnvironmentVariable('GZ_SIM_RESOURCE_PATH', default_value='')],
        ),

        ExecuteProcess(
            cmd=['gz', 'sim', '-r', world],
            condition=IfCondition(gui), output='screen',
            on_exit=Shutdown(reason='Gazebo exited'),
        ),
        ExecuteProcess(
            cmd=['gz', 'sim', '-s', '-r', world],
            condition=UnlessCondition(gui), output='screen',
            on_exit=Shutdown(reason='Gazebo exited'),
        ),

        Node(
            package='ros_gz_bridge', executable='parameter_bridge',
            name='orchard_bridge', output='screen',
            parameters=[{'config_file': str(share / 'config' / 'bridge.yaml')}],
            on_exit=Shutdown(reason='Bridge exited'),
        ),
    ])
