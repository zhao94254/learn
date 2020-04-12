# -*- coding: utf-8 -*-
# @time: 2020-04-10 18:04
# @file: dp.py


def lcs(lst1, lst2):
    """
    leetcode 1143 最长公共子序列
    用一个二维数组记录每个位置
    :param lst1:
    :param lst2:
    :return:
    """
    res = [[0]*(len(lst1)+1) for _ in range(len(lst2)+1)]
    ks = []
    for i in range(len(lst2)):
        for j in range(len(lst1)):
            if lst2[i] == lst1[j]:
                res[i][j] = res[i-1][j-1] + 1
                ks.append(lst2[i])
            else:
                res[i][j] = max(res[i-1][j], res[i][j-1])
    return res[-2][-2]


def lics(lst):
    res = 0
    tmp = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[i-1]:
            tmp += 1
        else:
            tmp = 0
        res = max(res,tmp)
    return res


def longestPalindrome(s):
    """
    最长回文 暴力破解
    :param s:
    :return:
    """
    def is_p(s):
        return s == s[::-1]
    res = ""
    if len(s) == 1:
        return s
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if is_p(s[i:j]):
                
                if j-i > len(res):
                    res = s[i:j]
    return res


if __name__ == '__main__':
    # print(lcs("abcde", "ace"))
    
    # print(lics([1,2,3,4,5,6,7,3,2,34,5,6,7,1,2,3,4,5,6,7,8]))
    
    print(longestPalindrome("aa"))