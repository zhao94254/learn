# -*- coding: utf-8 -*-
# @time: 2020-04-16 10:34
# @file: lst.py

def merge(lst):
    """
    56. 合并区间
    
    :param lst:
    :return:
    """
    res = []
    lst.sort(key=lambda x:x[0])
    for l in lst:
        if res and res[-1][1] >= l[0]:
            res[-1][1] = max(l[1], res[-1][1]) # 后面的并不一定是最大的
        else:
            res.append(l)
    return res

def coinChange(coins, x):
    if x < 0:
        return -1
    if x == 0:
        return 0
    res = 99999
    for coin in coins:
        
        subx = coinChange(coins, x-coin)
        if subx < 0:
            continue
        
        res = min(res, subx+1)
    
    return res

def numIslands(grid):
    res = 0
    
    def dfs(grid, i, j):
        if i<0 or j < 0 or j>=len(grid[0]) or i>= len(grid) or grid[i][j] != "1":
            return
        grid[i][j] = 2
        dfs(grid, i, j-1)
        dfs(grid, i, j + 1)
        dfs(grid, i-1, j)
        dfs(grid, i+1, j)
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                res += 1
                print(res, "s")
                dfs(grid, i, j)
                
    return res


def maxArea(grid):
    res = 0
    jj = 0
    def dfs(grid, i, j):
        nonlocal jj

        if i < 0 or j < 0 or j >= len(grid[0]) or i >= len(grid) or grid[i][j] != 1:
            return
        jj += 1
        
        grid[i][j] = 2
        dfs(grid, i, j - 1)
        dfs(grid, i, j + 1)
        dfs(grid, i - 1, j)
        dfs(grid, i + 1, j)
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                dfs(grid, i, j)
                res = max(res, jj)
                jj = 0
    return res


def prem(lst):
    """
    排列 -
    :param lst:
    :return:
    """
    res = []
    def helper(lst, start):
        if start >= len(lst):
            res.append(lst[:])
        for i in range(start, len(lst)):
            lst[i], lst[start] = lst[start], lst[i]
            helper(lst, start+1)
            lst[i], lst[start] = lst[start], lst[i]
    helper(lst, 0)
    return res

def combine(n, k):
    """
    组合
    :param n:
    :param k:
    :return:
    """
    res = []
    def dfs(start, tmp):
        if len(tmp) == k:
            res.append(tmp[:])
        for i in range(start, len(n)):
            tmp.append(n[i])
            dfs(i+1, tmp)
            tmp.pop()
    dfs(0, [])
    return res

def subset(t):
    """
    子集
    :param t:
    :return:
    """
    res = [[]]
    for i in range(len(t)):
        for j in res[:]:
            res.append(j + [t[i]])
    return res

def lengthOfLIS(lst):
    """
    最长递增子序列
    :param lst:
    :return:
    """
    dp = []
    for i in range(len(lst)):
        dp.append(1)
        for j in range(i):
            if lst[i] > lst[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def subsetss(n):
    res = []
    
    def dfs(s, nn, cur):
        if len(cur) == nn:
            res.append(cur[:])
            
        for i in range(s, len(n)):
            cur.append(n[i])
            dfs(i+1, nn, cur)
            cur.pop()
    for nn in range(len(n)+1):
        dfs(0, nn, [])
    return res

def combination(n, k):
    res = []
    
    def dfs(s, cur):
        if len(cur) == k:
            res.append(cur[:])
        for i in range(s, len(n)):
            cur.append(n[i])
            dfs(i+1, cur)
            cur.pop()
    dfs(0, [])
    return res


def permutation(n, k):
    res = []
    used = [False for _ in range(len(n))]
    def dfs(s, cur):
        if len(cur) == k:
            res.append(cur[:])
        for i in range(len(n)):
            if used[i]:
                continue
            cur.append(n[i])
            used[i] = True
            dfs(s + 1, cur)
            cur.pop()
            used[i] = False
    
    dfs(0, [])
    return res


def combinationSum(candidates, target):
    """
    和为 target 的组合数
    :param candidates:
    :param target:
    :return:
    """
    res = []

    def dfs(target, path, start):
        if target == 0:
            res.append(path[:])
            return
        for i in range(start, len(candidates)):
            _x = target - candidates[i] # 求解子问题
            if _x < 0:
                return
            path.append(candidates[i])
            dfs(_x, path, i) # 从i开始 - 可重复选
            path.pop()
        
        
    dfs(target, [], 0)
    return res

def rob(lst):
    if len(lst) < 2:
        return max(lst)
    dp = [0 for _ in range(len(lst))]
    dp[0] = lst[0]
    dp[1] = lst[1]
    for i in range(2, len(lst)):
        dp[i] = max(dp[i-1], lst[i]+dp[i-2])
    return dp[-1]

def rob1(lst):
    dp1, dp2 = 0, 0
    for i in lst:
        dp = max(dp1, dp2+i)
        dp2 = dp1
        dp1 = dp
    return dp1

def largestRectangleArea(heights):
    """
    最大矩阵面积
    :param heights:
    :return:
    """
    stack = []
    res = 0
    heights.append(0)  # 处理heights 本来就是一个单调栈的情况
    i, lenh = 0, len(heights)
    
    while i < lenh:
        if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
            stack.append(i)
        else:
            start = stack.pop()
            width = i if not stack else i - stack[-1]-1
            res = max(res, heights[start]*width)
            i -= 1
        i += 1
    
    return res

def maxArea1(lst):
    """
    盛水最多容器
    :param lst:
    :return:
    """
    res = 0
    l, r = 0, len(lst)-1
    while l < r:
        res = max(res, (r-l)*min(lst[r], lst[l]))
        if lst[l] < lst[r]:
            l += 1
        else:
            r -= 1
    return res

def maxPorfit(lst):
    """
    买卖股票 - 注意边界case
    :param lst:
    :return:
    """
    if len(lst) == 0:
        return 0
    res = 0
    m = lst[0]
    for i in range(len(lst)):
        m = min(m, lst[i]) # 维护一个当前最小值
        res = max(res, lst[i]-m)
    return res

if __name__ == '__main__':
    print(maxPorfit([7,6,5,4]))
    # print(maxArea1([8,1,2,3,8,2]))
    #
    # print(largestRectangleArea([1,2,3,4,5]))
    
    # print(merge([[1,3],[2,6],[8,10],[15,18]]))
    
    # print(coinChange([1,2,5, 10], 12))
    
    # print(merge_sort([4, 3, 1, 5, 43, 6, 23, 4, 5]))
    # print(numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
    # print(maxArea([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))
    #
    # print(prem([1,2,3]))
    #
    # print(combine("123", 2))
    #
    # print(subset([1,2,3]))
    
    # print(lengthOfLIS([10,9,2,5,3,7,101,18]))
    
    # print(combination("123", 2))
    #
    # print(permutation([1,2,3], 2))
    #
    # print(subsetss([1,2,3]))
    #
    # print(combination("123456", 2))
    
    # print(combinationSum([2,3,5], 8))
    
    # print(rob([2,7,9,3,1]))
    # print(rob1([1,7,9,3,1]))