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

    
if __name__ == '__main__':
    # print(merge([[1,3],[2,6],[8,10],[15,18]]))
    
    # print(coinChange([1,2,5, 10], 12))
    
    # print(merge_sort([4, 3, 1, 5, 43, 6, 23, 4, 5]))
    # print(numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
    print(maxArea([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))