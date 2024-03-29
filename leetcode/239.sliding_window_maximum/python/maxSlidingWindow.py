
def maxSlidingWindow(nums, k):
    if not nums: return []
    window, res = [], []
    for i,x in enumerate(nums):
        if i >= k and window[0] <= i - k:
            window.pop(0)
        while window and nums[window[-1]] <= x:
            window.pop()
        window.append(i)
        if i >= k - 1:
            res.append(nums[window[0]])
    return res

nums = [1,3,2,4,5,7,9,1]
k = 5
print maxSlidingWindow(nums, k)
