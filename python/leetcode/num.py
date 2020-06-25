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
    
def mysqrtint(x):
    l, r = 0, x
    res = 0
    while l < r:
        mid = (r+l) // 2
        if mid*mid > x:
            r = mid-1
        else:
            res = mid
            l = mid+1
    return res
    
def mysqrt(x):
    l, r, = 0, x
    mid = (l+r)/2
    while abs(x - mid*mid) > 0.01:
        if mid*mid > x:
            r = mid
        else:
            l = mid
        mid = (r+l)/2
    return mid

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


def addStrings(num1: str, num2: str) -> str:
    """
    leetcode 415
    :param num1:
    :param num2:
    :return:
    """
    len1, len2 = len(num1) - 1, len(num2) - 1
    res = ""
    carry = 0
    while len1 >= 0 or len2 >= 0:
        n1 = int(num1[len1]) if len1 >= 0 else 0
        n2 = int(num2[len2]) if len2 >= 0 else 0
        tmp = n1 + n2 + carry
        res = str(tmp % 10) + res
        carry = int(tmp / 10)
        len1 -= 1
        len2 -= 1
    return '1' + res if carry > 0 else res

def multiply(num1: str, num2: str) -> str:
    """
    leetcode 43
    :param num1:
    :param num2:
    :return:
    """
    if num1 == "0" or num2 == "0":
        return '0'
    len1, len2 = len(num1), len(num2)
    res = [0] * (len1+len2-1)
    for i in range(len1):
        for j in range(len2):
            res[i+j] = res[i+j] + int(num1[i]) * int(num2[j])
    lst = res
    carry = 0
    for j in range(len(lst) - 1, -1, -1):
        tmp = lst[j] + carry
        lst[j] = tmp % 10
        carry = int(tmp / 10)

    return str(carry) + "".join(map(str, lst)) if carry > 0 else "".join(map(str, lst))


if __name__ == '__main__':
    # print(threeSum([-1, 0, 1, 2, -1, -4]))
    
    # print(twoSum([3,2,4], 6))
    
    # print(mysqrt(8))
    
    import random
    
    for i in range(100):
        a = random.randint(0, 10000)
        b = random.randint(0, 10000)
        if str(a*b) == multiply(str(a), str(b)):
            print(a, b)
    # print(multiply("99", "999"))
    
    # lst_carry([9, 27, 54, 45, 27, 0])
    # lst_carry([1,0,0])