# -*- coding: utf-8 -*-
# @time: 2020-04-06 18:42
# @file: sliding_window.py

# 滑动窗口

def sliding_window_prob(s):
    """
    右指针一直向右，当不符合条件的时候左指针前移，直到符合条件
    :param s:
    :return:
    """
    l, r = 0, 0
    tmp = set()
    while r < len(s):
        
        r += 1
        
        while s[l]:
            tmp.remove(s[l])
            l += 1
    return


def lengthOfLongestSubstring(s):
    """
    最长子序列
    :param s:
    :return:
    """
    res = 0
    clen = 0
    lookup = set()
    left = 0
    for i in range(len(s)):
        clen += 1
        while s[i] in lookup: # 左指针右移
            lookup.remove(s[left])
            clen -= 1
            left += 1
        lookup.add(s[i])
        res = max(res, clen)
    return res
    

if __name__ == '__main__':
    print(lengthOfLongestSubstring("baacdea"))
    print(countN(534))