# -*- coding: utf-8 -*-
# @time: 2020-04-06 18:42
# @file: link.py

from python.link import *


def reverse(link: Linklist):
    """
    leetcode 206 链表反转
    :param link:
    :return:
    """
    res = None
    while link:
        rest = link.next
        link.next = res
        res = link
        link = rest
    return res


if __name__ == '__main__':
    lnk =  list_to_link(range(5))
    print(reverse(lnk))