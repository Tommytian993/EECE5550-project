from glob import glob

from setuptools import find_packages, setup

package_name = 'orchard_basics'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
        ('share/' + package_name + '/config', glob('config/*.yaml')),
    ],
    package_data={'': ['py.typed']},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jerrywang',
    maintainer_email='wang.tianye2@northeastern.edu',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'turtle_goal_controller = orchard_basics.turtle_goal_controller:main',
            'turtle_controller = orchard_basics.turtle_controller:main',
            'hello_node = orchard_basics.hello_node:main',
            'readiness_client = orchard_basics.readiness_client:main',
            'readiness_server = orchard_basics.readiness_server:main',
            'status_publisher = orchard_basics.status_publisher:main',
            'status_subscriber = orchard_basics.status_subscriber:main',
        ],
    },
)
