FROM osrf/ros:foxy-desktop-focal

# Tools I find useful during development
RUN apt-get update \
 && apt-get install -y \
    build-essential \
    lsb-release \
    sudo \
    wget \
    ros-foxy-gazebo-dev \
    ros-foxy-gazebo-msgs \
    ros-foxy-gazebo-ros \
    ros-foxy-gazebo-plugins \
    ros-foxy-gazebo-ros-pkgs \
    ros-foxy-xacro \
    ros-foxy-desktop \
 && apt-get clean

RUN sudo apt -y install python3-pip

RUN sudo apt install python3-colcon-common-extensions

RUN sudo apt install ros-foxy-eigen3-cmake-module


# Make sure everything is up to date before building from source
RUN apt-get update \
  && apt-get dist-upgrade -y \
  && apt-get clean

RUN /bin/sh -c 'echo ". /opt/ros/foxy/setup.bash" >> ~/.bashrc' \
  && /bin/sh -c 'echo ". /usr/share/gazebo/setup.sh" >> ~/.bashrc'

RUN cd $HOME
RUN git clone https://github.com/PX4/PX4-Autopilot.git --recursive
RUN bash ./PX4-Autopilot/Tools/setup/ubuntu.sh

RUN cd $HOME
RUN git clone https://github.com/eProsima/foonathan_memory_vendor.git
WORKDIR /foonathan_memory_vendor
RUN mkdir build && cd build \
    cmake .. \
    cmake --build . --target install

RUN cd $HOME
RUN git clone --recursive https://github.com/eProsima/Fast-DDS.git -b v2.1.2 ~/FastDDS-2.0.2
WORKDIR /FastDDS-2.0.2
RUN mkdir build && cd build \
    cmake -DTHIRDPARTY=ON -DSECURITY=ON .. \
    make -j$(nproc --all) \
    sudo make install

RUN git clone --recursive https://github.com/eProsima/Fast-DDS-Gen.git -b v1.0.4 ~/Fast-RTPS-Gen \ 
&& cd ~/Fast-RTPS-Gen/gradle/wrapper
WORKDIR /Fast-RTPS-Gen 
RUN ./gradlew assemble && sudo env "PATH=$PATH" ./gradlew install

RUN cd $HOME
RUN mkdir /workspace/px4_ros_com_ros2/src -p
WORKDIR /workspace/px4_ros_com_ros2/src
RUN git clone https://github.com/sumedhreddy90/MIPS-RAAS-Challenge.git


RUN git config --global  user.name "someone" && git config --global user.email "someone@someplace.com"

RUN apt-get update  && apt-get install python-jinja2 -y && apt-get clean


WORKDIR /workspace

# Get fastrps tarball for fastrtpsgen binary
RUN wget -q https://www.eprosima.com/index.php/component/ars/repository/eprosima-fast-rtps/eprosima-fast-rtps-1-7-2/eprosima_fastrtps-1-7-2-linux-tar-gz?format=raw -O /tmp/fastrtps-1.7.2.tar.gz \
 && tar -xf /tmp/fastrtps-1.7.2.tar.gz

ENV FASTRTPSGEN_DIR /workspace/eProsima_FastRTPS-1.7.2-Linux/bin

WORKDIR /workspace/px4_ros_com_ros2

RUN . /opt/ros/foxy/setup.sh && colcon build --merge-install --packages-skip ros2_serial_example --cmake-args -DBUILD_TESTING=False
RUN . /workspace/px4_ros_com_ros2/install/setup.sh && colcon build


# optional dependency for camera streaming
RUN apt-get update \
 && apt-get install -y \
    python3-contextlib2 \
 && apt-get clean
