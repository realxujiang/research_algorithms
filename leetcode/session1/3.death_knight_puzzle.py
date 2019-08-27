#!/usr/bin/env python
#-*- coding: utf-8 -*-

# by http://acm.hdu.edu.cn/showproblem.php?pid=1248

def bestPlan(price):
    t = 9
    n = 3
    dp = []
    alist = [150, 200, 350]
    while (--t and t > 0):
        sum = 0
        for i in range(3):
            for j in range(alist[i], n):
                dp[j] = max(dp[j], dp[j-w[i]]+w[i])
        return n - dp[n]
    return 0

if __name__ == "__main__":
    print bestPlan(900)

