import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class StatusPublisher(Node):

    def __init__(self):
        # Initialize our publisher node.
        super().__init__('status_publisher')

        # Create a publisher on the /orchard_status topic.
        # The queue depth is 10.
        self.publisher = self.create_publisher(
            String, '/orchard_status', 10
        )

        # Publishing interval in seconds.
        self.declare_parameter('publish_interval', 1.0)
        interval = self.get_parameter('publish_interval').value

        self.timer = self.create_timer(interval, self.publish_status)

        # Count how many messages we have published.
        self.count = 0

    def publish_status(self):
        # Create a message of type String.
        msg = String()

        # Set the message content.
        msg.data = f'Orchard robot is running! Count: {self.count}'

        # Send the message to the topic.
        self.publisher.publish(msg)

        # Print a log to the terminal.
        self.get_logger().info(f'Publishing: {msg.data}')

        self.count += 1


def main(args=None):
    rclpy.init(args=args)
    node = StatusPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
