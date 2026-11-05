"""Provide a simple readiness check for the orchard robot."""

import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger


class ReadinessServer(Node):
    """Answer readiness requests using the standard Trigger service."""

    def __init__(self):
        super().__init__('readiness_server')
        # Keep the service available while this node is spinning.
        self.service = self.create_service(
            Trigger, '/check_ready', self.check_ready
        )
        self.get_logger().info('Readiness service is ready.')

    def check_ready(self, request, response):
        """Return a readiness result for each request."""
        # Trigger has an empty request and a success/message response.
        # This demo always succeeds; real hardware checks can go here later.
        response.success = True
        response.message = 'Orchard robot is ready.'
        self.get_logger().info('Readiness check requested.')
        return response


def main(args=None):
    """Run the service until interrupted."""
    rclpy.init(args=args)
    node = ReadinessServer()
    try:
        # Process incoming service requests.
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
