#cd ~/kuLimo/colcon_sw/src
#ros2 pkg create --build-type ament_python hello_ros2
#code ~/.bashrc
#cd colcon_sw/
#colcon build
#source install/local_setup.bash
#ros2 run hello_ros2 hello_ros
#ros2 pkg list|grep heool
#colcon 명령문이 실행이 안 될 경우 
#추가 설치 한다. ==>   sudo apt install ros-dev-tools

#이 구조가 기본 구조임.

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Simple_pub(Node):
    def __init__(self):
        super().__init__('simple_pub')
        self.create_subscription(String, '/message', self.sub_callback, 10)

    def sub_callback(self, msg: String):
        print(msg.data)


def main():
    rclpy.init()
    node = Simple_pub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()

if __name__== '__main__':
    main()

