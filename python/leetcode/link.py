# -*- coding: utf-8 -*-
# @time: 2020-04-06 18:42
# @file: link.py

from python.link import *

def reverseKgroup(link, k):
    ret = Linklist(0)
    cur = ret
    while True:
        count = k
        tmp = []
        tp = link
        while count > 0 and tp: # 压栈
            tmp.append(tp)
            tp = tp.next
            count -= 1
        
        if count > 0: # 不够k个
            break
        while len(tmp) > 0:
            cur.next = tmp.pop()
            cur = cur.next
        
        cur.next = tp # 链接剩下的
        link = tp # 从后面开始
        
        
    return ret.next

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


def mergeTwoLists(l1, l2):
    """
    leetcode 21. 合并两个有序链表
    :param l1:
    :param l2:
    :return:
    """
    dummy = Linklist(0)
    cur = dummy
    while l1 and l2:
        if l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
    if l1:
        cur.next = l1
    if l2:
        cur.next = l2
        
    return dummy.next


def removeNthFromEnd(head, n):
    """
    leetcode 19
    :param head:
    :param n:
    :return:
    """
    dummy = Linklist()
    dummy.next = head
    slow = dummy
    fast = dummy
    while n >= 0:
        n -= 1
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    if slow.next:
        slow.next = slow.next.next
    return dummy.next


if __name__ == '__main__':
    lnk =  list_to_link(range(1, 2))
    # print(reverse(lnk))
    # print(reverseKgroup(lnk, 4))
    # l1 = list_to_link([7,2,4,3])
    # l2 = list_to_link([5,6,4])
    # print(addTwoNumbers(l1, l2))
    
    # print(mergeTwoLists(list_to_link([1,3,5,9]), list_to_link([2,4,7,8])))
    print(lnk)
    
    print(removeNthFromEnd(lnk, 1))