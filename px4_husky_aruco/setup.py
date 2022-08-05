from setuptools import setup
import os
from glob import glob

package_name = 'px4_husky_aruco'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
        (os.path.join('share', package_name,'worlds'), glob('worlds/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sumedh',
    maintainer_email='sumedhrk@umd.com',
    description='PX4 on Husky arcuo based landing',
    license='BSD 3-Clause "New" or "Revised" License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
