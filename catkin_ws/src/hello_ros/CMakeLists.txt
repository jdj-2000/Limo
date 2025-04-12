#sudo apt update
#sudo apt install git
#git clone https://github.com/jdj-2000/Limo.git

cmake_minimum_required(VERSION 3.0.2)
project(hello_ros)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  roscpp
  rospy
  std_msgs
)

catkin_package()

catkin_install_python(PROGRAMS
  script/hello.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)


include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

