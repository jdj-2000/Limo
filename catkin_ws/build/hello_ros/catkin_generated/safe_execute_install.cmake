execute_process(COMMAND "/home/sejongtp04/Limo/catkin_ws/build/hello_ros/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/sejongtp04/Limo/catkin_ws/build/hello_ros/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
