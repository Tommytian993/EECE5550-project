# Import the ROS 2 Python library.
import rclpy
from rclpy.node import Node


class HelloNode(Node):

    def __init__(self):
        # Initialize the node with a unique name.
        super().__init__('hello_node')

        # Trigger say_hello every 2 seconds.
        self.timer = self.create_timer(2.0, self.say_hello)

    def say_hello(self):
        # Print a ROS 2 log message.
        self.get_logger().info('Hello from our orchard robot!')


def main(args=None):
    # Initialize the ROS 2 system.
    rclpy.init(args=args)

    # Create our node.
    node = HelloNode()

    try:
        # Keep processing callbacks.
        rclpy.spin(node)
    except KeyboardInterrupt:
        # Stop gracefully when Ctrl+C is pressed.
        pass
    finally:
        # Clean up the node and ROS 2 resources.
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
