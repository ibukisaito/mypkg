import rclpy                #ros2のクライアントのためのライブラリ
from rclpy.node import Node     #ノードを実装するためのNodeクラス
from std_msgs.msg import Int16  #通信の型(16ビットの符号付き整数)

class Talker():
    def __init__(self,node_ref):
        self.pub = node_ref.create_publisher(Int16,"countup",10)
        self.n = 0
        node_ref.create_timer(0.5,self.cb)

    def cb(self):
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.n += 1

def main():
    rclpy.init()
    node = Node("talker")           #ノードの作成(nodeという「オブジェクト」を作成)
    talker = Talker(node)
    rclpy.spin(node)

if __name__ == '__main__':
    main()

