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
from geometry_msgs.msg import Twist
from rclpy.node import Node

class Move_turtle(Node):
    def __init__(self):
        super().__init__('move_turtle')
        self.create_timer(0.1, self.pub_turtle)
        self.pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.vel =0.0

    def pub_turtle(self):
        msg = Twist()
        msg.angular.z = 0.5      #python type  캐스팅이 자유롭다.
        msg.linear.x = self.vel  #그런데, 여기서 2로 주면 안된다. DDS 넘어갈 때 (c) 기에 ,,, type check 가 되야한다.
        self.pub.publish(msg)
        self.vel += 0.01

def main():
    rclpy.init()
    node = Move_turtle()# 정석적인 방식으로 변경한 코드임..  class  선언 방식으로 사용해야 함.
    #node.create_timer(1, print_hello)
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()
    
if __name__ =="__main__":
    main()   

