FROM arm64v8/ubuntu:focal

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN apt-get update && apt-get -y --quiet --no-install-recommends install \
		bzip2 \
		ca-certificates \
		ccache \
		cmake \
		cppcheck \
		curl \
		dirmngr \
		doxygen \
		file \
		g++ \
		gcc \
		gdb \
		git \
		gnupg \
		gosu \
		lcov \
		libfreetype6-dev \
		libgtest-dev \
		libpng-dev \
		libssl-dev \
		lsb-release \
		make \
		ninja-build \
		openjdk-8-jdk \
		openjdk-8-jre \
		openssh-client \
		pkg-config \
		python3-dev \
		python3-pip \
		rsync \
		shellcheck \
		tzdata \
		unzip \
		valgrind \
		wget \
		xsltproc \
		zip \
	&& apt-get -y autoremove \
	&& apt-get clean autoclean \
	&& rm -rf /var/lib/apt/lists/{apt,dpkg,cache,log} /tmp/* /var/tmp/*

# gtest
RUN cd /usr/src/gtest \
	&& mkdir build && cd build \
	&& cmake .. && make -j$(nproc) \
	&& find . -name \*.a -exec cp {} /usr/lib \; \
	&& cd .. && rm -rf build

# Install Python 3 pip build dependencies first.
RUN python3 -m pip install --upgrade pip wheel setuptools

# Python 3 dependencies installed by pip
RUN python3 -m pip install argparse argcomplete coverage cerberus empy jinja2 kconfiglib \
		matplotlib==3.0.* numpy nunavut>=1.1.0 packaging pkgconfig pyros-genmsg pyulog \
		pyyaml requests serial six toml psutil pyulog wheel jsonschema pynacl

# manual ccache setup
RUN ln -s /usr/bin/ccache /usr/lib/ccache/cc \
	&& ln -s /usr/bin/ccache /usr/lib/ccache/c++



# Gradle (Required to build Fast-RTPS-Gen)
RUN wget -q "https://services.gradle.org/distributions/gradle-6.3-rc-4-bin.zip" -O /tmp/gradle-6.3-rc-4-bin.zip \
	&& mkdir /opt/gradle \
	&& cd /tmp \
	&& unzip -d /opt/gradle gradle-6.3-rc-4-bin.zip \
	&& rm -rf /tmp/*

ENV PATH "/opt/gradle/gradle-6.3-rc-4/bin:$PATH"

# Intall foonathan_memory from source as it is required to Fast-RTPS >= 1.9
RUN git clone https://github.com/eProsima/foonathan_memory_vendor.git /tmp/foonathan_memory \
	&& cd /tmp/foonathan_memory \
	&& mkdir build && cd build \
	&& cmake .. \
	&& cmake --build . --target install -- -j $(nproc) \
	&& rm -rf /tmp/*

# create user with id 1001 (jenkins docker workflow default)
RUN useradd --shell /bin/bash -u 1001 -c "" -m user && usermod -a -G dialout user

# setup virtual X server
RUN mkdir /tmp/.X11-unix && \
	chmod 1777 /tmp/.X11-unix && \
	chown -R root:root /tmp/.X11-unix
ENV DISPLAY :99

ENV CCACHE_UMASK=000
ENV FASTRTPSGEN_DIR="/usr/local/bin/"
ENV PATH="/usr/lib/ccache:$PATH"
ENV TERM=xterm
ENV TZ=UTC

# SITL UDP PORTS
EXPOSE 14556/udp
EXPOSE 14557/udp

# setup environment
ENV ROS_DISTRO galactic

# setup ros2 keys
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

# setup sources.list
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null

# install bootstrap tools
RUN apt-get update \
	&& apt-get install --quiet -y \
		python3-colcon-common-extensions \
		python3-colcon-mixin \
		python3-rosdep \
		python3-vcstool \
	&& apt-get -y autoremove \
	&& apt-get clean autoclean \
	&& rm -rf /var/lib/apt/lists/{apt,dpkg,cache,log} /tmp/* /var/tmp/*

# install ros2 desktop
RUN apt-get install --quiet --no-install-recommends -y \
		ros-$ROS_DISTRO-desktop \
		ros-$ROS_DISTRO-launch-testing-ament-cmake \
		ros-$ROS_DISTRO-ros2bag \
		ros-$ROS_DISTRO-rosidl-generator-dds-idl \
	&& apt-get -y autoremove \
	&& apt-get clean autoclean \
	&& rm -rf /var/lib/apt/lists/{apt,dpkg,cache,log} /tmp/* /var/tmp/*

# Install Python 3 packages needed for testing
RUN pip3 install -U \
		argcomplete \
		flake8 \
		flake8-blind-except \
		flake8-builtins \
		flake8-class-newline \
		flake8-comprehensions \
		flake8-deprecated \
		flake8-docstrings \
		flake8-import-order \
		flake8-quotes \
		pytest-repeat \
		pytest-rerunfailures

# bootstrap rosdep
RUN rosdep init && rosdep update

# setup colcon mixin and metadata
RUN colcon mixin add default \
		https://raw.githubusercontent.com/colcon/colcon-mixin-repository/master/index.yaml \
	&& colcon mixin update \
	&& colcon metadata add default \
		https://raw.githubusercontent.com/colcon/colcon-metadata-repository/master/index.yaml \
	&& colcon metadata update

# Install Fast-DDS 2.3.1
RUN rm -rf /usr/local/include/fastrtps /usr/local/share/fastrtps /usr/local/lib/libfastrtps* \
	&& git clone --recursive https://github.com/eProsima/Fast-DDS.git -b v2.3.1 /tmp/FastRTPS-2.3.1 \
	&& cd /tmp/FastRTPS-2.3.1 \
	&& mkdir build && cd build \
	&& cmake -DTHIRDPARTY=ON -DSECURITY=ON .. \
	&& cmake --build . --target install -- -j $(nproc) \
	&& rm -rf /tmp/*

# create and start as LOCAL_USER_ID
COPY scripts/entrypoint.sh /usr/local/bin/entrypoint.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

# source
CMD ["/bin/bash"]
