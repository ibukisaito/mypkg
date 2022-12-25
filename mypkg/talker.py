# SPDX-FileCopyrightText: 2022 Ibuki Saito <s21c1050gb@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause
import rclpy                #ros2のクライアントのためのライブラリ
from rclpy.node import Node     #ノードを実装するためのNodeクラス
from std_msgs.msg import Int16  #通信の型(16ビットの符号付き整数)

rclpy.init()
node = Node("talker")           #ノードの作成(nodeという「オブジェクト」を作成)
pub = node.create_publisher(Int16,"countup",10)#パブリッシャのオブジェクト作成
n = 0#カウント用変数

def cd():
    global n
    msg= Int16()
    msg.data = n
    pub.publish(msg)
    n += 1

node.create_timer(0.5, cd)
rclpy.spin(node)

