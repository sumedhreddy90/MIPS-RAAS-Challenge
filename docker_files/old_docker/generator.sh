set -x

source /opt/ros/kinetic/setup.bash
cd ~/ros_catkin_ws/
apt-get install -y python-pip
apt-get install -y libpoco-dev
pip install future

rosinstall_generator class_loader --rosdistro kinetic --deps --exclude RPP --wet-only --tar > additional.rosinstall
rosinstall_generator diagnostic_msgs --rosdistro kinetic --deps --exclude RPP --wet-only --tar >> additional.rosinstall
rosinstall_generator geographic_msgs --rosdistro kinetic --deps --exclude RPP --wet-only --tar >> additional.rosinstall
rosinstall_generator geometry2 --rosdistro kinetic --deps --exclude RPP --wet-only --tar >> additional.rosinstall
rosinstall_generator libmavconn --rosdistro kinetic --deps --exclude RPP --wet-only --tar >> additional.rosinstall
rosinstall_generator map_msgs --rosdistro kinetic --deps --exclude RPP --wet-only --tar >> additional.rosinstall
rosinstall_generator mavlink --rosdistro kinetic --deps --exclude RPP --wet-only --tar >> additional.rosinstall
rosinstall_generator mavros --rosdistro kinetic --deps --exclude RPP --wet-only --tar >> additional.rosinstall
rosinstall_generator mavros_msgs --rosdistro kinetic --deps --exclude RPP --wet-only --tar >> additional.rosinstall
rosinstall_generator nav_msgs --rosdistro kinetic --deps --exclude RPP --wet-only --tar >> additional.rosinstall
rosinstall_generator nodelet --rosdistro kinetic --deps --exclude RPP --wet-only --tar >> additional.rosinstall
rosinstall_generator nodelet_topic_tools --rosdistro kinetic --deps --exclude RPP --wet-only --tar >> additional.rosinstall
rosinstall_generator pcl_msgs --rosdistro kinetic --deps --exclude RPP --wet-only --tar >> additional.rosinstall
rosinstall_generator rosbag_migration_rule --rosdistro kinetic --deps --exclude RPP --wet-only --tar >> additional.rosinstall
rosinstall_generator rosconsole_bridge --rosdistro kinetic --deps --exclude RPP --wet-only --tar >> additional.rosinstall
rosinstall_generator serial --rosdistro kinetic --deps --exclude RPP --wet-only --tar >> additional.rosinstall
rosinstall_generator shape_msgs --rosdistro kinetic --deps --exclude RPP --wet-only --tar >> additional.rosinstall
rosinstall_generator stereo_msgs --rosdistro kinetic --deps --exclude RPP --wet-only --tar >> additional.rosinstall
rosinstall_generator tf --rosdistro kinetic --deps --exclude RPP --wet-only --tar >> additional.rosinstall
rosinstall_generator trajectory_msgs --rosdistro kinetic --deps --exclude RPP --wet-only --tar >> additional.rosinstall
rosinstall_generator uuid_msgs --rosdistro kinetic --deps --exclude RPP --wet-only --tar >> additional.rosinstall
rosinstall_generator visualization_msgs --rosdistro kinetic --deps --exclude RPP --wet-only --tar >> additional.rosinstall

wstool init -j8 src additional.rosinstall
rosdep install --from-paths src --ignore-src --rosdistro kinetic -y -r
src/catkin/bin/catkin_make_isolated -j4 --install -DCMAKE_BUILD_TYPE=Release --install-space /opt/ros/kinetic
catkin_make_isolated -j1 --install -DCMAKE_BUILD_TYPE=Release --install-space /opt/ros/kinetic
