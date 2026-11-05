"""Drive a turtle to a goal using pose feedback."""

import math

from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node
from rclpy.signals import SignalHandlerOptions
from turtlesim_msgs.msg import Pose


class TurtleGoalController(Node):
    """Publish velocity commands until the turtle reaches its goal."""

    def __init__(self):
        super().__init__('turtle_goal_controller')
        self.declare_parameter('goal_x', 8.0)
        self.declare_parameter('goal_y', 8.0)
        self.goal_x = self.get_parameter('goal_x').value
        self.goal_y = self.get_parameter('goal_y').value
        self.finished = False
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscription = self.create_subscription(
            Pose, '/turtle1/pose', self.control_from_pose, 10
        )
        self.get_logger().info(f'Goal: ({self.goal_x}, {self.goal_y})')

    def control_from_pose(self, pose):
        """Adjust heading and speed using the measured pose."""
        if self.finished:
            return
        dx = self.goal_x - pose.x
        dy = self.goal_y - pose.y
        distance = math.hypot(dx, dy)
        msg = Twist()
        if distance < 0.1:
            self.publisher.publish(msg)
            self.finished = True
            self.get_logger().info(f'Goal reached; error={distance:.3f}')
            return
        error = math.atan2(dy, dx) - pose.theta
        error = math.atan2(math.sin(error), math.cos(error))
        msg.angular.z = max(-2.0, min(2.0, 4.0 * error))
        if abs(error) < 0.2:
            msg.linear.x = min(1.5, 1.5 * distance)
        self.publisher.publish(msg)

    def stop(self):
        """Publish zero velocity."""
        self.publisher.publish(Twist())


def main(args=None):
    """Process pose updates until arrival or interruption."""
    rclpy.init(args=args, signal_handler_options=SignalHandlerOptions.NO)
    node = TurtleGoalController()
    try:
        while rclpy.ok() and not node.finished:
            rclpy.spin_once(node, timeout_sec=0.1)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            node.stop()
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
