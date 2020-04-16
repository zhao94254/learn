# -*- coding: utf-8 -*-
# @time: 2020-04-15 21:38
# @file: num.py

def threeSum(nums):
    """
    排序 + 指针
    :param nums:
    :return:
    """
    nums.sort()
    lenn = len(nums)
    res = set()
    for i in range(lenn):
        j, k = i+1, lenn-1
        while j < k:
            sm = nums[i] + nums[j] + nums[k]
            if sm == 0:
                res.add((nums[i], nums[j], nums[k]))
                k -= 1
                j += 1
            if sm > 0:
                k -= 1
            if sm < 0:
                j += 1
    return res
    
    

def twoSum(nums, target):
    """
    leetcode 1 找感觉
    :param nums:
    :param target:
    :return:
    """
    lenn = len(nums)
    rs = {}
    for i in range(lenn):
        rs[nums[i]] = i
    for i in range(lenn):
        t = target - nums[i]
        if t in rs and i != rs[t]:
            return [i, rs[t]]
    return [0, 0]



if __name__ == '__main__':
    print(threeSum([-1, 0, 1, 2, -1, -4]))
    
    print(twoSum([3,2,4], 6))