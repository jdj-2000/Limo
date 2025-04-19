import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/jdj/kuLimo/colcon_ws/install/hello_ros2'
