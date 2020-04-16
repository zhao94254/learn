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

if __name__ == '__main__':
    print(merge([[1,3],[2,6],[8,10],[15,18]]))
    
        
        