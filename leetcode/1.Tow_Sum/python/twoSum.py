#!/usr/bin/env python

def twoSum(nums, target):
    hash_map = dict()
    for i, x in enumerate(nums):
        if target - x in hash_map:
            return [i, hash_map[target -x]]
        hash_map[x] = i

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
