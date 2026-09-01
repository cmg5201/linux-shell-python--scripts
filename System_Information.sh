#!/bin/bash

echo "===== 系统信息 ====="

echo "主机名："
hostname

echo "系统版本："
cat /etc/os-release | grep PRETTY_NAME

echo "内核版本："
uname -r

echo "CPU："
lscpu | grep "Model name" | head -1

echo "内存："
free -h

echo "磁盘："
df -h
