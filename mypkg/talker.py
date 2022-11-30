import rclpy                #ros2のクライアントのためのライブラリ
from rclpy.node import Node     #ノードを実装するためのNodeクラス
from person_msgs.srv import Query  #通信の型(16ビットの符号付き整数)

def cd(request, response):
    if  request.name == "齊藤伊吹":
        response.age = 19
    else:
        response.age = 255

    return response

rclpy.init()
node = Node("talker")           #ノードの作成(nodeという「オブジェクト」を作成)
srv = node.create_service(Query,"query",cd)#パブリッシャのオブジェクト作成
rclpy.spin(node)


