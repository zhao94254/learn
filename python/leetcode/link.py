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


def hasCycle(head: Linklist):
    """
    leetcode 141. 环形链表
    :param head:
    :return:
    """
    a, b = head, head
    while a or b:
        if not a.next or not b.next:
            return False
        if a == b:
            return True
        a = a.next.next
        b = b.next
    return False

if __name__ == '__main__':
    lnk =  list_to_link(range(5))
    print(reverse(lnk))