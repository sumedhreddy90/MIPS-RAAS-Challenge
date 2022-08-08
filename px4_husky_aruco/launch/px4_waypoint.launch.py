#!/usr/bin/env python3

import os
import time

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, ExecuteProcess, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    """Launch Gazebo with a drone running PX4 communicating over ROS 2."""
    HOME = "/home/sumedh"
    PX4_RUN_DIR = HOME + '/PX4-Autopilot/build/px4_sitl_rtps/tmp'
    gazebo_launch_dir = os.path.join(get_package_share_directory('gazebo_ros'), 'launch')
    world = "/home/sumedh/PX4-Autopilot/Tools/sitl_gazebo/worlds/empty.world"
    model = "/home/sumedh/PX4-Autopilot/Tools/sitl_gazebo/models/iris_fpv_cam/iris_fpv_cam.sdf"
    os.environ["GAZEBO_MODEL_PATH"] = os.path.join(model)
    os.makedirs(PX4_RUN_DIR, exist_ok=True)

    return LaunchDescription([
        SetEnvironmentVariable('GAZEBO_PLUGIN_PATH',
                               HOME + '/PX4-Autopilot/build/px4_sitl_rtps/build_gazebo'),
        SetEnvironmentVariable('GAZEBO_MODEL_PATH', HOME + '/PX4-Autopilot/Tools/sitl_gazebo/models'),

        SetEnvironmentVariable('PX4_SIM_MODEL', 'iris'),
        SetEnvironmentVariable('PX4_SIM_SPEED_FACTOR', '10'),

        DeclareLaunchArgument('world', default_value=world),
        DeclareLaunchArgument('model', default_value=model),
        DeclareLaunchArgument('x', default_value='0.0'),
        DeclareLaunchArgument('y', default_value='0.0'),
        DeclareLaunchArgument('z', default_value='0.0'),
        DeclareLaunchArgument('R', default_value='0.0'),
        DeclareLaunchArgument('P', default_value='0.0'),
        DeclareLaunchArgument('Y', default_value='0.0'),
        ExecuteProcess(
            cmd=[
                'gazebo', '--verbose', world, '-s', 'libgazebo_ros_init.so', 
                '-s', 'libgazebo_ros_factory.so','model',
                '--spawn-file', LaunchConfiguration('model'),
                '--model-name', 'drone',
                '-x', LaunchConfiguration('x'),
                '-y', LaunchConfiguration('y'),
                '-z', LaunchConfiguration('z'),
                '-R', LaunchConfiguration('R'),
                '-P', LaunchConfiguration('P'),
                '-Y', LaunchConfiguration('Y')
            ],
            prefix="bash -c 'sleep 5s; $0 $@'",
            output='screen'),
            
            
        ExecuteProcess(
            cmd=[
                HOME + '/PX4-Autopilot/build/px4_sitl_rtps/bin/px4',
                HOME + '/PX4-Autopilot/build/px4_sitl_rtps/etc',
                '-s',
                HOME + '/PX4-Autopilot/build/px4_sitl_rtps/etc/init.d-posix/rcS',
                '-t',
                HOME + '/PX4-Autopilot/test_data'
            ],
            cwd=PX4_RUN_DIR,
            output='screen'),
        ExecuteProcess(
            cmd=['micrortps_agent', '-t', 'UDP'],
            output='screen'), 
])