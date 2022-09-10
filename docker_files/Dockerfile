FROM osrf/ros:foxy-desktop

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

# Micrortps demo dependencies
# TODO(add as declared dependencies)
RUN apt-get update \
&& apt-get install -y \
  python-future \
  python3-future \
  python-lxml \
  python3-jinja2 -y \
  openjdk-8-jdk \
  rsync \
  python-empy \
  python-toml \
  python-yaml \
  python-numpy \
  python-catkin-pkg \
  python3-tk \
  libpulse-mainloop-glib0 \
  pulseaudio \
  && apt-get clean \
  && pip3 install catkin-pkg empy toml numpy tk future

# optional dependency for qgc
RUN apt-get update \
 && apt-get install -y \
    speech-dispatcher \
    libimage-exiftool-perl \
    gstreamer1.0-libav \
 && apt-get clean

# optional dependency for camera streaming
RUN apt-get update \
 && apt-get install -y \
    gstreamer1.0-alsa \
    libgstreamer-plugins-base1.0-dev \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-ugly \
 && apt-get clean

# Make sure everything is up to date before building from source
RUN apt-get update \
  && apt-get dist-upgrade -y \
  && apt-get clean

RUN /bin/sh -c 'echo ". /opt/ros/foxy/setup.bash" >> ~/.bashrc' \
  && /bin/sh -c 'echo ". /usr/share/gazebo/setup.sh" >> ~/.bashrc'

RUN mkdir  /workspace/px4_ros_com_ros2/src -p
WORKDIR /workspace/px4_ros_com_ros2/src
RUN git clone https://github.com/sumedhreddy90/MIPS-RAAS-Challenge.git

# TODO(ahcorde): remove this cherry-pick when PR is merged
RUN git config --global  user.name "someone" && git config --global user.email "someone@someplace.com"

RUN apt-get update  && apt-get install python-jinja2 -y && apt-get clean

RUN git clone https://github.com/mavlink/mavlink -b 1.0.12 --recursive && \
    git clone https://github.com/mavlink/mavlink-gbp-release && \
    mv mavlink-gbp-release/patch/* mavlink

COPY files/mavlink/package.xml /workspace/px4_ros_com_ros2/src/mavlink/package.xml

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

