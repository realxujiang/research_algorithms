#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 三数之和等于0, 打印出三个值
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

def threeSum(nums):
    result = []
    target = 0
    nums.sort()
    for a in range(len(nums)-2):
        if a == 0 or nums[a] > nums[a-1]:
            b = a + 1
            c = len(nums) - 1
            while b < c:
                if nums[b] + nums[c] == -nums[a]:
                    result.append([nums[a], nums[b], nums[c]])
                    b+=1
                    c-=1
                    while b < c and nums[b] == nums[b-1]: 
                        b+=1
                    while b < c and  nums[c] == nums[c+1]:
                        c-=1
                elif nums[b] + nums[c] < -nums[a]:
                    while b < c:
                        b += 1
                        if nums[b] > nums[b-1]: break
                else:
                    while b < c:
                        c -= 1
                        if nums[c] < nums[c+1]: break
    return result

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
