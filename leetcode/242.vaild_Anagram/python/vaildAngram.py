#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 有效的字母异位词

# v1
def isAnagram(s, t):
    return sorted(s) == sorted(t)

v1 = 'cat'
v2 = 'tca'
# print(isAnagram(v1, v2))

# v2
def isAnagram1(s, t):
    dic1, dic2 = {},{}   # dict -> hashmap
    for item in s:
        dic1[item] = dic1.get(item, 0) + 1
    for item in t:
        dic2[item] = dic2.get(item, 0) + 1
    return dic1 == dic2

print(isAnagram1(v1, v2))
