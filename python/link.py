# -*- coding: utf-8 -*-
# @time: 2020-04-06 18:31
# @file: link.py

class Linklist:
    def __init__(self, x=None, next=None):
        self.val = x
        self.next = next

    def __str__(self):
        return "{}-->{}".format(self.val, self.next)

    __repr__ = __str__

    def __len__(self):
        if self.next is None:
            return 1
        return 1 + len(self.next)

    def __getitem__(self, i):
        if self.next is None:
            return None
        if i == 0:
            return None
        else:
            return self.next[i - 1]

    def __call__(self, x: list):
        return self.list_to_link(x)

    def list_to_link(self, x: list):
        """将数组转化为链表"""
        head = Linklist(0)
        cur = head
        for i in x:
            if isinstance(i, Linklist):
                cur.next = i
            else:
                cur.next = Linklist(i)
            cur = cur.next
        return head.next


def list_to_link(x: list):
    """
    :param x: [1,2,3]
    :return:
    """
    head = Linklist(0)
    cur = head
    for i in x:
        if isinstance(i, Linklist):
            cur.next = i
        else:
            cur.next = Linklist(i)
        cur = cur.next
    return head.next