FROM osrf/ros:galactic-desktop

#USER  root

RUN apt-get update && apt-get install -y nano && rm -rf /var/lib/apt/lists/*

RUN apt update && sudo apt install -y locales && locale-gen en_US en_US.UTF-8 && update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 && export LANG=en_US.UTF-8 && rm -rf /var/lib/apt/lists/*

RUN apt update && apt install -y software-properties-common && add-apt-repository universe && rm -rf /var/lib/apt/lists/*

RUN apt update && apt install -y curl && curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg && rm -rf /var/lib/apt/lists/*

RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

RUN apt update && apt upgrade -y && apt install -y ros-galactic-desktop && apt install -y ros-dev-tools && rm -rf /var/lib/apt/lists/*

RUN apt update && curl -sSL http://get.gazebosim.org | sh && apt install -y ros-galactic-gazebo-ros-pkgs && rm -rf /var/lib/apt/lists/*

#RUN /bin/bash -c "cd / && source /opt/ros/galactic/setup.bash && mkdir bt_lib && cd bt_lib && git clone https://github.com/BehaviorTree/BehaviorTree.CPP.git -b v3.8"

#RUN cd /bt_lib/BehaviorTree.CPP/ && mkdir build && cd build && cmake .. && make --jobs=8 && make install --jobs=8 && cd /

RUN apt update \ 
    && apt install -y ros-galactic-navigation2 \
    ros-galactic-ros2-control \
    ros-galactic-ros2-controllers \ 
    ros-galactic-cartographer-ros \ 
    ros-galactic-slam-toolbox \
    nlohmann-json3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN apt update && apt install -y libzmq3-dev libboost-dev && rm -rf /var/lib/apt/lists/* 

RUN mkdir g2o && cd g2o && git clone https://github.com/ros2-gbp/libg2o-release.git -b debian/galactic/libg2o \
    && cd libg2o-release && mkdir build && cd build && cmake ../ && make --jobs=10 && make install --jobs=10

ARG USERNAME=ros
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
  && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
  && mkdir /home/$USERNAME/.config && chown $USER_UID:$USER_GID /home/$USERNAME/.config

RUN apt-get update \
  && apt-get install -y sudo \
  && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME\
  && chmod 0440 /etc/sudoers.d/$USERNAME \
  && rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /entrypoint.sh
COPY bashrc /home/${USERNAME}/.bashrc

#USER root
#ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
CMD ["bash"]

