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


def addTwoNumbers(l1, l2):
    """
    leetcode 445. 两数相加 II
    链表反转 + 链表相加
    :param l1:
    :param l2:
    :return:
    """
    l1r = reverse(l1)
    l2r = reverse(l2)
    
    res = Linklist()
    cur = res
    _sum = 0
    while l1r or l2r:
        _sum = _sum // 10
        if l1r:
            _sum += l1r.val
            l1r = l1r.next
        if l2r:
            _sum += l2r.val
            l2r = l2r.next
        cur.next = Linklist(_sum % 10)
        cur = cur.next
    if _sum >= 10:
        cur.next = Linklist(1)
        

    return reverse(res.next)
    

if __name__ == '__main__':
    lnk =  list_to_link(range(5))
    print(reverse(lnk))
    
    l1 = list_to_link([7,2,4,3])
    l2 = list_to_link([5,6,4])
    print(addTwoNumbers(l1, l2))