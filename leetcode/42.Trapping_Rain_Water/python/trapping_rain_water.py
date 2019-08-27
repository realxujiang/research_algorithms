#!/usr/bin/env python
#-*- coding: utf-8 -*-

def trap(height):
    res, mx, n = 0, 0, len(height)
    dp = []
    for i in range(0, n):
        dp.insert(i, mx)
        mx = max(mx, height[i])

    print "dp: " + str(dp)

    mx = 0
    y = n-1
    while y > 0:
         dp[y] = min(dp[y], mx)
         mx = max(mx, height[y])
         if (dp[y] - height[y] > 0):
            res += dp[y] - height[y]
         y = y - 1
    return res

height = [0,1,0,2,1,0,1,3,2,1,2,1]

print "trap: %s" %(trap(height))
