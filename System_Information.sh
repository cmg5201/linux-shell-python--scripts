#!/bin/bash
# 系统基础信息汇总脚本
echo "========== 系统基本信息 =========="
echo "主机名: $(hostname)"
echo "操作系统版本: $(cat /etc/redhat-release)"
echo "内核版本: $(uname -r)"
echo "系统运行时长: $(uptime | awk '{print $3,$4}' | sed 's/,//')"

echo -e "\n========== CPU信息 =========="
echo "CPU型号: $(grep "model name" /proc/cpuinfo | head -1 | awk -F: '{print $2}' | sed 's/^[ \t]*//')"
echo "CPU逻辑核心数: $(grep "processor" /proc/cpuinfo | wc -l)"

echo -e "\n========== 内存信息 =========="
free -h | awk 'NR==2{printf "总内存: %s\n已用内存: %s\n剩余内存: %s\n内存使用率: %.1f%%\n", $2,$3,$4,$3/$2*100}'

echo -e "\n========== 根分区磁盘信息 =========="
df -h / | awk 'NR==2{printf "总容量: %s\n已用: %s\n剩余: %s\n使用率: %s\n", $2,$3,$4,$5}'

echo -e "\n========== 网卡IP信息 =========="
ip addr | grep inet | grep -v inet6 | grep -v 127.0.0.1 | awk '{print "网卡"$NF": " $2}'
