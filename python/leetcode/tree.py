# -*- coding: utf-8 -*-
# @time: 2020-05-11 10:56
# @file: tree.py

from python.tree import *


def maxDepth(root):
    if root is None:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1


def minDepth(root):
    """
    leetcode 111. 二叉树的最小深度
    - 根节点到树叶节点
    :param root:
    :return:
    """
    if root is None:
        return 0
    if not root.left:
        return minDepth(root.right) + 1
    if not root.right:
        return minDepth(root.left) + 1
    return min(minDepth(root.left), minDepth(root.right)) + 1


def hasPathSum(root, _sum):
    """
    leetcode 112 路径和
    :param root:
    :param _sum:
    :return:
    """
    if root is None:
        return False
    if root.val == _sum and root.left is None and root.right is None:
        return True
    return hasPathSum(root.left, _sum-root.val) or hasPathSum(root.right, _sum-root.val)


def levelOrder(root):
    """
    leetcode 102 二叉树层次遍历
    :param root:
    :return:
    """
    res = []
    _q = [root]
    def helper(_q, res, level):
        while _q:
            if len(res) < level+1:
                res.append([])
            _root = _q.pop()
            res[level].append(_root.val)
            if _root.left:
                _q.append(_root.left)
                helper(_q, res, level+1)
            if _root.right:
                _q.append(_root.right)
                helper(_q, res, level + 1)
        return
    helper(_q, res, 0)
    return res
    
def isSymmetric(root):
    """
    是否是镜像树
    :param root:
    :return:
    """
    def helper(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return helper(left.left, right.right) and helper(left.right, right.left)
    if root is None:
        return True
    return helper(root.left, root.right)

def isSubtree(s, t):
    if t is None:
        return True
    if s is None:
        return False
    if isSameTree(s, t):
        return True
    return isSubtree(s.left, t) or isSubtree(s.right, t)

def isSameTree(s, t):
    if s is None or t is None:
        return s == t
    return s.val == t.val and isSameTree(s.left, t.left) and isSameTree(s.right, t.right)


if __name__ == '__main__':
    
    xtree = BinTree().list_to_tree(range(10))
    # print(xtree)
    
    # print(tree_height(xtree))
    # print(tree_m_height(xtree))
    
    print(hasPathSum(xtree, 11))
    
    print(levelOrder(xtree))