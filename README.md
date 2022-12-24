# mypkg
# robosys2022
ロボットシステム学のROS2講義用のリポジトリ


![test](https://github.com/ibukisaito/mypkg/actions/workflows/test.yml/badge.svg)
# ノード

## talker.py
### 内容
* countupというオブジェクトを作成
* 0.5秒ごとに数字を出力

## listener.py
### 内容
* countupからデータを読み込み標準出力に出力する
## 実行準備
以下を実行
```
$ cd ~/ros2_ws;colcon build
$ source 
```
## 入出力例
```
$ ros2 launch mypkg talk.listen_launch.py
[listener-2] [INFO] [1671907754.131586200] [Listener]: Listen: 7 <- 出力例
```

# 実用なソフトウェア
* テスト済み
  * python:3.10


# テスト環境
* Ubuntu 22.04.1 LTS

# ライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです
	* [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* © 2022 Ibuki Saito
