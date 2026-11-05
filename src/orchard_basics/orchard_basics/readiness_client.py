"""Request a readiness check from the robot."""

import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger


def main(args=None):
    """Send one request, print the reply, and exit."""
    rclpy.init(args=args)
    node = Node('readiness_client')

    try:
        # Both the service name and interface type must match the server.
        client = node.create_client(Trigger, '/check_ready')
        while not client.wait_for_service(timeout_sec=1.0):
            if not rclpy.ok():
                return
            node.get_logger().info('Waiting for readiness service...')

        # Trigger has no request fields. The future holds the eventual reply.
        future = client.call_async(Trigger.Request())
        rclpy.spin_until_future_complete(node, future)
        if not future.done():
            return

        response = future.result()
        if response is None:
            raise RuntimeError('Readiness service returned no response.')
        node.get_logger().info(
            f'Ready: {response.success}; {response.message}'
        )
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
