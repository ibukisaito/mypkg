#!/bin/bash

dir=~
["$1" != ""] && dir="$1"

cd $dir/ros2_ws
colocn build
source $dir/.bashrc
timeout 10 ros2 launch mypkg talk_listen_launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log
gerp 'Listen: 10'
