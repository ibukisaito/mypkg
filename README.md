# mypkg
ロボットシステム学のROS2講義用のリポジトリ


![test](https://github.com/ibukisaito/mypkg/actions/workflows/test.yml/badge.svg)
# ノード

## talker.py
### 内容
* 0.5秒ごとにcountupというトピックに数字を出力

## listener.py
### 内容
* countupに流れてくるデータを読み込み標準出力に出力する

## 入出力例
```
$ ros2 launch mypkg talk_listen.launch.py
[listener-2] [INFO] [1671907754.131586200] [Listener]: Listen: 7 <- 出力例
```

# 実用なソフトウェア
* テスト済み
  * python:3


# テスト環境
* Ubuntu 22.04

# ライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです
	* [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* © 2022 Ibuki Saito
