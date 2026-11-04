import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class StatusSubscriber(Node):
    def __init__(self):
        # Initialize our subscriber node.
        super().__init__('status_subscriber')

        # Subscribe to the /orchard_status topic.
        self.subscription = self.create_subscription(
            String,
            '/orchard_status',
            self.status_callback,
            10
        )

    def status_callback(self, msg):
        # This callback runs whenever a message arrives.
        self.get_logger().info(f'Received: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = StatusSubscriber()

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
