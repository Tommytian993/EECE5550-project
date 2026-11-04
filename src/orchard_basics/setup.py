from setuptools import find_packages, setup
from glob import glob
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
            'hello_node = orchard_basics.hello_node:main',
            'status_publisher = orchard_basics.status_publisher:main',
            'status_subscriber = orchard_basics.status_subscriber:main',
        ],
    },
)
