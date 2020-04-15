# -*- coding: utf-8 -*-
# @time: 2020-04-11 08:43
# @file: str.py


def longestCommonPrefix(strs):
    """
    leetcode 14 最长公共前缀..
    :param strs:
    :return:
    """
    res = 0
    for _ in range(len(strs[0])):
        for i in range(1, len(strs)):
            if len(strs[i]) <= res or len(strs[i-1]) <= res or  strs[i][res] != strs[i-1][res]:
                return strs[0][:res]
        res += 1
    return strs[0][:res]


def reverse(x):
    """
    leetcode  7 整数反转
    考虑溢出的处理
    :param x:
    :return:
    """
    if x == 0:
        return x
    res = []
    f = False
    if x < 0:
        x = -x
        f = True
    while x > 0:
        res.append(x % 10)
        x = x // 10
    ks = int(''.join(map(str, res)))
    if ks > 2 ** 31:
        return 0
    if f:
        return -ks
    return ks

def romanToInt(s):
    """
    leetcode 13. 罗马数字转整数
    :param s:
    :return:
    """
    mp = {
        "I":1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C":100,
        "D":500,
        "M":1000,
        "IV":4,
        "IX":9,
        "XL":40,
        "XC":90,
        "CD":400,
        "CM":900,
    }
    lens = len(s)
    res = 0
    i = 0
    while i < lens:
        if i+1 < lens and s[i:i+2] in mp:
            res += mp[s[i:i+2]]
            i += 2
        else:
            res += mp[s[i]]
            i += 1
    return res
    

if __name__ == '__main__':
    # print(longestCommonPrefix(["dog","racecar","car"]))
    
    print(reverse(0))
    
    print(romanToInt("MCMXCIV"))