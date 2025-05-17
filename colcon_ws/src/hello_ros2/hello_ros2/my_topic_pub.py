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


# ros2 run hello_ros2 my_topic_pub
# ros2 topic echo /message
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from user_interface.msg import MyTopic

class Simple_pub(Node):
    def __init__(self):
        super().__init__("myTopicPub")  # node name
        self.create_timer(0.1, self.pub_turtle)
        self.pub = self.create_publisher(MyTopic, "/message", 10)
        self.count = 0

    def pub_turtle(self):
        msg = MyTopic()
        msg.a = 10
        msg.b = 20
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = f"내가 만든 토픽 입니다.{self.count}"
        self.pub.publish(msg)
        self.count += 1


def main():
    rclpy.init()
    node = Simple_pub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()

if __name__== '__main__':
    main()

