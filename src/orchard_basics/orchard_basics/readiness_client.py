import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger


def main(args=None):
    rclpy.init(args=args)
    node = Node('readiness_client')

    try:
        client = node.create_client(Trigger, '/check_ready')

        while not client.wait_for_service(timeout_sec=1.0):
            if not rclpy.ok():
                return
            node.get_logger().info('Waiting for readiness service...')

        request = Trigger.Request()

        future = client.call_async(request)

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
