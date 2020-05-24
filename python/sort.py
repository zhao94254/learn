# -*- coding: utf-8 -*-
# @time: 2020-05-24 13:28
# @file: sort.py

import heapq
import random


def buildHeap(lst):
    for i in range(len(lst)//2, -1, -1):
        heapify(lst, len(lst), i)
    return lst


def heapify(lst, n, i):
    """
    构建大顶堆
     - 每个父节点大于所有子节点
    :param lst:
    :param n:
    :param i:
    :return:
    """
    left, right = 2*i+1, 2*i+2
    largest = i
    if left < n and lst[left] > lst[largest]:
        largest = left
    if right < n and lst[right] > lst[largest]:
        largest = right
    if largest != i:
        lst[largest], lst[i] = lst[i], lst[largest]
        heapify(lst, n, largest)


def heap_sort(lst):
    _h = buildHeap(lst)
    print(_h)
    for i in range(len(lst)-1, -1, -1):
        print(_h[0], _h[i], "s")
        _h[0], _h[i] = _h[i], _h[0]
        print(_h[0], _h[i], "e")
        heapify(_h, i, 0)
    return _h


def topK(lst, k):
    _q = lst[:k]
    buildHeap(_q)

    for i in range(k, len(lst)):
        if lst[i] < _q[0]: # 更新最大的
            _q[0] = lst[i]
            heapify(_q, k, 0)
    return _q

if __name__ == '__main__':
    # print(buildHeap(list(range(10))[::-1]))
    #
    lst = [random.randint(0, 100) for _ in range(100)]
    # print(heap_sort(lst))
    
    print(topK(list(set(lst)), 3))
    lst.sort()
    print(lst)
    