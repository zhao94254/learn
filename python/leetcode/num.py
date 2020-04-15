# -*- coding: utf-8 -*-
# @time: 2020-04-15 21:38
# @file: num.py

def threeSum(nums):
    lenn = len(nums)
    res = []
    sset = set()
    for i in range(lenn):
        for j in range(i+1, lenn):
            for z in range(j+1, lenn):
                
                if nums[i] + nums[j] + nums[z] == 0:
                    tmp = [nums[i], nums[j], nums[z]]
                    tmp.sort()
                    ssss = "{}".format(tmp)
                    print(ssss)
                    if ssss not in sset:
                        sset.add(ssss)
                        res.append([nums[i], nums[j], nums[z]])
    
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
    # print(threeSum([-1, 0, 1, 2, -1, -4]))
    
    print(twoSum([3,2,4], 6))