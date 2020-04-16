# -*- coding: utf-8 -*-
# @time: 2020-04-15 08:40
# @file: binary.py


def hammingWeight(n):
    """
    面试题15. 二进制中1的个数
    :type n: int
    :rtype: int
    """
    res = 0
    while n:
        res += 1
        n = n & (n - 1)
    return res


def pow_2(x):
    """
    2 的指数
    :param x:
    :return:
    """
    if x < 0:
        return False
    return (x & (x-1)) == 0