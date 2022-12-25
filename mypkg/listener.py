# SPDX-FileCopyrightText: 2022 Ibuki Saito <s21c1050gb@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause
import rclpy                #ros2のクライアントのためのライブラリ
from rclpy.node import Node     #ノードを実装するためのNodeクラス
from std_msgs.msg import Int16  #通信の型(16ビットの符号付き整数)

def cd(msg):
    global node
    node.get_logger().info("Listen: %d" % msg.data)

rclpy.init()
node = Node("Listener")
pub = node.create_subscription(Int16,"countup",cd,10)
rclpy.spin(node)

