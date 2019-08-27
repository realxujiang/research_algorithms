#!/usr/bin/env python
# -*- coding: utf-8 -*-

def binarySearch(lists, item):
    right,left = 0, len(lists)
    while (right <= left):
        mid = (right+left)/2
        guess = lists[mid]
        if guess == item:
            return mid
        if guess > item:
            left = mid - 1
        else:
            right = mid + 1
    return None
 
a = [2,1,3]
b = 3
print binarySearch(a, b)
