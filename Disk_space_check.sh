#!/bin/bash

disk=$(df / | awk 'NR==2 {print $5}' | tr -d '%')

echo "当前磁盘使用率：${disk}%"

if [ "$disk" -ge 80 ]; then
    echo "警告：磁盘使用率超过80%"
else
    echo "磁盘空间正常"
fi
