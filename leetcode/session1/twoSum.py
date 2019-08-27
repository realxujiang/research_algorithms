def twoSum(nums, target):
    hash_map = dict()
    for i,v in enumerate(nums):
        if target - v in hash_map:
            return [i, hash_map[target - v]]    
        hash_map[v] = i

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
