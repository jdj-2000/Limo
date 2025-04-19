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

class Hello(Node):
    def __init__(self):
        super().__init__('hello')
        self.create_timer(1, self.print_hello)
        self.count =0
    def print_hello(self):
        print(f"hello, ROS2 humble! {self.count}")
        self.count += 1

def main():
    rclpy.init()
    node = Hello()# 정석적인 방식으로 변경한 코드임..  class  선언 방식으로 사용해야 함.
    #node.create_timer(1, print_hello)
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()
    
if __name__ =="__main__":
    main()   

