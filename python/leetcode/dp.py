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


def longestPalindrome_409(s):
    """
    leetcode 409. 最长回文串
    偶数次的可以全部使用，奇数最多用一个
    :type s: str
    :rtype: int
    """
    mp = {}
    for i in s:
        mp[i] = mp.get(i, 0) + 1
    res = 0
    p = 0
    for i, j in mp.items():
        if j % 2 == 1:
            res += (j - 1)
            p = 1
        if j % 2 == 0:
            res += j
    return res + p

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

def longestSubPalindrome(s):
    """
    leetcode 5 最长回文字串
    :param s:
    :return:
    """
    n = len(s)
    
    def getLen(l, r):
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
            
        return  r-l-1
    length = 0
    start, end = 0, 0
    for i in range(n):
        
        tmp = max(getLen(i,i), getLen(i,i+1))
        if tmp < length:
            continue
        length = tmp
        start = i - (length-1) // 2
    
    return s[start:start+length]
    

def longestPalindromeV1(s):
    """
    leetcode 5. 最长回文子串
    最长回文字串 中心扩展法 O2
    :param s:
    :return:
    """
    lens = len(s)
    start, end = 0, 0
    tmp = 0
    if lens < 2:
        return s
    for i in range(len(s)): # 扫一遍奇数情况
        left, right = i-1, i+1
        while left >= 0 and right < lens and s[left]==s[right]:
            print(right, left)
            if right - left > tmp:
                tmp = right - left
                start = left
                end = right
            left -= 1
            right += 1
    for i in range(len(s)): # 扫偶数
        left, right = i-1, i
        while left >= 0 and right < lens and s[left]==s[right]:
            if right - left > tmp:
                tmp = right-left
                start = left
                end = right
            left -= 1
            right += 1
    return s[start:end+1]


if __name__ == '__main__':
    # print(lcs("abcde", "ace"))
    
    # print(lics([1,2,3,4,5,6,7,3,2,34,5,6,7,1,2,3,4,5,6,7,8]))
    
    # print(longestPalindrome("aa"))
    #
    # print(longestPalindromeV1("abccba"))
    # print(longestPalindromeV1("aababcc"))
    # print(longestPalindromeV1("abb"))
    # print(longestPalindromeV1("ccc"))
    
    print(longestSubPalindrome("cbbd"))
    
    # print(longestPalindromet("ccc"))