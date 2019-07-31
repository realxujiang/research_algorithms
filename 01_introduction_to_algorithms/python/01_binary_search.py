#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 给定一个有序数组，快速查找某一元素是否在这个有序数据中，如果存在则打印此元素的位置。

def binary_search(elist, item):
  low = 0
  high = len(elist) - 1
  
  while low <= high:
    mid = (low + high)/2
    guess = elist[mid]
    if guess == item:
      return mid
    if guess > item:
      high = low - 1
    else:
      low = mid + 1
  return None

my_list = [1,3,5,7,9,10]

print(binary_search(my_list, 10)) # => 5

print(binary_search(my_list, 2)) # => None
