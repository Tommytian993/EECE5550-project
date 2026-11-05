import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger


class ReadinessServer(Node):

    def __init__(self):
        super().__init__('readiness_server')

        self.declare_parameter('ready', True)

        self.service = self.create_service(
            Trigger, '/check_ready', self.check_ready
        )
        self.get_logger().info('Readiness service is ready.')

    def check_ready(self, request, response):
        ready = self.get_parameter('ready').value
        response.success = ready
        response.message = (
            'Orchard robot is ready.'
            if ready else 'Orchard robot is not ready.'
        )
        self.get_logger().info(f'Readiness check requested: {ready}')

        return response


def main(args=None):
    rclpy.init(args=args)
    node = ReadinessServer()
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
