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
    

def exists(board, word):
    """
    面试题12. 矩阵中的路径
    dfs + 标记
    类似于求岛屿数量问题
    :param board:
    :param word:
    :return:
    """
    m, n = len(board), len(board[0])
    def dfs(i, j, k):
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
            return False
        if k == len(word)-1:
            return True
        tmp = board[i][j]
        board[i][j] = "."
        res = dfs(i-1, j, k+1) or dfs(i,j-1,k+1) or dfs(i, j+1, k+1) or dfs(i+1, j, k+1)
        board[i][j] = tmp
        return res
    
    for i in range(m):
        for j in range(n):
            print(i,j)
            if dfs(i,j,0):
                return True
    return False
    
    
def longest_brackets(s):
    res = 0
    tp = 0
    for i in s:
        if i == ")":
            if tp > 0:
                res += 2
            tp -= 1
        if i == "(":
            tp += 1
        if tp < 0:
            tp = 0
    return res

def xsqrt(x, gap):
    d = x/2
    low, up = 0, x
    while abs(d*d - x) > gap:
        print(d,low,up)
        if d*d > x:
            up = d
            d = up - (up-low) /2.0
            
        else:
            low = d
            d = low + (up-low) /2.0
            
    return d


def simplifyPath(path):
    """
    简化linux路径
    :param path:
    :return:
    """
    stack = []
    for i in path.split("/"):
        if i == ".":
            continue
        elif i == "..":
            if len(stack) > 0:
                stack.pop()
        elif i == "":
            pass
        else:
            stack.append(i)
    return "/".join(stack)

def intToRoman(d):
    """
    leetcode 12. 整数转罗马数字

    :param d:
    :return:
    """
    mp = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
    res = ""
    while d > 0:
        for m in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            if d >= m:
                t = mp[m] * (d//m)
                d = d % m
                res += t
    return res


def wordBreak(s, wordDict) -> bool:
    """
    workdict 中的单词是否可以组成 s
    :param s:
    :param wordDict:
    :return:
    """
    wmap = {i:True for i in wordDict}
    res = [0] * (len(s)+1)
    res[0] = 1
    for i in range(1, len(s)+1):
        for j in range(0, i):
            if res[j] == 1 and wmap.get(s[j:i], False):
                res[i] = 1
                break
    return res[-1] == 1
    
def convert(s: str, numRows: int):
    """
    z 字型打印
    :param s:
    :param numRows:
    :return:
    """
    res = ["" for i in range(len(s))]
    i, flag = 0, -1 # 借一个flag 从上到下从下到上
    for t in s:
        flag = -flag if i == 0 or i == numRows-1 else flag
        res[i] += t
        i = i+flag
    print(res)
    return res

def isMatch(s, p):
    """
    通配匹配 ？匹配任意一个 * 匹配0个或者多个
    :param s:
    :param p:
    :return:
    """
    i, j = 0, 0
    istar = -1
    jstar = -1
    while i < len(s):
        if j < len(p) and (s[i] == p[j] or p[j] == '?'):  # 正常匹配到
            i += 1
            j += 1
        elif j < len(p) and p[j] == "*":   # 遇到通配符，记录通配符起始位置
            istar = i
            jstar = j
            j += 1
        elif istar >= 0:  # 前面有可用的 *  istar 向后移动
            istar += 1
            i = istar
            j = jstar + 1
        else:
            return False
    for t in range(j, len(p)): # 去掉p 最后的*
        if p[t] != "*":
            return False
    return True
        

if __name__ == '__main__':
    # print(longestCommonPrefix(["dog","racecar","car"]))
    
    # print(reverse(0))
    
    # print(romanToInt("MCMXCIV"))
    
    # print(exists([["a","b"]], "ba"))
    
    # print(xsqrt(8.0, 0.04))
    
    # print(simplifyPath("/a//b////c/d//././/.."))
    #
    # print(intToRoman(58))
    
    # print(wordBreak("applepenapple", ["apple", "pen"]))
    #
    # convert("LEETCOD", 3)
    
    print(isMatch("aaa", "*?"))
    print(isMatch("abcdeasdfadf", "a*ea***d*"))
    
    