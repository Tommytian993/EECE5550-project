"""Run a short timed movement sequence in turtlesim."""

import math

from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node


class TurtleController(Node):
    """Publish timed velocity commands to the first turtle."""

    def __init__(self):
        super().__init__('turtle_controller')

        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        self.steps = [
            (2.0, 1.0, 0.0),
            (math.pi / 2.0, 0.0, 1.0),
            (2.0, 1.0, 0.0),
        ]
        self.step_index = 0
        self.step_started = None
        self.finished = False
        self.wait_logged = False

        self.timer = self.create_timer(0.1, self.update_motion)

    def update_motion(self):
        """Advance the sequence and publish the current velocity."""
        if self.step_started is None:
            if self.publisher.get_subscription_count() == 0:
                if not self.wait_logged:
                    self.get_logger().info('Waiting for a cmd_vel subscriber...')
                    self.wait_logged = True
                return
            self.step_started = self.get_clock().now()
            self.get_logger().info('Step 1: move forward')

        duration, forward, turn = self.steps[self.step_index]
        elapsed = (self.get_clock().now() - self.step_started).nanoseconds / 1e9

        if elapsed >= duration:
            self.step_index += 1
            if self.step_index == len(self.steps):
                self.stop()
                self.finished = True
                self.timer.cancel()
                self.get_logger().info('Sequence complete: stopped')
                return

            self.step_started = self.get_clock().now()
            _, forward, turn = self.steps[self.step_index]
            action = 'turn left' if self.step_index == 1 else 'move forward'
            self.get_logger().info(f'Step {self.step_index + 1}: {action}')

        msg = Twist()
        msg.linear.x = forward
        msg.angular.z = turn
        self.publisher.publish(msg)

    def stop(self):
        """Publish zero velocity."""
        self.publisher.publish(Twist())


def main(args=None):
    """Run until the motion sequence finishes or the user interrupts."""
    rclpy.init(args=args, signal_handler_options=rclpy.signals.SignalHandlerOptions.NO)
    node = TurtleController()
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
