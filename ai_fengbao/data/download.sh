#!/bin/bash

# this script is used to download the data from the remote server

mkdir videos

# 读取文件的每一行
while IFS= read -r line; do
  # 检查这行是否是HTTPS链接
  if [[ "$line" == https* ]]; then
    # 打印这个链接
    echo "Download : $line"
    bilili  $line  --disable-proxy -d videos  --num-threads 12 --yes
  fi
done < "video_link.txt"

echo "Download finished"
